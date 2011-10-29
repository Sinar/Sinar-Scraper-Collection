from pdfminer.pdfparser import PDFParser,PDFDocument
from pdfminer.pdfinterp import PDFResourceManager,PDFPageInterpreter
from pdfminer.pdfdevice import PDFDevice
from pdfminer.layout import LAParams
from pdfminer.converter import PDFPageAggregator
from pdfminer.layout import LTTextBox, LTTextLine, LTFigure, LTImage, LTChar,LTTextBoxHorizontal
import re


class Document:
    def __init__(self,filename,password=''):
        self.extracted_text = ''
        self.xml_text = ''
        self.data_structure = {}
        self.fp = open(filename,'rb')
        self.parser = PDFParser(self.fp)
        self.doc = PDFDocument()
        self.parser.set_document(self.doc)
        self.doc.set_parser(self.parser)
        self.password = password
        self.doc.initialize(self.password)

        self.rsrcmgr = PDFResourceManager()
        self.laparams = LAParams()

        self.device = PDFPageAggregator(self.rsrcmgr,laparams=self.laparams)

        self.interpreter = PDFPageInterpreter(self.rsrcmgr,self.device)
        
            
    def get_layout(self):
        for page in self.doc.get_pages():
            self.interpreter.process_page(page)
            layout = self.device.get_result()
            yield layout
    

    def get_item(self,page):
        for item in page:
            yield item
            
    
    
        
