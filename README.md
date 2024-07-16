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
experimental, needs some patches for nimble ble stack and rtc support. The machine_bitstream driver to drive NeoPixel LEDs works for a couple of NeoPixel (Matrix) I have tested
