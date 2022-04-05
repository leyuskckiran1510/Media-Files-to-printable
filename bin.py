from PIL import Image, ImageColor
from functools import lru_cache

@lru_cache(maxsize=None)
class Run:
    def __init__(self,file,w=50,h=50):
        self.w = w
        self.h = h
        self.file = file


    def BW(self):
        img = Image.open(self.file)
        img = img.resize((self.w,self.h))
        img = img.convert("L")
        arry = ''
        for y in range(0, img.size[1]):
            for x in range(0, img.size[0]):
                a = img.getpixel((x, y))
                c = int(int(a) /10.7)
                arry += f'\x1b[48;5;{232+ c}m \x1b[0m'
            arry += "\n"
        return arry

    def RGB(self):
        img = Image.open(self.file)
        img = img.resize((self.w,self.h))
        img = img.convert("RGB")
        arry = ''
        for y in range(0, img.size[1]):
            for x in range(0, img.size[0]):
                a = img.getpixel((x, y))
                arry += f'\x1b[48;2;{a[0]};{a[1]};{a[2]}m`\x1b[0m'
            arry += "\n"
        return arry


if __name__ == "__main__":
    for i in range(1, 545):
        i = (3 - len(str(i))) * "0" + str(i)
        a = Run(f'./seq/img_{i}.png')
        a = a.RGB()
        print(a)



