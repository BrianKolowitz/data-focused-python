"""Build lecture navigation markdown files.

The original version of this helper relied on implicit working-directory changes and
produced several syntax warnings on Python 3.12 due to invalid escape sequences. This
rewrite leans on ``pathlib`` for clarity and keeps string handling explicit.
"""

from pathlib import Path
from urllib.parse import quote

REPO_ROOT = Path(__file__).resolve().parent.parent
LECTURE_ROOT = REPO_ROOT / "lectures"
IPYNB_ROOT = "https://github.com/BrianKolowitz/data-focused-python/blob/master/lectures"


def _write_week_index(week_dir: Path, nav_order: int, lecture_toc_title: str) -> None:
    week_header = [
        "---",
        "layout: default",
        f"title: {week_dir.name}",
        f"parent: {lecture_toc_title}",
        "has_children: true",
        f"nav_order: {nav_order}",
        "---",
        "",
    ]
    week_index_path = week_dir.with_suffix(".md")
    week_index_path.write_text("\n".join(week_header), encoding="utf-8")


def _prepend_front_matter(target: Path, header: list[str]) -> None:
    content = target.read_text(encoding="utf-8")
    if content.startswith("---\n"):
        return
    body = content.splitlines()
    new_text = "\n".join(["\n".join(header)] + body)
    target.write_text(new_text, encoding="utf-8")


def main() -> None:
    lecture_toc_title = "Lectures"
    lecture_toc_md = [
        "---",
        "layout: default",
        f"title: {lecture_toc_title}",
        "nav_order: 3",
        "has_children: true",
        "has_toc: false",
        "permalink: /lectures",
        "---",
    ]

    week_nav_order = 1
    for week_dir in sorted(
        path
        for path in LECTURE_ROOT.iterdir()
        if path.is_dir() and path.name.lower().startswith("week")
    ):
        lecture_toc_md.append("")
        lecture_toc_md.append(f"## {week_dir.name}")
        lecture_toc_md.append("")
        _write_week_index(week_dir, week_nav_order, lecture_toc_title)
        week_nav_order += 1

        file_nav_order = 1
        for lecture_md in sorted(week_dir.glob("*.md")):
            relative_md = lecture_md.relative_to(LECTURE_ROOT)
            ipynb_route = quote(str(relative_md.with_suffix(".ipynb")))
            lecture_ipynb_path = f"{IPYNB_ROOT}/{ipynb_route}"
            lecture_toc_md.append(
                f"* [{lecture_md.stem.title()}]({relative_md.as_posix()}) "
                f"([ipynb]({lecture_ipynb_path}))"
            )

            header = [
                "---",
                "layout: default",
                f"title: {lecture_md.stem}",
                f"parent: {week_dir.name}",
                f"grand_parent: {lecture_toc_title}",
                f"nav_order: {file_nav_order}",
                "---",
                "",
            ]
            _prepend_front_matter(lecture_md, header)
            file_nav_order += 1

    (LECTURE_ROOT / "lectures.md").write_text("\n".join(lecture_toc_md), encoding="utf-8")


if __name__ == "__main__":
    main()
