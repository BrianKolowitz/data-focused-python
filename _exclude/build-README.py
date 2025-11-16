"""Utility helpers for regenerating the README from lecture fragments."""

from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent
LECTURES_PATH = REPO_ROOT.parent / "lectures"


def build_lectures_md(target: Path) -> None:
    """Write the lecture overview page."""

    weekly_lectures = sorted(
        lecture
        for lecture in LECTURES_PATH.iterdir()
        if lecture.name.startswith("Week") and lecture.is_dir()
    )

    lines = [
        "## Lectures\n",
        "\n",
        "Lectures will contain a mixture of content form this site and others.\n",
        "\n",
    ]
    for lecture in weekly_lectures:
        week, content = lecture.name.split(" - ", maxsplit=1)
        lines.append(f"1. [{week}](lectures/lectures.md) - {content}\n")
    target.write_text("".join(lines), encoding="utf-8")


def main() -> None:
    lectures_md_path = REPO_ROOT / "02-lectures.md"
    build_lectures_md(lectures_md_path)

    title = "Data Focused Python"
    md = [
        "---\n",
        "layout: default\n",
        f"title: {title}\n",
        "nav_order: 1\n",
        "permalink: /\n",
        "---\n",
        "\n",
    ]

    files = [
        REPO_ROOT / "01-data-focused-python.md",
        lectures_md_path,
        REPO_ROOT / "03-quizzes.md",
        REPO_ROOT / "04-assignments.md",
    ]
    for file in files:
        md.append(file.read_text(encoding="utf-8"))
        md.append("\n")

    (REPO_ROOT.parent / "README.md").write_text("".join(md), encoding="utf-8")


if __name__ == "__main__":
    main()
