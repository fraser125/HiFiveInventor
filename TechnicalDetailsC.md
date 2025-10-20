# Technical Documentation - HiFive Inventor
Useful primarily for C programming.

Note: TBD = To Be Determined (i.e. To Be Confirmed)

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
  * WS2812 is used in a chain from one LED to the next
  * CPU Pin 44: Used as a Digital Output
  * Pixel 0 = Top Right
  * Right to Left on all rows
  * Pixel 42 = Bottom Left
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
    * Pin 12 on the Inventor is not connected to any MicroController pin spec says "Reserved:accessibility"
    * If powered via the Edge Connector the LED's will not light up.   
  * [micro:bit Edge Connector Pins](https://tech.microbit.org/hardware/edgeconnector/)  
  * TBD: Ring 0 is Analog In (HiFive:Speaker  PWM out from Microcontroller for playing Tunes)
  * TBD: Ring 1 is Analog In + GPIO
  * TBD: Ring 2 is Analog In + GPIO
  * Left to Right (Ring 0 to GND)
  * TBD: Edge P3 (left of 0) LED Col 3/Analog In
  * TBD: Edge P4 (right of 0) LED Col 1/Analog In  * 
  * TBD: Edge P5 Button A
  * TBD: Edge P6 LED Col 4
  * TBD: Edge P7 (left of 1) LED Col 2
  * TBD: Edge P8 (right of 1) GPIO
  * TBD: Edge P9 GPIO
  * TBD: Edge P10 LED Col 5 / Analog In
  * TBD: Edge P11 Button B
  * TBD: Edge P12 (left of 2) Reserved:accessibility Unrouted on HiFive
  * CPU Pin 31: Edge P13 (right of 2) SPI1:SCK
  * CPU Pin 29: Edge P14 SPI1:MISO
  * CPU Pin 28: Edge P15 SPI1:MOSI
  * CPU Pin 27: Edge P16 GPIO (CPU:SS0)
  * Edge +3v3 (left of 3v)
  * Edge +3v3 (right of 3v)
  * CPU Pin 37: Edge P19 I2C1:SCL
  * CPU Pin 36: Edge P20 I2C1:SDA
  * Edge GND (left of GND)
  * Edge GND (right of GND)

Additional components not programmed directly, but on the PCB
* SEGGER J-Link (firmware hosted on a Kinetis K22F 128 KB Flash Cortex M-4)
* Reset Button
* 512 kB Flash Memory (0.5 MB)
* USB Port for Drag & Drop Programming

## Notes:
* The HiFive1RevB is an Arduino style board with the same core processing (FE310, ESP32, Segger OB) but without the LED Matrix and other sensors on the HiFive Inventor board.  [HiFive1RevB](https://www.sifive.com/boards/hifive1-rev-b)  TBD: Pinout or the use of [SiFive Freedom Studio](https://www.sifive.com/software/sifive-freedom-studio)

* [YouTube Playlist (kind of random)](https://www.youtube.com/playlist?list=PLvZXTXiQDCe7YSpDQmd2ksVSHb431ns7F)
* Python stuff & firmware blobs [HiFive-PythonSandbox](https://github.com/damianburrin/HiFive-PythonSandbox/tree/main/h5%20updater-20240605T172322Z-001/h5%20updater/hifive_updater)


## Technical User Guide [Technical User Guide](HiFive_Inventor_Tech_UG_Web.pdf)

