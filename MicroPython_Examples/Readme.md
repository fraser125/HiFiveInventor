# Example Code intended to Exercise the known MicroPython API

## Pins referenced are based on the micro:bit Edge connector

| Tested | Status   | Feature       | API Function Call      | Notes |
|---------|----------|---------------|------------------------|-------|
| - [ ]   | Untested | random        | .getrandbits(n)        |       |
| - [ ]   | Untested | random        | .seed(n)               |       |
| - [ ]   | Untested | random        | .randint(a,b)          |       |
| - [ ]   | Untested | random        | .randrange(stop)       |       |
| - [ ]   | Untested | random        | .choice(seq)           |       |
| - [ ]   | Untested | random        | .random(n)             |       |
| - [ ]   | Untested | random        | .uniform(n)            |       |
| - [ ]   | Untested | os            | .listdir()             |       |
| - [ ]   | Untested | os            | .remove(filename)      |       |
| - [ ]   | Untested | os            | .size(filename)        |       |
| - [ ]   | Untested | os            | .uname()               |       |
| - [ ]   | Untested | sys           | .version               |       |
| - [ ]   | Untested | sys           | .version_info          |       |
| - [ ]   | Untested | sys           | .implementation        |       |
| - [ ]   | Untested | sys           | .platform              |       |
| - [ ]   | Untested | sys           | .byteorder             |       |
| - [ ]   | Untested | hifive        | .panic()               |       |
| - [ ]   | Untested | hifive        | .sleep(time)           |       |
| - [ ]   | Untested | hifive        | .running_time()        |       |
| - [ ]   | Untested | hifive        | .temperature()         |       |
| - [ ]   | Untested | accelerometer | .get_x()               |       |
| - [ ]   | Untested | accelerometer | .get_y()               |       |
| - [ ]   | Untested | accelerometer | .get_z()               |       |
| - [ ]   | Untested | accelerometer | .is_gesture(name)      |       |
| - [ ]   | Untested | accelerometer | .was_gesure(name)      |       |
| - [ ]   | Untested | accelerometer | .get_gestures()        |       |
| - [ ]   | Untested | accelerometer | .get_values()          |       |
| - [ ]   | Untested | button_a     | .is_pressed()          |       |
| - [ ]   | Untested | button_a     | .was_pressed()         |       |
| - [ ]   | Untested | button_a     | .get_presses()         |       |
| - [ ]   | Untested | button_b     | .is_pressed()          |       |
| - [ ]   | Untested | button_b     | .was_pressed()         |       |
| - [ ]   | Untested | button_b     | .get_presses()         |       |
| - [ ]   | Untested | compass      | .is_calibrated()       |       |
| - [ ]   | Untested | compass      | .calibrate()           |       |
| - [ ]   | Untested | compass      | .clear_calibration()   |       |
| - [ ]   | Untested | compass      | .get_x()               |       |
| - [ ]   | Untested | compass      | .get_y()               |       |
| - [ ]   | Untested | compass      | .get_z()               |       |
| - [ ]   | Untested | compass      | .get_field_strength()  |       |
| - [ ]   | Untested | compass      | .heading()             |       |
| - [ ]   | Untested | display      | .show(x,delay,wait,loop,clear) |       |
| - [ ]   | Untested | display      | .scroll(string,delay,wait,loop,monspace) |       |
| - [ ]   | Untested | display      | .clear()               |       |
| - [ ]   | Untested | display      | .get_pixel(x,y)        |       |
| - [ ]   | Untested | display      | .set_pixel(x,y,b)      |       |
| - [ ]   | Untested | display      | .on()                  |       |
| - [ ]   | Untested | display      | .off()                 |       |
| - [ ]   | Untested | display      | .is_on()               |       |
| - [ ]   | Untested | Image        | Image()                |       |
| - [ ]   | Untested | Image        | .width()               |       |
| - [ ]   | Untested | Image        | .height()              |       |
| - [ ]   | Untested | Image        | .get_pixel(x,y)        |       |
| - [ ]   | Untested | Image        | .set_pixel(x,y,b)      |       |
| - [ ]   | Untested | Image        | .shift_left(n)         |       |
| - [ ]   | Untested | Image        | .shift_right(n)        |       |
| - [ ]   | Untested | Image        | .shift_up(n)           |       |
| - [ ]   | Untested | Image        | .shift_down(n)         |       |
| - [ ]   | Untested | Image        | .copy()                |       |
| - [ ]   | Untested | Image        | .crop(x1,y1,x2,y2)     |       |
| - [ ]   | Untested | Image        | .invert()              |       |
| - [ ]   | Untested | i2c          | .read()                |       |
| - [ ]   | Untested | i2c          | .write()               |       |
| - [ ]   | Untested | i2c          | .init()                |       |
| - [ ]   | Untested | uart         | .init(baudrate,bits,parity) |       |
| - [ ]   | Untested | uart         | .any()                 |       |
| - [ ]   | Untested | uart         | .read(n)               |       |
| - [ ]   | Untested | uart         | .readall()             |       |
| - [ ]   | Untested | uart         | .readline()            |       |
| - [ ]   | Untested | uart         | .readinto(buf,n)       |       |
| - [ ]   | Untested | uart         | .write()               |       |
| - [ ]   | Untested | spi          | .init(baudrate,bits,mode) |       |
| - [ ]   | Untested | spi          | .write(buf)            |       |
| - [ ]   | Untested | spi          | .read(n)               |       |
| - [ ]   | Untested | spi          | .write_readinto(out,in)|       |
| - [ ]   | Untested | music        | .set_tempo(number,bpm) |       |
| - [ ]   | Untested | music        | .pitch(freq,length,pin,wait)|       |
| - [ ]   | Untested | music        | .play(music,pin,wait,loop)|       |
| - [ ]   | Untested | music        | .get_tempo()           |       |
| - [ ]   | Untested | music        | .stop(pin)             |       |
| - [ ]   | Untested | music        | .reset()               |       |
| - [ ]   | Untested | this         | .authors()             |       |
| - [ ]   | Untested | love         | .badaboom()            |       |
| - [ ]   | Untested | neopixel     | .NeoPixel(pin,n)       |       |
| - [ ]   | Untested | neopixel     | .NeoPixel.clear()      |       |
| - [ ]   | Untested | neopixel     | .NeoPixel.show()       |       |
| - [ ]   | Untested | radio        | .on()                  |       |
| - [ ]   | Untested | radio        | .off()                 |       |
| - [ ]   | Untested | radio        | .config(length,queue,channel, power, address, group,data_rate)||
| - [ ]   | Untested | radio        | .reset()               |       |
| - [ ]   | Untested | radio        | .send_bytes(message)   |       |
| - [ ]   | Untested | radio        | .receive_bytes()       |       |
| - [ ]   | Untested | radio        | .send(message)         |       |
| - [ ]   | Untested | radio        | .receive()             |       |
| - [ ]   | Untested | audio        | .AudioFrame()          |       |
| - [ ]   | Untested | audio        | .receive()             |       |
| - [ ]   | Untested | speech       | .translate(words)      |       |
| - [ ]   | Untested | speech       | .say(words,pitch,speed,mouth,throat) |       |
| - [ ]   | Untested | speech       | .pronounce(phonemes,pitch,speed,mouth,throat) |       |
| - [ ]   | Untested | speech       | .sing(song,pitch,speed,mouth,throat) |       |
| - [ ]   | Untested | math         | .sqrt(x)               |       |
| - [ ]   | Untested | math         | .pow(x,y)              |       |
| - [ ]   | Untested | math         | .exp(x)                |       |
| - [ ]   | Untested | math         | .log(x,base)           |       |
| - [ ]   | Untested | math         | .cos(x)                |       |
| - [ ]   | Untested | math         | .sin(x)                |       |
| - [ ]   | Untested | math         | .tan(x)                |       |
| - [ ]   | Untested | math         | .acos(x)               |       |
| - [ ]   | Untested | math         | .asin(x)               |       |
| - [ ]   | Untested | math         | .atan(x)               |       |
| - [ ]   | Untested | math         | .atan2(x,y)            |       |
| - [ ]   | Untested | math         | .ceil(x)               |       |
| - [ ]   | Untested | math         | .copysign(x,y)         |       |
| - [ ]   | Untested | math         | .fabs(x)               |       |
| - [ ]   | Untested | math         | .floor(x)              |       |
| - [ ]   | Untested | math         | .fmod(x,y)             |       |
| - [ ]   | Untested | math         | .frexp(x)              |       |
| - [ ]   | Untested | math         | .ldexp(x,i)            |       |
| - [ ]   | Untested | math         | .modf(x)               |       |
| - [ ]   | Untested | math         | .isfinite(x)           |       |
| - [ ]   | Untested | math         | .isinf(x)              |       |
| - [ ]   | Untested | math         | .isnan(x)              |       |
| - [ ]   | Untested | math         | .trunc(x)              |       |
| - [ ]   | Untested | math         | .radians(x)            |       |
| - [ ]   | Untested | math         | .degrees(x)            |       |
| - [ ]   | Untested | pin0         | .is_touched()          |       |
| - [ ]   | Untested | pin0         | .read_digital()        |       |
| - [ ]   | Untested | pin0         | .write_digital(value)  |       |
| - [ ]   | Untested | pin0         | .read_analog()         |       |
| - [ ]   | Untested | pin0         | .write_analog(value)   |       |
| - [ ]   | Untested | pin0         | .set_analog_period(period) |           |
| - [ ]   | Untested | pin0         | .set_analog_period_microseconds(period) |       |
| - [ ]   | Untested | pin1         | .is_touched()          |               |
| - [ ]   | Untested | pin1         | .read_digital()        |               |
| - [ ]   | Untested | pin1         | .write_digital(value)  |               |
| - [ ]   | Untested | pin1         | .read_analog()         |               |
| - [ ]   | Untested | pin1         | .write_analog(value)   |               |
| - [ ]   | Untested | pin1         | .set_analog_period(period) |           |
| - [ ]   | Untested | pin1         | .set_analog_period_microseconds(period) |       |
| - [ ]   | Untested | pin2         | .is_touched()          |               |
| - [ ]   | Untested | pin2         | .read_digital()        |               |
| - [ ]   | Untested | pin2         | .write_digital(value)  |               |
| - [ ]   | Untested | pin2         | .read_analog()         |               |
| - [ ]   | Untested | pin2         | .write_analog(value)   |               |
| - [ ]   | Untested | pin2         | .set_analog_period(period) |           |
| - [ ]   | Untested | pin2         | .set_analog_period_microseconds(period) |       |
| - [ ]   | Untested | pin3         | .read_analog()         | Analog Only   |
| - [ ]   | Untested | pin3         | .write_analog(value)   |               |
| - [ ]   | Untested | pin3         | .set_analog_period(period) |           |
| - [ ]   | Untested | pin3         | .set_analog_period_microseconds(period) |       |
| - [ ]   | Untested | pin4         | .read_digital()        | No Touch      |
| - [ ]   | Untested | pin4         | .write_digital(value)  |               |
| - [ ]   | Untested | pin4         | .read_analog()         |               |
| - [ ]   | Untested | pin4         | .write_analog(value)   |               |
| - [ ]   | Untested | pin4         | .set_analog_period(period) |           |
| - [ ]   | Untested | pin4         | .set_analog_period_microseconds(period) |       |
| - [ ]   | Untested | pin5         | .read_digital()        | Digital Only  |
| - [ ]   | Untested | pin5         | .write_digital(value)  |               |
| - [ ]   | Untested | pin6         | .read_digital()        | Digital Only  |
| - [ ]   | Untested | pin6         | .write_digital(value)  |               |
| - [ ]   | Untested | pin7         | .read_digital()        | Digital Only  |
| - [ ]   | Untested | pin7         | .write_digital(value)  |               |
| - [ ]   | Untested | pin8         | .read_digital()        | Digital Only  |
| - [ ]   | Untested | pin8         | .write_digital(value)  |               |
| - [ ]   | Untested | pin9         | .read_digital()        | Digital Only  |
| - [ ]   | Untested | pin9         | .write_digital(value)  |               |
| - [ ]   | Untested | pin10        | .read_digital()        | No Touch      |
| - [ ]   | Untested | pin10        | .write_digital(value)  |               |
| - [ ]   | Untested | pin10        | .read_analog()         |               |
| - [ ]   | Untested | pin10        | .write_analog(value)   |               |
| - [ ]   | Untested | pin10        | .set_analog_period(period) |           |
| - [ ]   | Untested | pin10        | .set_analog_period_microseconds(period) |       |
| - [ ]   | Untested | pin11        | .read_digital()        | Digital Only |
| - [ ]   | Untested | pin11        | .write_digital(value)  |              |
|         |          | pin12        | NOTHING                |              |
| - [ ]   | Untested | pin13        | .read_digital()        | Digital Only |
| - [ ]   | Untested | pin13        | .write_digital(value)  |              |
| - [ ]   | Untested | pin14        | .read_digital()        | Digital Only |
| - [ ]   | Untested | pin14        | .write_digital(value)  |              |
| - [ ]   | Untested | pin15        | .read_digital()        | Digital Only |
| - [ ]   | Untested | pin15        | .write_digital(value)  |              |
| - [ ]   | Untested | pin16        | .read_digital()        | Digital Only |
| - [ ]   | Untested | pin16        | .write_digital(value)  |              |
|         |          | pin17        | NOTHING                |              |
|         |          | pin18        | NOTHING                |              |
| - [ ]   | Untested | pin19        | .read_digital()        | Digital Only |
| - [ ]   | Untested | pin19        | .write_digital(value)  |              |
| - [ ]   | Untested | pin20        | .read_digital()        | Digital Only |
| - [ ]   | Untested | pin20        | .write_digital(value)  |              |

| Radio Data Rates             | Notes |
|------------------------------|-------|
| radio.RATE_250KBIT           |       |
| radio.RATE_1MBIT             |       |
| radio.RATE_2MBIT             |       |   

| Image Name                    | Notes |
|-------------------------------|-------|
| hifive.Image.HEART            |       |
| hifive.Image.HEART_SMALL      |       |
| hifive.Image.HAPPY            |       |
| hifive.Image.SMILE            |       |
| hifive.Image.SAD              |       |
| hifive.Image.CONFUSED         |       |
| hifive.Image.ANGRY            |       |
| hifive.Image.ASLEEP           |       |
| hifive.Image.SURPRISED        |       |
| hifive.Image.SILLY            |       |
| hifive.Image.FABULOUS         |       |
| hifive.Image.MEH              |       |
| hifive.Image.YES              |       |
| hifive.Image.NO               |       |
| hifive.Image.CLOCK12          |       |
| hifive.Image.CLOCK11          |       |
| hifive.Image.CLOCK10          |       |
| hifive.Image.CLOCK9           |       |
| hifive.Image.CLOCK8           |       |
| hifive.Image.CLOCK7           |       |
| hifive.Image.CLOCK6           |       |
| hifive.Image.CLOCK5           |       |
| hifive.Image.CLOCK4           |       |
| hifive.Image.CLOCK3           |       |
| hifive.Image.CLOCK2           |       |
| hifive.Image.CLOCK1           |       |
| hifive.Image.ARROW_N          |       |
| hifive.Image.ARROW_NE         |       |
| hifive.Image.ARROW_E          |       |
| hifive.Image.ARROW_SE         |       |
| hifive.Image.ARROW_S          |       |
| hifive.Image.ARROW_SW         |       |
| hifive.Image.ARROW_W          |       |
| hifive.Image.ARROW_NW         |       |
| hifive.Image.TRIANGLE         |       |
| hifive.Image.TRIANGLE_LEFT    |       |
| hifive.Image.CHESSBOARD       |       |
| hifive.Image.DIAMOND          |       |
| hifive.Image.DIAMOND_SMALL    |       |
| hifive.Image.SQUARE           |       |
| hifive.Image.SQUARE_SMALL     |       |
| hifive.Image.RABBIT           |       |
| hifive.Image.COW              |       |
| hifive.Image.MUSIC_CROTCHET   |       |
| hifive.Image.MUSIC_QUAVER     |       |
| hifive.Image.MUSIC_QUAVERS    |       |
| hifive.Image.PITCHFORK        |       |
| hifive.Image.XMAS             |       |
| hifive.Image.PACMAN           |       |
| hifive.Image.TARGET           |       |
| hifive.Image.TSHIRT           |       |
| hifive.Image.ROLLERSKATE      |       |
| hifive.Image.DUCK             |       |
| hifive.Image.HOUSE            |       |
| hifive.Image.TORTOISE         |       |
| hifive.Image.BUTTERFLY        |       |
| hifive.Image.STICKFIGURE      |       |
| hifive.Image.GHOST            |       |
| hifive.Image.SWORD            |       |
| hifive.Image.GIRAFFE          |       |
| hifive.Image.SKULL            |       |
| hifive.Image.UMBRELLA         |       |
| hifive.Image.SNAKE            |       |
| hifive.Image.ALL_CLOCKS       |       |
| hifive.Image.ALL_ARROWS       |       |

| Song Name         | Notes         |
|-------------------|---------------|
| music.DADADADUM   |               |
| music.ENTERTAINER |               |
| music.PRELUDE     |               |
| music.ODE         |               |
| music.NYAN        |               |
| music.RINGTONE    |               |
| music.FUNK        |               |
| music.BLUES       |               |
| music.BIRTHDAY    |               |
| music.WEDDING     |               |
| music.FUNERAL     |               |
| music.PUNCHLINE   |               |
| music.PYTHON      |               |
| music.BADDY       |               |
| music.CHASE       |               |
| music.BA_DING     |               |
| music.WAWAWAWAA   |               |
| music.JUMP_UP     |               |
| music.JUMP_DOWN   |               |
| music.POWER_UP    |               |
| music.POWER_DOWN  |               |
| antigravity       | No prefix?    |

# Statuses
## Untested
Add it to the list, no work has been done.
## Coded
Code has been written to at least test that the function exists.
## Pass
If it can be called and responds, this doesn't mean it's fully functional. More that it's less likely to break your program.
## Fail
This is a broken API, that may never work, but may also simply require different parameters than were used. 