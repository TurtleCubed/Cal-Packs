from Display import Display
from ImageReader import ImageReader
import BogoPack

dino_array = ImageReader.text_to_array("triceratops.dino")
# dino_array = ImageReader.text_to_array("small.dino")
image = Display.tray_to_image(dino_array)
image.show()
