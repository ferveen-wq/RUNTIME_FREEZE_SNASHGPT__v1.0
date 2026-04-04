from __future__ import annotations

from video_followup_selector import select_video_followup
from visual_education_engine import find_visual


def attach_visual(
    message: str,
    service: str,
    conversation_phase: str,
    primary_trigger: str | None = None,
    qualification_ready: bool = False,
    phase3a_required: bool = False,
    phase3a_qualifier_id: str | None = None,
    video_already_shown: bool = False,
    language: str | None = None,
    category: str | None = None,
) -> dict:
    followup = select_video_followup(
        service=service,
        conversation_phase=conversation_phase,
        primary_trigger=primary_trigger,
        qualification_ready=qualification_ready,
        phase3a_required=phase3a_required,
        phase3a_qualifier_id=phase3a_qualifier_id,
        video_already_shown=video_already_shown,
    )

    if not followup["show_video_now"]:
        return {
            "message": message,
            "video": None,
            "followup": followup,
        }

    visual = find_visual(
        service_name=service,
        primary_trigger=primary_trigger,
        phase=conversation_phase,
        language=language,
        category=category,
    )

    if not visual:
        return {
            "message": message,
            "video": None,
            "followup": followup,
        }

    visual_block = f"""

Visual:
{visual['video_name']}
{visual['link']}
"""

    return {
        "message": message + visual_block,
        "video": visual,
        "followup": followup,
    }


if __name__ == "__main__":
    result = attach_visual(
        message="Many high quality PPF films can recover from light scratches with heat.",
        service="PPF",
        conversation_phase="Phase7",
        primary_trigger="PPF_SELF_HEAL_QUESTION",
        qualification_ready=False,
        phase3a_required=True,
        phase3a_qualifier_id="PHASE3A_Q_PPF_DRIVING_PATTERN",
        video_already_shown=False,
        language="EN",
    )
    print(result)
