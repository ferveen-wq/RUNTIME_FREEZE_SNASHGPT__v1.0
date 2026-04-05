from __future__ import annotations

import re
from pathlib import Path

from visual_selector import select_best_visual

VIDEO_INDEX_PATH = Path("00__CONTROL_TOWER/VIDEO_LIBRARY_INDEX.md")


def _norm(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", "", (value or "").lower())


def _extract_field(block: str, field: str) -> str:
    pattern = rf"^{re.escape(field)}:\s*\n(.+?)(?:\n\s*\n|\n[A-Z_ ]+:\s*\n|\Z)"
    match = re.search(pattern, block, flags=re.MULTILINE | re.DOTALL)
    if not match:
        return ""
    return match.group(1).strip()


def _parse_video_index(path: Path = VIDEO_INDEX_PATH) -> list[dict[str, str]]:
    if not path.exists():
        return []

    text = path.read_text(encoding="utf-8")
    blocks = re.split(r"\n---\n+", text)

    videos: list[dict[str, str]] = []
    for block in blocks:
        if "VIDEO_ID:" not in block or "VIDEO_NAME:" not in block:
            continue

        item = {
            "video_id": _extract_field(block, "VIDEO_ID"),
            "video_name": _extract_field(block, "VIDEO_NAME"),
            "service": _extract_field(block, "SERVICE"),
            "primary_trigger": _extract_field(block, "PRIMARY_TRIGGER"),
            "phase_default": _extract_field(block, "PHASE_DEFAULT"),
            "secondary_phase": _extract_field(block, "SECONDARY_PHASE"),
            "category": _extract_field(block, "CATEGORY"),
            "language": _extract_field(block, "LANGUAGE"),
            "link": _extract_field(block, "LINK"),
            "status": _extract_field(block, "STATUS"),
            "notes": _extract_field(block, "NOTES"),
        }

        if item["link"] and item["status"].upper() == "APPROVED":
            videos.append(item)

    return videos


def find_visual_candidates(
    service_name: str,
    primary_trigger: str | None = None,
    phase: str | None = None,
    language: str | None = None,
    category: str | None = None,
) -> list[dict[str, str]]:
    videos = _parse_video_index()
    if not videos:
        return []

    svc = _norm(service_name)
    trig = _norm(primary_trigger or "")
    ph = _norm(phase or "")
    lang = _norm(language or "")
    cat = _norm(category or "")

    candidates: list[dict[str, str]] = []

    for video in videos:
        video_service = _norm(video["service"])
        video_trigger = _norm(video["primary_trigger"])
        video_phase_default = _norm(video["phase_default"])
        video_phase_secondary = _norm(video["secondary_phase"])
        video_language = _norm(video["language"])
        video_category = _norm(video["category"])

        service_ok = (
            not svc
            or video_service == svc
            or video_service == "multi"
            or (svc == "polish" and video_service == "polishing")
            or (svc == "polishing" and video_service == "polish")
        )
        if not service_ok:
            continue

        if trig and video_trigger != trig:
            continue

        if ph and ph not in {video_phase_default, video_phase_secondary}:
            continue

        if lang and video_language != lang:
            continue

        if cat and video_category != cat:
            continue

        candidates.append(video)

    if not candidates and trig:
        for video in videos:
            video_service = _norm(video["service"])
            video_trigger = _norm(video["primary_trigger"])
            if video_trigger != trig:
                continue
            if not (
                video_service == svc
                or video_service == "multi"
                or (svc == "polish" and video_service == "polishing")
                or (svc == "polishing" and video_service == "polish")
            ):
                continue
            candidates.append(video)

    if not candidates:
        for video in videos:
            video_service = _norm(video["service"])
            if video_service in {svc, "multi"}:
                candidates.append(video)

    return candidates


def find_visual(
    service_name: str,
    primary_trigger: str | None = None,
    phase: str | None = None,
    language: str | None = None,
    category: str | None = None,
) -> dict[str, str] | None:
    candidates = find_visual_candidates(
        service_name=service_name,
        primary_trigger=primary_trigger,
        phase=phase,
        language=language,
        category=category,
    )
    return select_best_visual(candidates)


if __name__ == "__main__":
    result = find_visual(
        service_name="PPF",
        primary_trigger="PPF_SELF_HEAL_QUESTION",
        phase="Phase7",
        language="EN",
    )
    print(result)
