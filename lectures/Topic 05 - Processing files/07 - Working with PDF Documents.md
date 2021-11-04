---
layout: default
title: 07 - Working with PDF Documents
parent: Topic 05 - Processing files
grand_parent: Lectures
nav_order: 9
---
# Working with PDF Documents
[Source](https://automatetheboringstuff.com/2e/chapter15/)

## PDF Documents

PDF stands for Portable Document Format and uses the .pdf file extension. Although PDFs support many features, this chapter will focus on the two things you’ll be doing most often with them: reading text content from PDFs and crafting new PDFs from existing documents.

The module you’ll use to work with PDFs is PyPDF2 version 1.26.0. It’s important that you install this version because future versions of PyPDF2 may be incompatible with the code. To install it, run `pip install --user PyPDF2` from the command line. This module name is case sensitive, so make sure the y is lowercase and everything else is uppercase. (Check out Appendix A for full details about installing third-party modules.) If the module was installed correctly, running import PyPDF2 in the interactive shell shouldn’t display any errors.

> THE PROBLEMATIC PDF FORMAT
> While PDF files are great for laying out text in a way that’s easy for people to print and read, they’re not straightforward for software to parse into plaintext. As a result, PyPDF2 might make mistakes when extracting text from a PDF and may even be unable to open some PDFs at all. There isn’t much you can do about this, unfortunately. PyPDF2 may simply be unable to work with some of your particular PDF files. That said, I haven’t found any PDF files so far that can’t be opened with PyPDF2.

## Extracting Text from PDFs

PyPDF2 does not have a way to extract images, charts, or other media from PDF documents, but it can extract text and return it as a Python string. To start learning how PyPDF2 works, we’ll use it on the example PDF shown in Figure 15-1.
image


```python
import PyPDF2
pdfFileObj = open('../automate_online-materials/meetingminutes.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
pdfReader.numPages
```




    19




```python
pageObj = pdfReader.getPage(0)
pageObj.extractText()
```




    'OOFFFFIICCIIAALL  BBOOAARRDD  MMIINNUUTTEESS   Meeting of \nMarch 7\n, 2014\n        \n     The Board of Elementary and Secondary Education shall provide leadership and \ncreate policies for education that expand opportunities for children, empower \nfamilies and communities, and advance Louisiana in an increasingly \ncompetitive glob\nal market.\n BOARD \n of ELEMENTARY\n and \n SECONDARY\n EDUCATION\n  '



Some PDF documents have an encryption feature that will keep them from being read until whoever is opening the document provides a password. Enter the following into the interactive shell with the PDF you downloaded, which has been encrypted with the password rosebud:


```python
import PyPDF2
pdfReader = PyPDF2.PdfFileReader(open('../automate_online-materials/encrypted.pdf', 'rb'))
pdfReader.isEncrypted
```




    True




```python
pdfReader.getPage(0)
```


    ---------------------------------------------------------------------------

    PdfReadError                              Traceback (most recent call last)

    /var/folders/jd/pq0swyt521jb2424d6fvth840000gn/T/ipykernel_77941/2680691199.py in <module>
    ----> 1 pdfReader.getPage(0)
    

    ~/opt/miniconda3/envs/cmu39/lib/python3.9/site-packages/PyPDF2/pdf.py in getPage(self, pageNumber)
       1174         #assert not self.trailer.has_key("/Encrypt")
       1175         if self.flattenedPages == None:
    -> 1176             self._flatten()
       1177         return self.flattenedPages[pageNumber]
       1178 


    ~/opt/miniconda3/envs/cmu39/lib/python3.9/site-packages/PyPDF2/pdf.py in _flatten(self, pages, inherit, indirectRef)
       1503         if pages == None:
       1504             self.flattenedPages = []
    -> 1505             catalog = self.trailer["/Root"].getObject()
       1506             pages = catalog["/Pages"].getObject()
       1507 


    ~/opt/miniconda3/envs/cmu39/lib/python3.9/site-packages/PyPDF2/generic.py in __getitem__(self, key)
        514 
        515     def __getitem__(self, key):
    --> 516         return dict.__getitem__(self, key).getObject()
        517 
        518     ##


    ~/opt/miniconda3/envs/cmu39/lib/python3.9/site-packages/PyPDF2/generic.py in getObject(self)
        176 
        177     def getObject(self):
    --> 178         return self.pdf.getObject(self).getObject()
        179 
        180     def __repr__(self):


    ~/opt/miniconda3/envs/cmu39/lib/python3.9/site-packages/PyPDF2/pdf.py in getObject(self, indirectReference)
       1615                 # if we don't have the encryption key:
       1616                 if not hasattr(self, '_decryption_key'):
    -> 1617                     raise utils.PdfReadError("file has not been decrypted")
       1618                 # otherwise, decrypt here...
       1619                 import struct


    PdfReadError: file has not been decrypted



```python
pdfReader = PyPDF2.PdfFileReader(open('../automate_online-materials/encrypted.pdf', 'rb'))
pdfReader.decrypt('rosebud')
pageObj = pdfReader.getPage(0)
pageObj.extractText()
```




    'OOFFFFIICCIIAALL  BBOOAARRDD  MMIINNUUTTEESS   Meeting of \nMarch 7\n, 2014\n        \n     The Board of Elementary and Secondary Education shall provide leadership and \ncreate policies for education that expand opportunities for children, empower \nfamilies and communities, and advance Louisiana in an increasingly \ncompetitive glob\nal market.\n BOARD \n of ELEMENTARY\n and \n SECONDARY\n EDUCATION\n  '



>NOTE
>Due to a bug in PyPDF2 version 1.26.0, calling getPage() on an encrypted PDF before calling decrypt() on it causes future getPage() calls to fail with the following error: IndexError: list index out of range. This is why our example reopened the file with a new PdfFileReader object.

## Creating PDFs
PyPDF2’s counterpart to PdfFileReader is PdfFileWriter, which can create new PDF files. But PyPDF2 cannot write arbitrary text to a PDF like Python can do with plaintext files. Instead, PyPDF2’s PDF-writing capabilities are limited to copying pages from other PDFs, rotating pages, overlaying pages, and encrypting files.

PyPDF2 doesn’t allow you to directly edit a PDF. Instead, you have to create a new PDF and then copy content over from an existing document. The examples in this section will follow this general approach:

1. Open one or more existing PDFs (the source PDFs) into PdfFileReader objects.
2. Create a new PdfFileWriter object.
3. Copy pages from the PdfFileReader objects into the PdfFileWriter object.
4. Finally, use the PdfFileWriter object to write the output PDF.

Creating a PdfFileWriter object creates only a value that represents a PDF document in Python. It doesn’t create the actual PDF file. For that, you must call the PdfFileWriter’s write() method.
The write() method takes a regular File object that has been opened in write-binary mode. You can get such a File object by calling Python’s open() function with two arguments: the string of what you want the PDF’s filename to be and 'wb' to indicate the file should be opened in write-binary mode.
If this sounds a little confusing, don’t worry—you’ll see how this works in the following code examples.

## Copying Pages

You can use PyPDF2 to copy pages from one PDF document to another. This allows you to combine multiple PDF files, cut unwanted pages, or reorder pages.


```python
import PyPDF2
pdf1File = open('../automate_online-materials/meetingminutes.pdf', 'rb')
pdf2File = open('../automate_online-materials/meetingminutes2.pdf', 'rb')
pdf1Reader = PyPDF2.PdfFileReader(pdf1File)
pdf2Reader = PyPDF2.PdfFileReader(pdf2File)
pdfWriter = PyPDF2.PdfFileWriter()

for pageNum in range(pdf1Reader.numPages):
    pageObj = pdf1Reader.getPage(pageNum)
    pdfWriter.addPage(pageObj)

for pageNum in range(pdf2Reader.numPages):
    pageObj = pdf2Reader.getPage(pageNum)
    pdfWriter.addPage(pageObj)

pdfOutputFile = open('combinedminutes.pdf', 'wb')
pdfWriter.write(pdfOutputFile)
pdfOutputFile.close()
pdf1File.close()
pdf2File.close()
```

>NOTE
>PyPDF2 cannot insert pages in the middle of a PdfFileWriter object; the addPage() method will only add pages to the end.

## Rotating Pages

The pages of a PDF can also be rotated in 90-degree increments with the rotateClockwise() and rotateCounterClockwise() methods. Pass one of the integers 90, 180, or 270 to these methods. Enter the following into the interactive shell, with the meetingminutes.pdf file in the current working directory:


```python
import PyPDF2
minutesFile = open('../automate_online-materials/meetingminutes.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(minutesFile)
page = pdfReader.getPage(0)
page.rotateClockwise(90)
```


```python
pdfWriter = PyPDF2.PdfFileWriter()
pdfWriter.addPage(page)
resultPdfFile = open('rotatedPage.pdf', 'wb')
pdfWriter.write(resultPdfFile)
resultPdfFile.close()
minutesFile.close()
```

## Overlaying Pages

PyPDF2 can also overlay the contents of one page over another, which is useful for adding a logo, timestamp, or watermark to a page. With Python, it’s easy to add watermarks to multiple files and only to pages your program specifies.


```python
import PyPDF2
minutesFile = open('../automate_online-materials/meetingminutes.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(minutesFile)
minutesFirstPage = pdfReader.getPage(0)
pdfWatermarkReader = PyPDF2.PdfFileReader(open('../automate_online-materials/watermark.pdf', 'rb'))
minutesFirstPage.mergePage(pdfWatermarkReader.getPage(0))
pdfWriter = PyPDF2.PdfFileWriter()
pdfWriter.addPage(minutesFirstPage)

for pageNum in range(1, pdfReader.numPages):
    pageObj = pdfReader.getPage(pageNum)
    pdfWriter.addPage(pageObj)

resultPdfFile = open('watermarkedCover.pdf', 'wb')
pdfWriter.write(resultPdfFile)
minutesFile.close()
resultPdfFile.close()
```

## Encrypting PDFs
A PdfFileWriter object can also add encryption to a PDF document. Enter the following into the interactive shell:

    


```python
import PyPDF2
pdfFile = open('../automate_online-materials/meetingminutes.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(pdfFile)
pdfWriter = PyPDF2.PdfFileWriter()
for pageNum in range(pdfReader.numPages):
    pdfWriter.addPage(pdfReader.getPage(pageNum))

pdfWriter.encrypt('swordfish')
resultPdf = open('encryptedminutes.pdf', 'wb')
pdfWriter.write(resultPdf)
resultPdf.close()
```


```python

```
