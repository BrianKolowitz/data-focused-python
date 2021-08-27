jupyter nbconvert --to markdown lectures/**/*.ipynb
python3 _exclude/build-lecture-toc.py
python3 _exclude/build-README.py
bundle exec just-the-docs rake search:init