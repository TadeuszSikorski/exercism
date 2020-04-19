def check_scores(scores: list):
    if scores == []:
        raise Exception("List of scores is empty.")


def latest(scores: list) -> int:
    check_scores(scores)

    return scores[-1]


def personal_best(scores: list) -> int:
    check_scores(scores)

    return max(scores)


def personal_top_three(scores: list) -> list:
    check_scores(scores)

    scores.sort(reverse=True)

    return scores[:3]
