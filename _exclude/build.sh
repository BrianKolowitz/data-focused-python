jupyter nbconvert --to markdown lectures/**/*.ipynb
python _exclude/build-lecture-toc.py
python _exclude/build-README.py
bundle exec just-the-docs rake search:init