# HiFive Inventor
## Overview
This is a great little developer board, originally targetted at 7+ year old kids. Unfortunately due to licensing issue, it's no longer supported. It was originally associated with the BBC Dr. Who, including narration of the tutorial videos. These videos do not appear to be available on YouTube, there are many review videos and others that include people working through the exercises.

The board has the following features:  
* 150 MHz RISC-V CPU - RV32IMAC
  * 8 kB One Time Programmable
  * 16 kB Instruction Cache
  * 64 kB Data SRAM
  * 3 PWM Controllers
  * SPI
  * I2C
  * 2 UART
  * JTAG Debugging
* ESP32-SOLO-1 Module providing WiFi & Bluetooth via UART to the RISC-V CPU
  * 250 MHz
  * 32-bit LX6 Single Core Microprocessor
  * 448 KB ROM, 520 KB SRAM, 8 KB SRAM in RTC
  * 802.11 b/g/n
  * v4.2 Bluetooth LE
* 6x8 RGB LED Matrix via WS2812
* 2 Buttons A & B
* Light Sensor (To Confirm: I2C)
* Accelerometer & Compass (TBD: I2C or SPI)
* Edge Connector (0, 1, 2) + 3V & GND

Additional components not programmed directly, but on the PCB
* SEGGER J-Link (firmware hosted on a Kinetis K22F 128 KB Flash Cortex M-4)
* Reset Button
* 512 kB Flash Memory (0.5 MB)
* USB Port for Drag & Drop Programming

## Notes:
* The HiFive1RevB is an Arduino style board with the same core processing (FE310, ESP32, Segger OB) but without the LED Matrix and other sensors on the HiFive Inventor board.  [HiFive1RevB](https://www.sifive.com/boards/hifive1-rev-b)  TBD: Pinout or the use of [SiFive Freedom Studio](https://www.sifive.com/software/sifive-freedom-studio)
* If powered via the Edge Connector the LED's will not light up.

## Technical User Guide [Technical User Guide](HiFive_Inventor_Tech_UG_Web.pdf)

## Original Blockly Programs
1.  Use the compass to display a green arrow when the kit is oriented to the north or a red cross in the other cases.
2.  [More project names](https://youtu.be/7QDixjAANNQ?si=xpowm5YkKtd2wJIu&t=236)

## Original Python Programs
1. Scroll on the LED matrix: "Hello World!"  
??.  Create a Melody
