# HiFive Inventor aka SiFive Learn Inventor
## Overview
This is a great little developer board, originally targetted at 7+ year old kids. Unfortunately due to licensing contract expiring, it's no longer supported. It was originally associated with the BBC Dr. Who, including narration of the tutorial videos. These videos do not appear to be available on YouTube, there are some review videos and others that include people working through the exercises.

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
  *  TBD: Address 0101001b aka 0x29 aka 41 (decimal)
* Accelerometer & Compass & Temperature Sensors (TBD: I2C or SPI)
  *  TBD: Pin 2 CS_XL selects SPI/I2C
  *  TBD: Pin 3 CS_MAG selects SPI/I2C
  *  TBD: Pin 7 INT_MAG/DRDY Interrupt when data is available
  *  TBD: Pin 11 & 12 aka INT_2_XL & INT_1_XL respectively when Accel data is available
  *  TBD: Accel Address 0011001b aka 0x19 aka 25 (decimal)
  *  TBD: Mag Address 0011110b  aka 0x1E aka 30 (decimal)
* Edge Connector (0, 1, 2) + 3V & GND
  *  TBD: Edge 0 is PWM on Microcontroller for playing Tunes
  *  micro:bit compatibility  
    * Pin 12 on the Inventor is not connected to any MicroController pin

Additional components not programmed directly, but on the PCB
* SEGGER J-Link (firmware hosted on a Kinetis K22F 128 KB Flash Cortex M-4)
* Reset Button
* 512 kB Flash Memory (0.5 MB)
* USB Port for Drag & Drop Programming

## Notes:
* The HiFive1RevB is an Arduino style board with the same core processing (FE310, ESP32, Segger OB) but without the LED Matrix and other sensors on the HiFive Inventor board.  [HiFive1RevB](https://www.sifive.com/boards/hifive1-rev-b)  TBD: Pinout or the use of [SiFive Freedom Studio](https://www.sifive.com/software/sifive-freedom-studio)
* If powered via the Edge Connector the LED's will not light up.
* [YouTube Playlist (kind of random)](https://www.youtube.com/playlist?list=PLvZXTXiQDCe7YSpDQmd2ksVSHb431ns7F)
* Python stuff & firmware blobs [HiFive-PythonSandbox](https://github.com/damianburrin/HiFive-PythonSandbox/tree/main/h5%20updater-20240605T172322Z-001/h5%20updater/hifive_updater)


## Technical User Guide [Technical User Guide](HiFive_Inventor_Tech_UG_Web.pdf)

## Marketing Phrases to describe what can be built
* Develop an Intergalactice weather service
* Wirelessly pilot an alien spaceship
* Learn to control a robot
* send and receive emojis
* Build alien musical instruments
* Create a security system

## Original Blockly Programs
1.  Use the compass to display a green arrow when the kit is oriented to the north or a red cross in the other cases.
2.  [More project names](https://youtu.be/7QDixjAANNQ?si=xpowm5YkKtd2wJIu&t=236)

## Original Python Programs
1. Scroll on the LED matrix: "Hello World!"  
??.  Create a Melody

## micro:bit Accessories
See full descriptions, below are only the "caveats" (things that don't work). Others may also work, but weren't known to work in 2021. Pin 12 is not available on HiFive Inventor. Review the issues noted below and research before purchasing.  
[micro:bit accessories supported by HiFive Inventor](https://web.archive.org/web/20210614053018/https://www.hifiveinventor.com/getting-started/creative) 
### SparkFun micro:bot
### SparkFun micro:climate
### SparkFun gator:science
### Pimoroni enviro:bit
### Pimoroni noise:bit
### Pimoroni touch:bit
### Pimoroni bit:commander
* Audio is compromised
* Red Button: Pin 12 is not connected on the HiFIve therefore it will not function
* Use batteries in the bit:commander, it will power the HiFive
### Pimoroni simon:says
* Touch Pad C: Pin 12 is not connected on the HiFive therefore will not function (breaking failure or only 3 button/leds work)
### Kitronik:game

[Pimoroni micro:bit accessories](https://shop.pimoroni.com/search?q=micro:bit&product_type=micro:bit%20Addon&stock=true)

