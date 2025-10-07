[https://www.sifive.com/boards/hifive1-rev-b](https://www.sifive.com/boards/hifive1-rev-b)  
[https://www.sifive.com/document-file/hifive1b-getting-started-guide](https://www.sifive.com/document-file/hifive1b-getting-started-guide)  
[https://www.sifive.com/document-file/freedom-e310-g002-manual](https://www.sifive.com/document-file/freedom-e310-g002-manual)  
[https://sifive.cdn.prismic.io/sifive/b9b9c901-d522-4ac4-99b9-fe585ade229d_FE310_G002_errata_20210408.pdf](https://sifive.cdn.prismic.io/sifive/b9b9c901-d522-4ac4-99b9-fe585ade229d_FE310_G002_errata_20210408.pdf)  
[https://www.sifive.com/document-file/freedom-e310-g002-datasheet](https://www.sifive.com/document-file/freedom-e310-g002-datasheet)  
[https://www.sifive.com/document-file/hifive1-rev-b-schematics](https://www.sifive.com/document-file/hifive1-rev-b-schematics)  
[https://www.sifive.com/software/sifive-freedom-studio](https://www.sifive.com/software/sifive-freedom-studio)  
[Platform IO](https://docs.platformio.org/en/latest/boards/sifive/hifive1-revb.html)  [Board Config](https://github.com/platformio/platform-sifive/tree/develop/boards)  
Lots of Forum Posts for HiFive1RevB  
[Category: HiFive1RevB](https://forums.sifive.com/c/hifive1/9)  
[Writing to SPI Flash](https://forums.sifive.com/t/writing-to-the-external-qspi-flash-memory/6401)  
[Boot Process](https://forums.sifive.com/t/fe310-g002-boot-process-entry-point/5839/3) and some [Additional Boot Process Notes](https://forums.sifive.com/t/is-there-c-boot-code-source-for-revb02-hardware/5987/2)

## Microcontroller  
* FE310-G002  
Operating Voltage  
* 3.3 V and 1.8 V  
Input Voltage  
* 5 V USB or 7-12 VDC Jack  
IO Voltages  
* Both 3.3 V  
Networking  
* WiFi/BT (off-chip)  
Weight  
* 22 g  
## Expansion Capabilities  
Digital I/O Pins: 19    
PWM Pins : 9   
SPI Controllers/HW CS Pins : 1/3  
UART : 2  
I2C : 1  
External Interrupt Pins : 19  
External Wakeup Pins : 1  
### Flash Memory  
* 32 Mbit Off-Chip (ISSI SPI Flash)

### Host Interface (microUSB)  
* Program, Debug, and Serial Communication

### Debug  
* Segger J-Link, drag/drop code download

[GitHub repo for the following webpages](https://github.com/iachievedit?tab=repositories&q=hifive)  
### IO [HiFive1 Rev B GPIO Pins](https://dev.iachieved.it/iachievedit/hifive1-rev-b-gpio-pins/)
Header Pins are ignored because that is part of the Arduino Shield header, not applicable to the HiFive Inventor board  

* GPIO  0 - Digital I/O
* GPIO  1 - PWM
* GPIO  2 - SPI - SS
* GPIO  3 - SPI - MOSI
* GPIO  4 - SPI - MISO
* GPIO  5 - SPI - SCK
* GPIO  8 - Digital I/O
* GPIO  9 - Digital I/O
* GPIO 10 - Digital I/O
* GPIO 11 - Digital I/O (Maybe PWM)
* GPIO 12 - I2C - SDA
* GPIO 13 - I2C - SCL
* GPIO 16 - Serial - RX
* GPIO 17 - Serial - TX
* GPIO 18 - Digital I/O
* GPIO 19 - RGB LED - Green (PWM) - LOW is ON
* GPIO 21 - RGB LED - Blue  (PWM) - LOW is ON
* GPIO 22 - RGB LED - Red   (PWM) - LOW is ON
* GPIO 23 - Digital I/O

[Exploring HiFive1 Rev B GPIOs with PlatformIO](https://dev.iachieved.it/iachievedit/exploring-hifive1-rev-b-gpios-with-platformio/)  
[I2C with the SiFive HiFive1 Rev B](https://dev.iachieved.it/iachievedit/i2c-with-the-sifive-hifive1-rev-b/) [hifive1_i2c_eeprom](https://github.com/iachievedit/hifive1_i2c_eeprom)  
[HiFive1 Rev B, Zephyr, and SPI](https://dev.iachieved.it/iachievedit/hifive1-rev-b-zephyr-and-spi/)  
