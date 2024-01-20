import pyperclip as ppc
import numpy as np
from cv2 import imread
from tkinter.filedialog import askopenfilename
import cm2py as cm2

fine = 0.0234375
unfine = 16
code = ""
save = cm2.Save()

print("Image Reader!")
side = ""
while not side in ["flat", "top"]:
    side = input("Flat on Baseplate or Standing Up (flat/top): ").lower()
input("Press Enter to select a file.")
image_path = askopenfilename()
print("Picked " + str(image_path) + "...")
print("Reading...", end=" ")
image = imread(image_path)
print("Done")
print("Converting...", end=" ")
blocks = []
x,y=0,0
for row in image:
    for pixel in row:
        blocks.append(
            save.addBlock(
                14,
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
print("Done")


code = save.exportSave()
ppc.copy(code)
print("Copied code to clipboard! :D")
