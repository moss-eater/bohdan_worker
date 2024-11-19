from PIL import Image
from PIL import ImageFilter

with Image.open('original.jpg') as flower_original:
    print("Sizee fluwer:", flower_original.size)
    print("Fuermat fluwer:", flower_original.format)
    print("Le moeden au fluwer:", flower_original.mode)
#    flower_original.show()

    flower_gray = flower_original.convert("L")
    flower_gray.save("gray.jpg")
    print("Sizee groey fluwer:", flower_gray.size)
    print("Fuermat groey fluwer:", flower_gray.format)
    print("Le moeden au groey fluwer:", flower_gray.mode)
#    flower_gray.show()

    flower_blured = flower_original.filter(ImageFilter.BLUR)
    flower_blured.save("blured.jpg")
    print("Sizee bluerre fluwer:", flower_blured.size)
    print("Fuermat bluerre fluwer:", flower_blured.format)
    print("Le moeden au bluerre fluwer:", flower_blured.mode)
#    flower_blured.show()

    flower_up = flower_original.transpose(Image.FLIP_LEFT_RIGHT)
    flower_up.save("up.jpg")
    print("Sizee uppedd fluwer:", flower_up.size)
    print("Fuermat uppedd fluwer:", flower_up.format)
    print("Le moeden au uppedd fluwer:", flower_up.mode)
    flower_up.show()

    flower_mirror = flower_original.transpose(Image.FLIP_LEFT_RIGHT)
    flower_blured.save("up.jpg")
    print("Sizee uppedd fluwer:", flower_up.size)
    print("Fuermat uppedd fluwer:", flower_up.format)
    print("Le moeden au uppedd fluwer:", flower_up.mode)
#    flower_up.show()