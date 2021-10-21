import glob, os
import sys
import urllib
from pathlib import Path

if __name__ == "__main__":
    os.chdir(os.path.dirname(sys.argv[0]))

    lecture_toc_md = []
    lecture_root = "../lectures"
    topics = [topic for topic in os.listdir(lecture_root) if topic.lower().startswith('topic') and not topic.lower().endswith('.md')]
    topics.sort()
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
    
    topic_nav_order = 1
    # todo : delete all md files
    for topic_title in topics:
        topic_path = os.path.join(lecture_root, topic_title)
        lecture_toc_md.append("")
        lecture_toc_md.append(f"## {topic_title}")
        lecture_toc_md.append("")
        with open(topic_path + '.md', 'w') as topic_file:
            topic_md = [
                f"---",
                f"layout: default",
                f"title: {topic_title}",
                f"parent: {lecture_toc_title}",
                f"has_children: true",
                f"nav_order: {topic_nav_order}",
                f"---",
                f"",
            ]
            topic_file.write('\n'.join(topic_md))
            topic_nav_order += 1
        
        files = os.listdir(topic_path)
        files = [file for file in files if file.endswith('.md')]
        files.sort()
        file_nav_order = 1
        for file in files:
            lecture_md_path = os.path.join(topic_title, file)
            
            # todo : figure out why this broke
            ipynb_root = "https://github.com/BrianKolowitz/data-focused-python/blob/master/lectures"
            ipynb_route = os.path.join(topic_title, file[:-3] + ".ipynb")
            ipynb_route = urllib.parse.quote(ipynb_route)
            lecture_ipynb_path = os.path.join(ipynb_root, ipynb_route)
            # lecture_ipynb_path = os.path.join(topic_path, file[:-3] + ".ipynb")
            # lecture_md_path = urllib.parse.quote(md_path)
            # lecture_ipynb_path = urllib.parse.quote(lecture_ipynb_path)
            lecture_toc_md.append(f"* [{Path(file).resolve().stem.title()}]({lecture_md_path}) \([ipynb]({lecture_ipynb_path})\)")

            with open(os.path.join(lecture_root, lecture_md_path), 'r+') as lecture_md_file:
                lines = lecture_md_file.readlines()
                header = [
                    f"---", 
                    f"layout: default",
                    f"title: {file[:-3]}",
                    f"parent: {topic_title}",
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
