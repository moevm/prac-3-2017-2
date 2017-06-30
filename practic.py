# -*- coding: utf-8 -*-
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase import ttfonts
def textParsing (text):
    textmasiv=text.split('\n')
    for line in range(len(textmasiv)):
        textmasiv[line]=textmasiv[line].split();
    return textmasiv

def interpritator(text):
    upClamping=770
    downClamping=40
    border=40
    step=14
    MyFontObject = ttfonts.TTFont('Time', 'timesi.ttf')
    pdfmetrics.registerFont(MyFontObject)
    MyCanvas = canvas.Canvas("sample.pdf")
    textobj = MyCanvas.beginText(border,upClamping)
    textobj.setFont("Time", 12)
    text = textParsing(text)
    textobj.setLeading(14)
    for lineWord in text:
        textobj.moveCursor(10, 0)
        i=0
        for word in range(len(lineWord)):
            if (textobj.getX() + 6 * len(lineWord[word])) > 550:
                upClamping -= step
            if upClamping - 2*step < downClamping:
                MyCanvas.drawText(textobj)
                MyCanvas.showPage()
                upClamping = 770
                textobj = MyCanvas.beginText(border, upClamping)
                textobj.setFont("Time", 12)
                textobj.setLeading(14)

            if (textobj.getX()+6*len(lineWord[word]))<=550:
                str = lineWord[word] + " "
                textobj.textOut(str)
                border=40
            else:
                if i == 0:
                    textobj.moveCursor(-10, 0)
                    i+=1
                textobj.textLine("")
                str = lineWord[word] + " "
                textobj.textOut(str)
                border=50
        if i==0:
            textobj.moveCursor(-10, 0)
        border=50
        upClamping -= 2*step
        textobj.textLine("")
        textobj.textLine("")
    MyCanvas.drawText(textobj)
    MyCanvas.save()


if __name__=="__main__":
    text=input()
    interpritator(text)
