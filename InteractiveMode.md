# MicroPython Interactive Mode
After the FE310 firmware is updated with the to 2.0.69 micropython, try the following.
## Getting access to Interactive Mode
1. Open the HiFive Mu version
2. Press the REPL button in the top toolbar
3. At this point you should see something like:
```
MicroPython mp_v2-0-68_d2021-02-12-2-gc7228e7 on 2021-02-26; HiFiveIoT v2.0.69 with FE310.
Type "help()" for more information.
>>>
```
4. Of course typing `help()` will provide some good information.
5. I especially like the `display.scroll('Hello')` command, which just works!
6. The real magic is just pressing the `Tab` key from the `>>>` prompt
   * Typing any of the shown names (and sometimes '.') and pressing `Tab` again will show related functions.
8. This immediately shows the available hardware I/O that you can interact with.
   * pin0 ... pin20 : some support ADC in/out, most are digital in/out (see section below)
   * temperature() : default is Celsius for Farenheit `temperature() * 1.8 + 32` this is the CPU temp, so a little higher than room temp.
   * sleep() : is in milliseconds so 1000 per second ex. `sleep(2000)` is 2 seconds
   * reset() : just like pushing the reset button on the back of the board, also includes some technical details and the SiFive Logo in ASCII art.
   * running_time() : returns a counter value based on when the board was last powered on or reset. Divide by 1000 for the number of seconds.
   * panic() : 
## More involved I/O
### Buttons
* button_a.is_pressed()
* button_a.was_pressed()
* button_a.get_presses()
* button_b.is_pressed()
* button_b.was_pressed()
* button_b.get_presses()
### Compass
* compass.heading()
* compass.is_calibrated()
* compass.calibrate()
* compass.clear_calibration()
* compass.get_x()
* compass.get_y()
* compass.get_z()
* compass.get_field_strength()
### accelerometer
* accelerometer.get_x()
* accelerometer.get_y()
* accelerometer.get_z()
* accelerometer.get_values()
* accelerometer.current_gesture()
* accelerometer.is_gesture()
* accelerometer.was_gesture()
* accelerometer.get_gestures()
* Gestures
   * up
   * down
   * left
   * right
   * face up
   * face down
   * freefall
   * 3g
   * 6g
   * 8g
   * shake
### spi
* spi.init()
* spi.deinit()
* spi.write()
* spi.read()
* spi.write_readinto()
### i2c
* i2c.init()
* i2c.scan()
* i2c.read()
* i2c.write()
### Image
* Image.width()
* Image.height()
* Image.get_pixel()
* Image.set_pixel()
* Image.shift_left()
* Image.shift_right()
* Image.shift_up()
* Image.shift_down()
* Image.copy()
* Image.crop()
* Image.invert()
* Image.fill()
* Image.blit()
* Included Images
   * ALL_CLOCKS
   * ALL_ARROWS      
   * ANGRY
   * ARROW_E
   * ARROW_N
   * ARROW_NE
   * ARROW_NW
   * ARROW_S
   * ARROW_SE
   * ARROW_SW
   * ARROW_W
   * ASLEEP
   * BUTTERFLY
   * CHESSBOARD
   * CLOCK1
   * CLOCK2
   * CLOCK3
   * CLOCK4
   * CLOCK5
   * CLOCK6
   * CLOCK7
   * CLOCK8
   * CLOCK9
   * CLOCK10
   * CLOCK11
   * CLOCK12
   * CONFUSED
   * COW
   * DIAMOND
   * DIAMOND_SMALL
   * DUCK
   * GHOST
   * GIRAFFE
   * HAPPY
   * HEART
   * HEART_SMALL
   * HOUSE
   * FABULOUS
   * MEH
   * MUSIC_CROTCHET
   * MUSIC_QUAVER
   * MUSIC_QUAVERS
   * NO
   * PACMAN
   * PITCHFORK
   * RABBIT
   * ROLLERSKATE
   * SAD
   * SILLY
   * SKULL
   * SMILE
   * SNAKE
   * SQUARE
   * SQUARE_SMALL
   * STICKFIGURE
   * SURPRISED
   * SWORD
   * TARGET
   * TORTOISE
   * TRIANGLE_LEFT
   * TSHIRT
   * TYNKER
   * UMBRELLA
   * XMAS
   * YES
### display
* display.get_pixel()
* display.set_pixel()
* display.show()
* display.color()
* display.scroll()
* display.clear()
* display.on()
* display.off()
* display.is_on()
* display.read_light_level()
* display.read_ir_level()
## Not Displayed, but available
### uart
* uart.init()
* uart.any()
* uart.read()
* uart.readline()
* uart.readinto()
* uart.write()
* uart.on()
* uart.off()
* Init Values
   * ODD
   * EVEN
## Not Displayed, but these were documented, so could be in other MicroPython revisions, or otherwise hidden
### math
### music
### speech
### audio
### radio
### neopixel
### love
### authors()
### sys
### os
### random
## Troubleshooting
1. Only one app should connect to the device at a time so close other related apps.
   1. For example only Mu REPL OR the Firmware Updater.
2. If it's not connecting to any desktop applications, perform the Power Reset Sequence
   1. Unplug the device
   2. Hold the reset button on the back
   3. Plug it back in
   4. Release the reset button
4. The device should show as a 'HiFive' drive letter.
   1. If more than 2 files are present on the drive, then perform the board Power Reset Sequence in #2.
6. Close all related desktop apps. i.e. Mu, gui.exe (Updater)
7. Pressing the reset button is also very safe to try.

