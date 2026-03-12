from tools.visual_education_engine import find_visual


def attach_visual(service, message):

    visual = find_visual(service)

    if not visual:
        return message

    visual_block = f"""

🎬 Visual demonstration:
{visual}
"""

    return message + visual_block


if __name__ == "__main__":

    test_message = "PPF protects your paint from stone chips."

    result = attach_visual("ppf", test_message)

    print(result)
