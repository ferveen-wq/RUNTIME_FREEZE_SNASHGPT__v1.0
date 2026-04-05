from __future__ import annotations

PRIORITY_BY_CATEGORY = {
    "PROOF": 10,
    "INSTALL": 20,
    "RESULT": 30,
    "TESTIMONIAL": 40,
    "TRUST": 50,
}

PHASE_BONUS = {
    "Phase7": {"PROOF": -15},
    "Phase8": {"RESULT": -25, "INSTALL": -20},
    "Phase9": {"TESTIMONIAL": -35, "TRUST": -30},
}


def select_best_visual(
    candidates: list[dict],
    conversation_phase: str | None = None,
) -> dict | None:
    if not candidates:
        return None

    def score(video: dict) -> int:
        category = video.get("category", "TRUST")
        base = PRIORITY_BY_CATEGORY.get(category, 999)

        bonus = 0
        if conversation_phase:
            phase_rules = PHASE_BONUS.get(conversation_phase, {})
            bonus = phase_rules.get(category, 0)

        return base + bonus

    sorted_videos = sorted(candidates, key=score)
    return sorted_videos[0]


if __name__ == "__main__":
    sample = [
        {"video_id": "1", "category": "TESTIMONIAL"},
        {"video_id": "2", "category": "PROOF"},
        {"video_id": "3", "category": "RESULT"},
        {"video_id": "4", "category": "TRUST"},
        {"video_id": "5", "category": "INSTALL"},
    ]

    print(select_best_visual(sample, "Phase7"))
    print(select_best_visual(sample, "Phase8"))
    print(select_best_visual(sample, "Phase9"))
