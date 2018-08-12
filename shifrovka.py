from PIL import Image, ImageDraw, ImageFont

f = open("text.txt", "r")
text = f.read()
f.close()

imgmask = Image.open("kot.jpg")
w, h = imgmask.width, imgmask.height
img = Image.new("RGB", (w, h))
draw = ImageDraw.Draw(img)

font = ImageFont.truetype("arial.ttf", 16)
draw.text((0, 0), text, (255, 255, 255), font=font)

pix = img.load()
pixmask = imgmask.load()
resi = Image.new("RGB", (w, h))
res = ImageDraw.Draw(resi)
for i in range(w):
    for j in range(h):
        if pix[i, j][0] > 128:
            print((pixmask[i, j][0] // 2) * 2)
            res.point((i, j), ((pixmask[i, j][0] // 2) * 2, pixmask[i, j][1],
                      pixmask[i, j][2]))
        else:
            res.point((i, j), ((pixmask[i, j][0] // 2) * 2 + 1, pixmask[i, j][1],
                      pixmask[i, j][2]))
resi.save("res.png", "PNG")
img.save("taina.png", "PNG")
del draw
del res





