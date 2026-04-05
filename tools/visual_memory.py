from __future__ import annotations


def update_visual_memory(
    current_video_id: str | None,
    visuals_already_shown: list[str] | None = None,
) -> dict:
    """
    Track shown videos and prevent exact repetition.

    This is a non-customer-facing helper.
    It does NOT choose videos.
    It only records whether a video was already shown.
    """

    memory = list(visuals_already_shown or [])

    if not current_video_id:
        return {
            "video_already_shown": False,
            "visuals_already_shown": memory,
        }

    if current_video_id in memory:
        return {
            "video_already_shown": True,
            "visuals_already_shown": memory,
        }

    memory.append(current_video_id)

    return {
        "video_already_shown": False,
        "visuals_already_shown": memory,
    }


if __name__ == "__main__":
    state_1 = update_visual_memory("VID_001", [])
    print(state_1)

    state_2 = update_visual_memory("VID_001", state_1["visuals_already_shown"])
    print(state_2)
