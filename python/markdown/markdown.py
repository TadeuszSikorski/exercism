import re


def get_headings(markdown: str) -> str:
    for number in range(1, 7):
        markdown = re.sub(
            r"^{} (.*?$)".format("#" * number),
            r"<h{0}>\1</h{0}>".format(number),
            markdown,
            flags=re.M,
        )

    return markdown


def get_important_texts(markdown: str) -> str:
    return re.sub(r"__(.*)__", r"<strong>\1</strong>", markdown)


def get_emphasized_texts(markdown: str) -> str:
    return re.sub(r"_(.*)_", r"<em>\1</em>", markdown)


def get_ordered_lists(markdown: str) -> str:
    return re.sub(r"^\* (.*)", r"<li>\1</li>", markdown, flags=re.M)


def get_unordered_lists(markdown: str) -> str:
    return re.sub(r"(\n?<li>.*</li>)", r"<ul>\1</ul>", markdown, flags=re.S)


def get_paragraphs(markdown: str) -> str:
    return re.sub(r"^(?!<[hlu])(.*?$)", r"<p>\1</p>", markdown, flags=re.M)


def delete_new_line(markdown: str) -> str:
    return re.sub(r"\n", "", markdown)


def parse(markdown):
    markdown = get_important_texts(markdown)

    markdown = get_emphasized_texts(markdown)

    markdown = get_ordered_lists(markdown)

    markdown = get_headings(markdown)

    markdown = get_unordered_lists(markdown)

    markdown = get_paragraphs(markdown)

    markdown = delete_new_line(markdown)

    return markdown
