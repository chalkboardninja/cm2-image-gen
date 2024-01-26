import pyperclip as ppc
import numpy as np
from cv2 import imread
from tkinter.filedialog import askopenfilename
import cm2py as cm2

code = ""
save = cm2.Save()

print("Image Reader!")
side = ""
blok = ""
while not side in ["flat", "top"]:
    side = input("Flat on Baseplate or Standing Up (flat/top): ").lower()
while not blok in ["led", "tile"]:
    blok = input("LED Block (works with vanilla CM2PY) or Tile Block (requires modded code in CM2PY)? (led/tile): ").lower()
input("Press Enter to select a file.")
image_path = askopenfilename()
print("Picked " + str(image_path) + "...")
print("Reading...", end=" ")
image = imread(image_path)
print("Done")
print("Converting blocks...", end=" ")
blocks = []
x,y=0,0
for row in image:
    for pixel in row:
        blocks.append(
            save.addBlock(
                [14 if blok == "tile" else 6][0],
                (x,
                 [(len(image) - 1) - y if side == "top" else 0][0],
                 [(len(image) - 1) - y if side == "flat" else 0][0]
                 ),
                False,
                [
                    pixel[2],
                    pixel[1],
                    pixel[0]
                ]
                )
            )
        x += 1
    y += 1
    x = 0
print("Done\nAdding connections...", end=" ")
t_flip_flop = save.addBlock(5, (-1,0,0), True)
for block in blocks:
    save.addConnection(t_flip_flop, block)
print("Done")


code = save.exportSave()
ppc.copy(code)
if code != "":
    print("Copied code to clipboard! :D")
else:
    print("Error exporting save... :(")
print("====SETTINGS====")
print("Side: " + side)
print("Type: " + blok)
print("Image: " + image_path)
