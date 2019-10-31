import glob, os
import sys
import urllib
from pathlib import Path

if __name__ == "__main__":
    os.chdir(os.path.dirname(sys.argv[0]))

    lecture_toc_md = []
    lecture_root = "../lectures"
    weeks = [week for week in os.listdir(lecture_root) if week.lower().startswith('week') and not week.lower().endswith('.md')]
    weeks.sort()
    lecture_toc_title = "Lectures"
    lecture_toc_md.append("---")
    lecture_toc_md.append("layout: default")
    lecture_toc_md.append(f"title: {lecture_toc_title}")
    lecture_toc_md.append("nav_order: 3")
    lecture_toc_md.append("has_children: true")
    lecture_toc_md.append("has_toc: false")
    lecture_toc_md.append("permalink: /lectures")
    lecture_toc_md.append("---")
    # lecture_toc_md.append("")
    
    week_nav_order = 1
    # todo : delete all md files
    for week_title in weeks:
        week_path = os.path.join(lecture_root, week_title)
        lecture_toc_md.append("")
        lecture_toc_md.append(f"## {week_title}")
        lecture_toc_md.append("")
        with open(week_path + '.md', 'w') as week_file:
            week_md = [
                f"---",
                f"layout: default",
                f"title: {week_title}",
                f"parent: {lecture_toc_title}",
                f"has_children: true",
                f"nav_order: {week_nav_order}",
                f"---",
                f"",
            ]
            week_file.write('\n'.join(week_md))
            week_nav_order += 1
        
        files = os.listdir(week_path)
        files = [file for file in files if file.endswith('.md')]
        files.sort()
        file_nav_order = 1
        for file in files:
            lecture_md_path = os.path.join(week_title, file)
            
            # todo : figure out why this broke
            ipynb_root = "https://github.com/BrianKolowitz/data-focused-python/blob/master/lectures"
            ipynb_route = os.path.join(week_title, file[:-3] + ".ipynb")
            ipynb_route = urllib.parse.quote(ipynb_route)
            lecture_ipynb_path = os.path.join(ipynb_root, ipynb_route)
            # lecture_ipynb_path = os.path.join(week_path, file[:-3] + ".ipynb")
            # lecture_md_path = urllib.parse.quote(md_path)
            # lecture_ipynb_path = urllib.parse.quote(lecture_ipynb_path)
            lecture_toc_md.append(f"* [{Path(file).resolve().stem.title()}]({lecture_md_path}) \([ipynb]({lecture_ipynb_path})\)")

            with open(os.path.join(lecture_root, lecture_md_path), 'r+') as lecture_md_file:
                lines = lecture_md_file.readlines()
                header = [
                    f"---", 
                    f"layout: default",
                    f"title: {file[:-3]}",
                    f"parent: {week_title}",
                    f"grand_parent: {lecture_toc_title}",
                    f"nav_order: {file_nav_order}",
                    f"---",
                    f""
                ]
                file_nav_order += 1
                lines.insert(0, '\n'.join(header))
                lecture_md_file.seek(0)
                lecture_md_file.writelines(lines)

    with open(os.path.join(lecture_root, 'lectures.md'), 'w') as f:
        f.write('\n'.join(lecture_toc_md))
