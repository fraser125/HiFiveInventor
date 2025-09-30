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
* SEGGER J-Link
* Reset Button
* 512 kB Flash Memory (0.5 MB)
* USB Port for Drag & Drop Programming

Notes:
* If powered via the Edge Connector the LED's will not light up.

## Technical User Guide [Technical User Guide](HiFive_Inventor_Tech_UG_Web.pdf)

