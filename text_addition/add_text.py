from PIL import Image, ImageDraw, ImageFont
import deep_translator


def add_text(text: str, path="") -> None:
    im = Image.new('RGB', (1280, 720), color=('#FAACAC'))
    draw_text = ImageDraw.Draw(im)
    draw_text.text(
        (500, 500),
        deep_translator.GoogleTranslator('auto', 'ru').translate(text),
        font=ImageFont.truetype('DischargePro.ttf', size=36),
        fill=('#1C0606')
    )
    im.show()
