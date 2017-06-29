# -*- coding: utf-8 -*-
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase import ttfonts
def textParsing (text):
    countSymbol = 90
    textmasiv=text.split('\n')
    for line in range(len(textmasiv)):
        text=[]
        for i in range(len(textmasiv[line])//countSymbol+1):
            text.append(textmasiv[line][i*countSymbol:countSymbol*(i+1)])
        textmasiv[line]=text
        text=[]
    return textmasiv

def interpritator(text="Привет, Мир!"):
    upClamping=760
    downClamping=40
    border=50
    step=14
    MyFontObject = ttfonts.TTFont('Time', 'timesi.ttf')
    pdfmetrics.registerFont(MyFontObject)
    MyCanvas = canvas.Canvas("sample.pdf")
    textobj = MyCanvas.beginText()
    textobj.setFont("Time", 12)
    text=textParsing(text)
    for lineMas in text:
        for line in lineMas:
            textobj.setTextOrigin(border, upClamping)
            border=40
            textobj.textLine(line)
            upClamping-=step
            if (upClamping-step < downClamping):
                MyCanvas.drawText(textobj)
                textobj = MyCanvas.beginText()
                MyCanvas.showPage()
                upClamping=760

        border=50
        upClamping -= step
        MyCanvas.drawText(textobj)
    MyCanvas.save()


if __name__=="__main__":
    text=input()
    # text = """ Эта книга адресована всем, кто изучает русский язык. Но состоит она не из правил, упражнений и учебных текстов. Для этого созданы другие замечательные учебники.
    # У этой книги совсем иная задача. Она поможет вам научиться не только разговаривать, но и размышлять по-русски. Книга, которую вы держите в руках, составлена из афоризмов и размышлений великих мыслителей, писателей, поэтов, философов и общественных деятелей различных эпох. Их мысли - о тех вопросах, которые не перестают волновать человечество.
    # Вы можете соглашаться или не соглашаться с тем, что прочитаете в этой книге. Возможно, вам покажется, что какие-то мысли уже устарели. Но вы должны обязательно подумать и обосновать, почему вы так считаете.
    # Parents and grandparents are always on the lookout for kids’ craft projects that will engage children and keep those little hands busy. Thankfully there are many inexpensive books that are filled with ideas. For example, you can find books that outline crafts using play dough, how to make flower figures, and even Christmas crafts. In fact, you can even find books that provide ideas for making Christmas gifts that fit in a jar. From crafts for preschool-age children to pastimes tor older kids these idea books provide a wealth of options for engaging children’s imaginations.
    # """
    interpritator(text)

