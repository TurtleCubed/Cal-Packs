from PIL import Image

class Display:

    @staticmethod
    def tray_to_image(tray):
        img = Image.new("1", (len(tray[0]), len(tray)))
        pixels = img.load()

        for i in range(img.size[0]):
            for j in range(img.size[1]):
                pixels[i, j] = (tray[j][i])

        return img

