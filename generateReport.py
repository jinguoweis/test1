import tempfile

from reportlab.lib import colors
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.pdfmetrics import registerFontFamily
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import Paragraph, SimpleDocTemplate, Table, LongTable, Image
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_JUSTIFY






def genReport(id, age, zr, mfcc, maxDeg, secDeg, selfSASc, file, preclass, secPreClass, type, degree, maxprob, secprob):
    # print("generate_probability:{}".format(probability))
    pdfmetrics.registerFont(TTFont('SimSun', './statics/FZLTXIHK.TTF'))  # 默认不支持中文，需要注册字体
    pdfmetrics.registerFont(TTFont('SimSunBd', './statics/FZLTXIHK.TTF'))
    # registerFontFamily('SimSun', normal='SimSun', bold='SimSunBd', italic='VeraIt', boldItalic='VeraBI')

    stylesheet = getSampleStyleSheet()  # 获取样式集

    # 获取reportlab自带样式
    Normal = stylesheet['Normal']
    BodyText = stylesheet['BodyText']
    Italic = stylesheet['Italic']
    Title = stylesheet['Title']
    Heading1 = stylesheet['Heading1']
    Heading2 = stylesheet['Heading2']
    Heading3 = stylesheet['Heading3']
    Heading4 = stylesheet['Heading4']
    Heading5 = stylesheet['Heading5']
    Heading6 = stylesheet['Heading6']
    Bullet = stylesheet['Bullet']
    Definition = stylesheet['Definition']
    Code = stylesheet['Code']

    # 自带样式不支持中文，需要设置中文字体，但有些样式会丢失，如斜体Italic。有待后续发现完全兼容的中文字体
    Normal.fontName = 'SimSun'
    Italic.fontName = 'SimSun'
    BodyText.fontName = 'SimSun'
    Title.fontName = 'SimSunBd'
    Heading1.fontName = 'SimSun'
    Heading2.fontName = 'SimSun'
    Heading3.fontName = 'SimSun'
    Heading4.fontName = 'SimSun'
    Heading5.fontName = 'SimSun'
    Heading6.fontName = 'SimSun'
    Bullet.fontName = 'SimSun'
    Definition.fontName = 'SimSun'
    Code.fontName = 'SimSun'

    # 添加自定义样式
    stylesheet.add(
        ParagraphStyle(name='body',
                       fontName="SimSun",
                       fontSize=10,
                       textColor='black',
                       leading=15,  # 行间距
                       spaceBefore=10,  # 段前间距
                       spaceAfter=0,  # 段后间距
                       leftIndent=10,  # 左缩进
                       rightIndent=0,  # 右缩进
                       # firstLineIndent=20,  # 首行缩进，每个汉字为10
                       alignment=TA_JUSTIFY,  # 对齐方式
                       )

    )

    body = stylesheet['body']



    story = []

    # 段落
    content1 = "编号：{} &nbsp &nbsp &nbsp &nbsp &nbsp &nbsp年龄：{} <br/> "\
                "————————————————————————————————————————".format(id, age)
    content3 = "{}".format(mfcc)
    type = "Diagnosis type: &nbsp {}".format(type)
    content4 = "Assessment Scale Score: &nbsp {}__{}".format(selfSASc, degree)
    content5 = 'Zero-Crossing Rate(ZCR): &nbsp {:.7f}'.format(zr)
    content7 = "Predict Class: &nbsp {}_{} {}".format(preclass, maxDeg, maxprob)
    content8 = " &nbsp &nbsp &nbsp &nbsp &nbsp &nbsp &nbsp&nbsp &nbsp {}_{} {}".format(secPreClass, secDeg, secprob)



    story.append(Paragraph("心理诊疗检测报告", Title))
    story.append(Paragraph(content1, body))
    story.append(Paragraph("Mel-Frequency Cipstal Coefficients(MFCC):", Heading3))
    story.append(Paragraph(content3, body))
    story.append(Paragraph(type, body))
    story.append(Paragraph(content4, body))
    story.append(Paragraph(content5, body))
    story.append(Image(r"./waveImg/{}_{}.jpg".format(id,age), 6 * 60, 2 * 60))
    story.append(Paragraph(content7, body))
    story.append(Paragraph(content8, body))



    # file
    doc = SimpleDocTemplate(file)
    doc.build(story)