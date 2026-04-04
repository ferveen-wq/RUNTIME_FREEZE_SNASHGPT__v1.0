from __future__ import annotations


def manage_deferred_video(
    conversation_phase: str,
    service: str,
    primary_trigger: str | None = None,
    topic_previously_discussed: bool = False,
    comparison_intent: bool = False,
    objection_signal: str | None = None,
    trust_or_risk_doubt: bool = False,
    video_already_shown: bool = False,
    silence_active: bool = False,
    silence_suppressed: bool = False,
    existing_deferred_trigger: str | None = None,
) -> dict:
    """
    Deferred visual decision layer.

    This function does NOT generate customer-facing text.
    It only decides whether a previously eligible video
    should be stored, held, released, or suppressed.
    """

    # Hard blockers
    if video_already_shown:
        return {
            "store_deferred": False,
            "release_now": False,
            "deferred_trigger": existing_deferred_trigger,
            "release_reason": None,
            "suppressed": True,
        }

    # Silence must NOT actively trigger visuals
    # It may only block release
    if silence_active or silence_suppressed:
        return {
            "store_deferred": False,
            "release_now": False,
            "deferred_trigger": existing_deferred_trigger,
            "release_reason": None,
            "suppressed": True,
        }

    # Early phases: store only, do not release
    if conversation_phase in ["Phase0", "Phase1", "Phase2"]:
        if primary_trigger:
            return {
                "store_deferred": True,
                "release_now": False,
                "deferred_trigger": primary_trigger,
                "release_reason": None,
                "suppressed": False,
            }

        return {
            "store_deferred": False,
            "release_now": False,
            "deferred_trigger": existing_deferred_trigger,
            "release_reason": None,
            "suppressed": False,
        }

    trigger_to_use = existing_deferred_trigger or primary_trigger

    # Release in later stages only if the topic was actually discussed before
    # and the customer now shows a valid release signal.
    release_signal = (
        comparison_intent
        or trust_or_risk_doubt
        or objection_signal in {
            "PRICE_COMPARISON",
            "TRUST_OR_RISK",
            "MISUNDERSTANDING",
        }
    )

    if conversation_phase in ["Phase4", "Phase5", "Phase7", "Phase8", "Phase9"]:
        if topic_previously_discussed and trigger_to_use and release_signal:
            reason = None

            if comparison_intent:
                reason = "comparison_intent"
            elif trust_or_risk_doubt:
                reason = "trust_or_risk_doubt"
            elif objection_signal:
                reason = objection_signal.lower()

            return {
                "store_deferred": False,
                "release_now": True,
                "deferred_trigger": trigger_to_use,
                "release_reason": reason,
                "suppressed": False,
            }

    return {
        "store_deferred": False,
        "release_now": False,
        "deferred_trigger": trigger_to_use,
        "release_reason": None,
        "suppressed": False,
    }


if __name__ == "__main__":
    result = manage_deferred_video(
        conversation_phase="Phase4",
        service="PPF",
        primary_trigger=None,
        topic_previously_discussed=True,
        comparison_intent=True,
        objection_signal="PRICE_COMPARISON",
        trust_or_risk_doubt=False,
        video_already_shown=False,
        silence_active=False,
        silence_suppressed=False,
        existing_deferred_trigger="PPF_SELF_HEAL_QUESTION",
    )
    print(result)
