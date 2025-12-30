# micropython-board-NRF52840
Micropython Board Definition for SuperMini / Nice!Nano / Pro Micro with nRF52840
SuperMini NRF52840 is a Pro Micro alternative development board that is compatible with Nice! Nano. See https://wiki.icbbuy.com/doku.php?id=developmentboard:nrf52840
It comes with the Adafruit nRF52 UF2 bootloader und Softdevice 140 preinstalled. 
The board shows up as a USB storage device. Just copy build-SUPERMINI_NRF52840/firmware.uf2 to the storage device to install.

firmware.uf2 has the required offset of 0x26000 . See https://github.com/adafruit/Adafruit_nRF52_Bootloader for details.

Work in progress...

## SUPERMINI_NRF52840 
basic board definition for the SuperMini / Nice!Nano / Pro Micro with nRF52840 works with micropython main repo
build instructions:
```
./drivers/bluetooth/download_ble_stack.sh s140_nrf52_6_1_1
make submodules
make BOARD=SUPERMINI_NRF52840
```

## SUPERMINI_NRF52840_NIMBLE
experimental, needs some patches for nimble ble stack and rtc support. The machine_bitstream driver to drive NeoPixel LEDs works for a couple of NeoPixel (Matrix) I have tested.
Pre build firmware can be found in the firmware directory.

## FEATHER_NRF52840
board definition for the Adafruit NRF528420 Feather (https://www.adafruit.com/product/4062). The board has the Adafruit nRF52 UF2 bootloader und Softdevice 140 preinstalled. The board definition is almost the same as for the Supermini Borad. Works with micropython main repo
build instructions:
```
./drivers/bluetooth/download_ble_stack.sh s140_nrf52_6_1_1
make submodules
make BOARD=FEATHER_NRF52840
```

test the on board neopixel led (ws1812) with:
```
from machine import Pin
from neopixel import NeoPixel
pixel = NeoPixel(Pin(16, Pin.OUT), 1)
pixel[0] = (0, 255, 0)
pixel.write()
```

some later revisions may have a NEOPIXEL_POWER pin (P46). If the neopixel does not work try to set pin 46 high.
the feather board has extra 2MB octco spi flash (GD25Q16)

the flash can be mounted with the script ``flash.py`` (code from https://github.com/robert-hh/SPI_Flash/) in this folder.
not tested but looks interesting: https://github.com/julien123123/Micropython-Helpers/tree/0101bd419a31bcf5f83d68667397a84463c8f5a0/nrfutils (adds deepsleep)

## FEATHER_NRF52840_NIMBLE
experimental, needs some patches for nimble ble stack and rtc support. Pre build firmware can be found in the firmware directory.

