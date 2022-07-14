## Kailh Choc Keyboard with hotswap

A keyboard PCB for Kailh Choc low profile switches using KiCad. PCB has
soldering holes for Blackpill (STM32F401) and Adafruit IS31FL3731 breakout
board.

- Use 1.2mm thickness pcb (suitable for Choc 1350 hotswap sockets)
- Diodes are SOD-123 (1N4148)
- LED is SMD 6028 monochrome (you can get white ones from aliexpress). They are
  connected through charlieplex using IS31FL3731 LED driver (Adafruit's
  breakout board). 
- Some notes on LEDs: IS31FL3731 drives (PWM) LEDs at 8k Hz. This causes
  audible buzz (annoying) from the ceramic capacitors on board of Adafruit
  board. To remove noise replace the 2 10uF capacitors on the Adafruit board
  with tantalum capacitors.
- MCU is STM32F401 (Blackpill). See the schematic for row/column connections.
  This MCU comes with USB-C.
- QMK code for this keyboard is on
  [github](https://github.com/girishji/qmk_firmware/tree/girish_dev_branch/keyboards/handwired/giri/aria)


