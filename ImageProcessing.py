import os
from PIL import Image, ImageOps

SIZE = (400, 650)

def getfiles():
    files = []
    for file in os.listdir(os.getcwd()):
        if file.endswith(".jpg"):
            files += [file]
    return files

def resizetype(file):
    image = Image.open(file)
    width, height = image.size
    aspect = height/width
    if aspect < 1.8 and aspect > 1.5:
        newi = resizer(image)
    else:
        newi = bordermaker(image, height, width, aspect)
    return newi


def bordermaker(image, height, width, aspect):
    if width > SIZE[0]:
        widthdiff = width - SIZE[0]
        heightdiff = int(widthdiff * aspect)
        newsize = (SIZE[0], height - heightdiff)
    else:
        widthdiff = SIZE[0] - width
        heightdiff = int(widthdiff * aspect)
        newsize = (SIZE[0], height + heightdiff)
    newi = image.resize(newsize)
    bordersize = int((SIZE[1] - newsize[1])/2)
    bordered = ImageOps.expand(newi, border=(0, bordersize), fill='white')
    return bordered
    
def filehandler(images):
    for img in images:
        out = resizetype(img)
        out.save(f"New_{img}")



def resizer(image):
    newi = image.resize(SIZE)

if __name__ == '__main__':
    filehandler(getfiles())
    print('wow, that finished without errors?')
