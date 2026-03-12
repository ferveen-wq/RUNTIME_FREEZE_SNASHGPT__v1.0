import re

VISUAL_PLAYBOOK = "00__LOCKED__UPLOAD_SET/00__Runtime/VISUAL_PLAYBOOK.md"


def find_visual(service_name):

    visuals = {
        "ppf": "https://snash.example/video/ppf_demo",
        "ceramic": "https://snash.example/video/ceramic_demo",
        "tint": "https://snash.example/video/window_tint_demo"
    }

    s = service_name.lower()

    for key in visuals:
        if re.search(key, s):
            return visuals[key]

    return None


if __name__ == "__main__":

    test = "ppf protection"

    visual = find_visual(test)

    if visual:
        print("Visual found:", visual)
    else:
        print("No visual available")
