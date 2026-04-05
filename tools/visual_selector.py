from __future__ import annotations

PRIORITY_BY_CATEGORY = {
    "PROOF": 1,
    "INSTALL": 2,
    "RESULT": 3,
    "TESTIMONIAL": 4,
    "TRUST": 5,
}


def select_best_visual(candidates: list[dict]) -> dict | None:
    """
    Select the best visual from candidates based on priority.

    Lower number = higher priority.
    """

    if not candidates:
        return None

    def score(video: dict) -> int:
        category = video.get("category", "TRUST")
        return PRIORITY_BY_CATEGORY.get(category, 999)

    sorted_videos = sorted(candidates, key=score)
    return sorted_videos[0]


if __name__ == "__main__":
    sample = [
        {"video_id": "1", "category": "TESTIMONIAL"},
        {"video_id": "2", "category": "PROOF"},
        {"video_id": "3", "category": "RESULT"},
    ]

    print(select_best_visual(sample))
