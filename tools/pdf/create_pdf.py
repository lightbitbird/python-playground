# You need install reportlab at first
# pip install reportlab
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4, portrait
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
import webbrowser
import os


current_dir = os.path.dirname(__file__)
GEN_SHIN_GOTHIC_TTF = current_dir + '/fonts/GenShinGothic-Light.ttf'

FILENAME = current_dir + '/HelloWorld.pdf'
c = canvas.Canvas(FILENAME, pagesize=portrait(A4))

pdfmetrics.registerFont(TTFont('GenShinGothic', GEN_SHIN_GOTHIC_TTF))
font_size = 20
c.setFont('GenShinGothic', font_size)

width, height = A4
c.drawCentredString(width / 2, height / 2 - font_size * 0.4, 'こんにちは、世界！')

c.showPage()
c.save()

webbrowser.open(FILENAME)
