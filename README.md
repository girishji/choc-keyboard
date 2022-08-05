## Kailh Choc Keyboard with hotswap

A keyboard PCB for Kailh Choc low profile switches using KiCad. PCB has
soldering holes for Blackpill (STM32F401) and Adafruit IS31FL3731 breakout
board.

- Use 1.2mm thickness pcb (suitable for Choc 1350 hotswap sockets)
- Diodes are SOD-123 (1N4148)
- LED is SMD 6028 monochrome (you can get white ones from aliexpress). They are
  connected through charlieplex using IS31FL3731 LED driver (Adafruit's
  breakout board). 
- IS31FL3731 drives (PWM) LEDs at 8k Hz. This may cause audible buzz from the
  ceramic capacitors on board of Adafruit board when driven full power. To
  remove noise replace the 2 10uF capacitors on the Adafruit board with
  tantalum capacitors. Alternately, set maximum intensity of LEDs to a value of
  100 (max is 256) in QMK.
- MCU is STM32F401 (Blackpill). See the schematic for row/column connections.
  This MCU comes with USB-C.
- QMK code for this keyboard is on
  [github](https://github.com/girishji/qmk_firmware/tree/girish_dev_branch/keyboards/chockb/rev1)
- Switch plate with cutouts for switches is in switch-plate directory; If you are
  using jlcpcb, have it made with 1.2mm pcb; preferably in aluminum since it holds
  the switches better.
- There are gerber files for jlcpcb; Compress them into a zip file and upload
  it to jlcpcb

![front side](https://i.imgur.com/7ngL65q.jpg)
![back side](https://i.imgur.com/xvfgL1L.jpg)

