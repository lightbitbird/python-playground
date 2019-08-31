# You deed install python-pptx at first
# pip install python-pptx
from pathlib import Path
import pptx
from pptx.util import Pt, Inches
import os


def create_slide(ppt, title, img_path):
    slide = ppt.slides.add_slide(ppt.slide_layouts[5])

    title_holder = slide.shapes.placeholders[0]
    title_frame = title_holder.text_frame
    title_frame.paragraphs[0].text = title
    title_frame.paragraphs[0].font.size = Pt(36)

    left, top, width = Inches(2), Inches(1.5), Inches(6)
    slide.shapes.add_picture(img_path, left, top, width=width)


current_dir = os.path.dirname(__file__)
prs = pptx.Presentation()
img_dir = Path(current_dir + '/prs')

for img in sorted(img_dir.glob('*.png')):
    file_name = img.stem
    prs_title = file_name.split('.')[0]
    create_slide(prs, prs_title, str(img))

ppt_path = img_dir.stem + '.pptx'
prs.save(current_dir + '/' + ppt_path)
