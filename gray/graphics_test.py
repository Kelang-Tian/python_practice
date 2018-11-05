from graphics import *


def main():
    window = GraphWin("test", 300, 225, autoflush=False)
    flower = Image(Point(150, 113), "hippo.ppm")
    flower.draw(window)
    window.getMouse()
    for i in range(0, 299):
        for j in range(0, 224):
            r, g, b = flower.getPixel(i, j)
            gray = round(r * 0.299 + g * 0.587 + b * 0.114)
            flower.setPixel(i, j, color_rgb(gray, gray, gray))
    window.getMouse()
    window.close()


if __name__ == '__main__':
    main()
