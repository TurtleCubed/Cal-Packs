from Display import Display
from ImageReader import ImageReader
import BogoPack
from BinaryPack import BinaryPack

test = [ImageReader.text_to_array("triceratops.dino"), ImageReader.text_to_array("pterodactyl.dino")]
a = BinaryPack(400, 300, test)
image = Display.tray_to_image(a.pack())
image.show()
print(a.num_dinos, a.percent_full())