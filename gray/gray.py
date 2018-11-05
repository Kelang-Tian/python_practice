# converts a color image to gray scale
from graphics import *


def colorchange(pic):
    width = pic.getWidth()
    height = pic.getHeight()
    for i in range(width):
        for j in range(height):
            r, g, b = pic.getPixel(i, j)
            brightness = int(round(0.299 * r + 0.587 * g + 0.114 * b))
            pic.setPixel(i, j, color_rgb(brightness, brightness, brightness))


def main():
    win = GraphWin('gray scale convert', 640, 480)
    img = Image(Point(320, 244), "hippo.ppm")
    img.draw(win)
    # 等待点击
    win.getMouse()
    colorchange(img)
    win.getMouse()
    win.close()


if __name__ == '__main__':
    main()
