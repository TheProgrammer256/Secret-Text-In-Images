from PIL import Image, ImageDraw

img = Image.open("res.png")
w, h = img.width, img.height
profil = Image.new("RGB", (w, h))
pr = ImageDraw.Draw(profil)
pix = img.load()
for i in range(w):
    for j in range(h):
        if pix[i, j][0] % 2 == 0:
            pr.point((i, j), (255, 255, 255))
        else:
            pr.point((i, j), (0, 0, 0))

profil.save("final.png", "PNG")
del pr
