from __future__ import annotations


def select_video_followup(
    service: str,
    conversation_phase: str,
    primary_trigger: str | None = None,
    qualification_ready: bool = False,
    phase3a_required: bool = False,
    phase3a_qualifier_id: str | None = None,
    video_already_shown: bool = False,
) -> dict:
    """
    Decide what to do AFTER a video is attached.

    This function does NOT generate any customer-facing text.
    It only returns structured decisions for downstream engines.
    """

    if video_already_shown:
        return {
            "show_video_now": False,
            "defer_video": False,
            "next_question_source": "none",
            "next_question_id": None,
            "hook_mode": "suppress",
        }

    if conversation_phase in ["Phase0", "Phase1", "Phase2"]:
        return {
            "show_video_now": False,
            "defer_video": False,
            "next_question_source": "none",
            "next_question_id": None,
            "hook_mode": "suppress",
        }

    if (not qualification_ready) and phase3a_required:
        if phase3a_qualifier_id:
            return {
                "show_video_now": True,
                "defer_video": False,
                "next_question_source": "phase3a",
                "next_question_id": phase3a_qualifier_id,
                "hook_mode": "qualification_bridge",
            }

        return {
            "show_video_now": True,
            "defer_video": False,
            "next_question_source": "none",
            "next_question_id": None,
            "hook_mode": "suppress",
        }

    if qualification_ready:
        return {
            "show_video_now": True,
            "defer_video": False,
            "next_question_source": "none",
            "next_question_id": None,
            "hook_mode": "suppress",
        }

    return {
        "show_video_now": False,
        "defer_video": False,
        "next_question_source": "none",
        "next_question_id": None,
        "hook_mode": "suppress",
    }


if __name__ == "__main__":
    result = select_video_followup(
        service="PPF",
        conversation_phase="Phase4",
        primary_trigger="PPF_SELF_HEAL_QUESTION",
        qualification_ready=False,
        phase3a_required=True,
        phase3a_qualifier_id="PHASE3A_Q_PPF_DRIVING_PATTERN",
        video_already_shown=False,
    )
    print(result)
