requires micropython fork 

https://github.com/andrewleech/micropython/tree/nrf_ubluetooth

git clone https://github.com/andrewleech/micropython.git
cd micropython
git checkout nrf_ubluetooth 
make -C mpy-cross
cd ports/nrf
make submodules
make BOARD=SUPERMINI_NRF52840
cp build-SUPERMINI_NRF52840/firmware.uf2 /Volumes/NICENANO/



see also
https://github.com/micropython/micropython/pull/8318

to enable RTC another pr is needed 
https://github.com/micropython/micropython/pull/14198
