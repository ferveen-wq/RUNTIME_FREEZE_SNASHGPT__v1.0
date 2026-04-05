from __future__ import annotations

from deferred_video_manager import manage_deferred_video
from phrase_resolver import resolve_phrase
from video_followup_selector import select_video_followup
from visual_education_engine import find_visual
from visual_memory import update_visual_memory


def attach_visual(
    message: str,
    service: str,
    conversation_phase: str,
    primary_trigger: str | None = None,
    qualification_ready: bool = False,
    phase3a_required: bool = False,
    phase3a_qualifier_id: str | None = None,
    video_already_shown: bool = False,
    topic_previously_discussed: bool = False,
    comparison_intent: bool = False,
    objection_signal: str | None = None,
    trust_or_risk_doubt: bool = False,
    silence_active: bool = False,
    silence_suppressed: bool = False,
    existing_deferred_trigger: str | None = None,
    visuals_already_shown: list[str] | None = None,
    language: str | None = None,
    category: str | None = None,
) -> dict:
    deferred = manage_deferred_video(
        conversation_phase=conversation_phase,
        service=service,
        primary_trigger=primary_trigger,
        topic_previously_discussed=topic_previously_discussed,
        comparison_intent=comparison_intent,
        objection_signal=objection_signal,
        trust_or_risk_doubt=trust_or_risk_doubt,
        video_already_shown=video_already_shown,
        silence_active=silence_active,
        silence_suppressed=silence_suppressed,
        existing_deferred_trigger=existing_deferred_trigger,
    )

    trigger_to_use = None
    force_video_display = False

    if deferred["release_now"]:
        trigger_to_use = deferred["deferred_trigger"]
        force_video_display = True
    elif deferred["store_deferred"]:
        return {
            "message": message,
            "video": None,
            "followup": None,
            "followup_text": None,
            "deferred_state": deferred,
            "visual_memory": update_visual_memory(
                None, visuals_already_shown
            ),
        }
    else:
        trigger_to_use = primary_trigger

    followup = select_video_followup(
        service=service,
        conversation_phase=conversation_phase,
        primary_trigger=trigger_to_use,
        qualification_ready=qualification_ready,
        phase3a_required=phase3a_required,
        phase3a_qualifier_id=phase3a_qualifier_id,
        video_already_shown=video_already_shown,
    )

    visual = None
    if force_video_display or followup["show_video_now"]:
        visual = find_visual(
            service_name=service,
            primary_trigger=trigger_to_use,
            phase=conversation_phase,
            language=language,
            category=category,
        )

    followup_text = None
    if (
        followup["next_question_source"] == "phase3a"
        and followup["next_question_id"]
    ):
        followup_text = resolve_phrase(
            followup["next_question_id"], language or "EN"
        )

    current_video_id = visual["video_id"] if visual else None
    visual_memory = update_visual_memory(
        current_video_id, visuals_already_shown
    )

    if visual_memory["video_already_shown"]:
        return {
            "message": message,
            "video": None,
            "followup": followup,
            "followup_text": followup_text,
            "deferred_state": deferred,
            "visual_memory": visual_memory,
        }

    if not visual:
        return {
            "message": message,
            "video": None,
            "followup": followup,
            "followup_text": followup_text,
            "deferred_state": deferred,
            "visual_memory": visual_memory,
        }

    visual_block = f"""

Visual:
{visual['video_name']}
{visual['link']}
"""

    final_message = message + visual_block

    if followup_text:
        final_message += f"\n{followup_text}"

    return {
        "message": final_message,
        "video": visual,
        "followup": followup,
        "followup_text": followup_text,
        "deferred_state": deferred,
        "visual_memory": visual_memory,
    }


if __name__ == "__main__":
    state_1 = attach_visual(
        message="PPF can self-heal light scratches with heat.",
        service="PPF",
        conversation_phase="Phase4",
        primary_trigger="PPF_SELF_HEAL_QUESTION",
        topic_previously_discussed=True,
        comparison_intent=True,
        language="EN",
        visuals_already_shown=[],
    )
    print(state_1)

    state_2 = attach_visual(
        message="PPF can self-heal light scratches with heat.",
        service="PPF",
        conversation_phase="Phase4",
        primary_trigger="PPF_SELF_HEAL_QUESTION",
        topic_previously_discussed=True,
        comparison_intent=True,
        language="EN",
        visuals_already_shown=state_1["visual_memory"]["visuals_already_shown"],
    )
    print(state_2)
