from PIL import Image


class ImageReader:
    __image = None
    __image_pixels = None

    def __init__(self, file):
        self.__image = Image.open(file, 'r')
        if self.__image is not None:
            self.__image_pixels = self.__image.load()

    def get_image_size(self):
        return self.__image.size

    def get_image_pixel(self, x, y):
        return self.__image_pixels[x, y]


class ImageConverter:
    __image_reader = None

    def __init__(self, image_reader):
        self.__image_reader = image_reader

    def print_as_ascii(self):
        width, height = self.__image_reader.get_image_size()
        x_step = 3
        y_step = 6
        print(f"width/height/xstep/ystep={width}/{height}/{x_step}/{y_step}")
        for y in range(0, height, y_step):
            for x in range(0, width, x_step):
                sum_red = 0
                sum_blue = 0
                sum_green = 0
                pixels = 0
                for yy in range(y, min(y + x_step, height)):
                    for xx in range(x, min(x + y_step, width)):
                        rgb = self.__image_reader.get_image_pixel(xx, yy)
                        sum_red += rgb[0]
                        sum_blue += rgb[1]
                        sum_green += rgb[2]
                        pixels += 1
                grayscale_value = (sum_red + sum_blue + sum_green) / (pixels * 3)
                self.__print_color_as_ascii(grayscale_value, True)
            print()

    @staticmethod
    def __print_color_as_ascii(color_value, invert_colours=False):
        ascii_chars = '@&%#(/*,. '
        if invert_colours:
            ascii_chars = ascii_chars[::-1]

        if color_value < 25:
            ascii_char = ascii_chars[0]
        elif color_value < 50:
            ascii_char = ascii_chars[1]
        elif color_value < 75:
            ascii_char = ascii_chars[2]
        elif color_value < 100:
            ascii_char = ascii_chars[3]
        elif color_value < 125:
            ascii_char = ascii_chars[4]
        elif color_value < 150:
            ascii_char = ascii_chars[5]
        elif color_value < 175:
            ascii_char = ascii_chars[6]
        elif color_value < 200:
            ascii_char = ascii_chars[7]
        elif color_value < 225:
            ascii_char = ascii_chars[8]
        else:
            ascii_char = ascii_chars[9]

        print(ascii_char, end='')


ir = ImageReader('penguin.png')
converter = ImageConverter(ir)
converter.print_as_ascii()

# TODO: parameterize step values and invert option.
# TODO: refactor to be able to work as a library/module as well as a script.
