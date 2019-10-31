import glob, os
import sys
import urllib
import shutil
from pathlib import Path

def build_lectures_md(lectures_md_file_name):
    weekly_lectures = []
    lectures_path = '../lectures'
    weekly_lectures = [lecture for lecture in os.listdir(lectures_path) \
        if lecture.startswith('Week') and not lecture.endswith('.md')]
    weekly_lectures.sort()

    lectures_md = []
    lectures_md.append("## Lectures\n")
    lectures_md.append("\n")
    lectures_md.append("Lectures will contain a mixture of content form this site and others.\n")
    lectures_md.append("\n")
    for lecture in weekly_lectures:
        print('***** ', lecture)
        (week, content) = tuple(lecture.split(' - '))
        lectures_md.append(f'1. [{week}](lectures/lectures.md) - {content}\n')
    with open(lectures_md_file_name, 'w+') as f:
        f.write(''.join(lectures_md))    


if __name__ == "__main__":
    os.chdir(os.path.dirname(sys.argv[0]))

    md = []

    title = "Data Focused Python"
    md.append("---\n")
    md.append("layout: default\n")
    md.append(f"title: {title}\n")
    md.append("nav_order: 1\n")
    md.append("permalink: /\n")
    md.append("---\n")
    md.append("\n")

    lectures_md_file_name = '02-lectures.md'
    build_lectures_md(lectures_md_file_name)

    files = [
        '01-data-focused-python.md',
        lectures_md_file_name,
        '03-quizzes.md',
        '04-assignments.md'
    ]
    for file in files:
        with open(file, 'r') as f:
            md.extend(f.readlines())
            md.append("\n")
    
    with open('../README.md', 'w+') as f:
        f.write(''.join(md))    
