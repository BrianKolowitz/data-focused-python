---
layout: default
title: 08 - Working with Word Documents
parent: Topic 05 - Processing files
grand_parent: Lectures
nav_order: 10
---
# Working with Word Documents
[Source](https://www.datacamp.com/community/tutorials/reading-and-editing-pdfs-and-word-documents-from-python)

The Word documents consist of the ".docx" extension at the end of the filename. These documents don't only contain text as in plain text files, but it includes a rich-text document. The rich-text document contains the different structures for the document, which have size, align, color, pictures, font, etc. associated with them.

It would be best if you had an application for working with the Word Documents. The popular application for Windows and Mac Operating systems is Microsoft Word, but it is a paid subscription platform. However, there is a free alternative option like "LibreOffice", which is an application in Linux which comes pre-installed. The applications can be downloaded for Windows and Mac Operating systems.

## Steps to Install-Package:

You need to install a package named `python-docx` which can handle the word documents of the '.docx' extension. 

```python
pip install python-docx
```

## Writing a Word Documents


```python
from docx import Document
document = Document()
document.save('first.docx')
```

### Add a heading


```python
from docx import Document
document = Document()
document.add_heading('This is the largest heading', level=0)
document.add_heading('This is header 1 as a main heading', level=1)
document.add_heading('This is header 2', level=2)
document.add_heading('This is header 3', level=3)
document.add_heading('This is header 4', level=4)
document.save('heading-example.docx')
```

### Add a Paragraph


```python
from docx import Document
document = Document()
document.add_paragraph('This is a simple paragraph')

document.add_heading('Things to Do', level=2)
document.add_paragraph('eat', style='List Number')
document.add_paragraph('sleep', style='List Number')
document.add_paragraph('repeat', style='List Number')

document.add_heading('Things Not to Do', level=2)
document.add_paragraph('forget to study', style='List Bullet')
document.add_paragraph('forget to do assignments', style='List Bullet')

document.save('paragraph-example.docx')
```

### Add a Picture


```python
from docx import Document
from docx.shared import Inches
document = Document()
document.add_picture('python.png', width=Inches(2.5), height=(2.5))
document.save('picture.example.docx')
```

## Reading a Word Documents

You'll now read a sample word document from Python, and it can be found [here](https://docs.google.com/document/d/13oX775JlQRweV02ZpY0_N35eC0CcWkE0fHK4CHaBLLc/edit?usp=sharing)


```python
from docx import Document
```


```python
def obtainText(docFileName):
    document = Document(docFileName)
    finalText = []
    for line in document.paragraphs:
        finalText.append(line.text)
    return '\n'.join(finalText)
```


```python
print(obtainText('fullText.docx'))
```

    This is Heading1 Text
    This is a regular paragraph with the default style of Normal. This is a regular paragraph with the default style of Normal. This is a regular paragraph with the default style of Normal. This is a regular paragraph with the default style of Normal. This is a regular paragraph with the default style of Normal.
    This is a Defined Block Style Called BlockStyleTest
    This is more Normal text.
    This is Heading 2 text
    This is more Normal text. This is bold, this is italic, and this is bold italic. This is normal. This is in a defined inline style called InlineStyle. This is normal. This is red text. This is normal.
    This block is centered.
    This is left-aligned.
     
    First item of bulleted list.
    Second item of bulleted list.
    Second paragraph of second item of bulleted list.
    Third item of bulleted list.
    First item of third item’s nested list
    Second item of third item’s nested list
    Fourth and final item of main bulleted list.
     
    



```python

```
