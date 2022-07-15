import argparse
from curses import newwin
from PIL import Image

parser = argparse.ArgumentParser(
    prog="Image Cropper",
    description="This program can crop images in grid separately.",
    usage='%(prog)s [options]')

parser.add_argument("-i", "--image", help="Path to the image", required=True)
parser.add_argument("-c", "--columns", help="Columns to crop")
parser.add_argument("-r", "--rows", help="Rows to crop")
parser.add_argument("-w", "--width", help="Width to crop")
parser.add_argument("-he", "--height", help="Height to crop")
parser.add_argument("-o", "--output", help="Path to output",  required=True)

arguments = parser.parse_args()

try:
    originalImage = Image.open(arguments.image)
except FileNotFoundError:
    print("[error] File not found")
    exit()

columnsGap = 0
rowGap = 0

if(arguments.columns and arguments.rows):
    fatorW = int(arguments.columns)
    fatorH = int(arguments.rows)
elif(arguments.width and arguments.height):
    fatorW = int(arguments.width)
    fatorH = int(arguments.height)
else:
    exit()

extension = originalImage.format.lower()
width, height = originalImage.size

newWidth = width / fatorW
newHeight = height / fatorH

for imageNum in range(fatorW * fatorH):
    left = (imageNum % fatorW) * newWidth
    upper = (imageNum % fatorH) * newHeight
    right = left + newWidth
    lower = upper + newHeight

    newImage = originalImage.crop((left, upper, right, lower))
    newImage.save("{}/{}.{}".format(arguments.output, imageNum, extension))
