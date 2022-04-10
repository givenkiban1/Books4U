from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
import requests

# https://stackoverflow.com/questions/2563822/how-do-you-composite-an-image-onto-another-image-with-pil-in-python
# https://www.geeksforgeeks.org/python-pil-image-resize-method/

def CreateAd(img, cost, condition, ref):

    response = requests.get(img)

    file = open("images/sample_image.png", "wb")
    file.write(response.content)
    file.close()

    img="images/sample_image.png"

    bg = Image.open(r"images/canvas.png")

    bg_w, bg_h = bg.size

    # bg.show()

    fg = Image.open(f"{img}")

    fg_w, fg_h = fg.size

    ideal_w=590
    ideal_h=694

    ideal_x=29
    ideal_y=358

    # fg.show()

    img1 = fg.resize((ideal_w, ideal_h))

    # img1.show()

    bg.paste(img1, (ideal_x, ideal_y))
    draw = ImageDraw.Draw(bg)
    # bg.show()

    font58 = ImageFont.truetype("fonts/arial.ttf", 58)

    font140 = ImageFont.truetype("fonts/arial.ttf", 140)

    font90 = ImageFont.truetype("fonts/arial.ttf", 90)

    text_x=670
    price_y=436
    price_label_y=358
    condition_y=726
    condition_label_y=648
    ref_y=967
    ref_label_y=889

    draw.text((text_x, price_label_y), "Price", (2555,255,255), font=font58)
    draw.text((text_x, price_y), f"R{cost}", (2555,255,255), font=font140)
    draw.text((text_x, condition_label_y), "Condition", (2555,255,255), font=font58)
    draw.text((text_x, condition_y), condition, (2555,255,255), font=font90)
    draw.text((text_x, ref_label_y), "Ref:", (2555,255,255), font=font58)
    draw.text((text_x, ref_y), ref, (2555,255,255), font=font90)

    bg.show()