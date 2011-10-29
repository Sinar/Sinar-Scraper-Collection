====================
Scraper Collections
====================

Preprocessing
---------------
Use the pdftotext tools of xpdf package to convert pdf to text. 

::

  pdftotext -layout pdf_file.pdf

Scraper
---------  
  

- hansard_parser.py
  
  this split question and answer into different files, work in progress. it only handle question and answer, but there is more in the hansard, 
  but the question and answer block is more sane to parse
  
- order_paper_parser.py 

  This is to parse the order paper in the parliament, but not much user I think
  
  