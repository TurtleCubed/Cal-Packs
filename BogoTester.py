from ImageReader import ImageReader
from BogoPack import BogoPack
from Display import Display

test = [ImageReader.text_to_array("triceratops.dino"), ImageReader.text_to_array("pterodactyl.dino"),
        ImageReader.text_to_array("trex.dino")]
a = BogoPack(400, 300, test)
image = Display.tray_to_image(a.pack())
image.show()
print(a.num_dinos, a.percent_full())