from Display import Display
from ImageReader import ImageReader
import BogoPack
from BinaryPack import BinaryPack

test = [ImageReader.text_to_array("triceratops.dino")]
a = BinaryPack(800, 800, test)
image = Display.tray_to_image(a.pack())
image.show()
print(a.num_dinos, a.percent_full())