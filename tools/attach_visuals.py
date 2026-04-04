from __future__ import annotations

from visual_education_engine import find_visual


def attach_visual(
    message: str,
    service: str,
    primary_trigger: str | None = None,
    phase: str | None = None,
    language: str | None = None,
    category: str | None = None,
) -> str:
    visual = find_visual(
        service_name=service,
        primary_trigger=primary_trigger,
        phase=phase,
        language=language,
        category=category,
    )

    if not visual:
        return message

    visual_block = f"""

Visual:
{visual['video_name']}
{visual['link']}
"""

    return message + visual_block


if __name__ == "__main__":
    test_message = "Many high quality PPF films can recover from light scratches with heat."
    result = attach_visual(
        message=test_message,
        service="PPF",
        primary_trigger="PPF_SELF_HEAL_QUESTION",
        phase="Phase7",
        language="EN",
    )
    print(result)
