# Learning How to Learn #
This is the real secret to making this device work, experiment on every boot over the serial port the following quote is displayed ...
```
The Zen of MicroPython, by Nicholas H. Tollervey

Code,
Hack it,
Less is more,
Keep it simple,
Small is beautiful,

Be brave! Break things! Learn and have fun!
Express yourself with MicroPython.

Happy hacking! :-)
```
1. The REPL console is your friend to trying things quickly and easily.
2. The unit itself will provide most of your error messages, in full sentences, one letter at a time on the LED display.
3. It's very easy to leave a connection open, either a terminal or the firmware updater open and not be able to program the unit.
# Getting Started Writing code #
Using the [Mu Editor](https://github.com/fraser125/HiFiveInventor/blob/main/Mu4Hi5/mu-editorA2_64bit.exe)
1. Create a "New" source file if one isn't already open.   
2. Line 1 (unless you type comments at the top) will be: `from hifive import *`  
3. The next line will be `import blah` but now we need to figure out what 'blah' is.
4. Switch back over to REPL mode and type `help('modules')` then press enter.
5. From the list presented, rerun the help command with the module name for more details `help('sys')`
# [MicroPython Documentation](https://docs.micropython.org/en/latest/library/index.html#python-standard-libraries-and-micro-libraries)
* [MicroPython Documentation](https://docs.micropython.org/en/latest/library/index.html#python-standard-libraries-and-micro-libraries)
* More "advice" than documentation but more is generally better 
# Results of `help('modules')` in REPL interactive command line.
## __main__
## antigravity
Note: Displays some ASCII art, it's the first frame of an xkcd comic  
* `import antigravity` triggers the following in the REPL console
```
+-xkcd.com/353---------------------------------------------------+
|                                                                |
|                                                    \0/         |
|                                                  /   \         |
|        You're flying!                  MicroPython!  /|        |
|            How?                                      \ \       |
|            /                                                   |
|          0                                                     |
|         /|\                                                    |
|          |                                                     |
|-----____/_\______________________________----------------------|
|                                                                |
+----------------------------------------------------------------+
```
* [xkcd.com/353](https://xkcd.com/353)
## array
## audio
* audio.AudioFrame()
  * Represents a list of 32 samples each of which is a signed byte. It takes just over 4ms to play a single frame.
* audio.play(source, wait=True, pins=(pin0, pin1))
  * Play the source to completion where 'source' is an iterable, each element of which must be an AudioFrame instance.
## builtins
## collections
## esp32
## gc
## hifive
## love
Note: I believe this requires the speaker module to be attached
* love.badaboom()
  * Hear my soul speak: The very instant that I saw you, did My heart fly to your service.
## machine
## math
* math.acos(x)
  * Return the arc cosine of 'x', in radians.
* math.asin(x)
  * Return the arc sine of 'x', in radians.
* math.atan(x)
  * Return the arc tangent of 'x', in radians.
* math.atan2(x, y)
  * Return atan(y / x), in radians.
* math.ceil(x)
  * Return the ceiling of 'x', the smallest integer greater than or equal to 'x'.
* math.copysign(x, y)
  * Return a float with the magnitude (absolute value) of 'x' but the sign of 'y'.
* math.cos(x)
  * Return the cosine of 'x' radians.
* math.degrees(x)
  * Convert angle 'x' from radians to degrees.
* math.exp(x)
  * Return math.e**'x'.
* math.fabs(x)
  * Return the absolute value of 'x'.
* math.floor(x)
  * Return the floor of 'x', the largest integer less than or equal to 'x'.
* math.fmod(x, y)
  * Return 'x' modulo 'y'.
* math.frexp(x)
  * Return the mantissa and exponent of 'x' as the pair (m, e).
* math.isinf(x)
  * Return True if 'x' is a positive or negative infinity, and False otherwise.
* math.isfinite(x)
  * Return True if 'x' is neither an infinity nor a NaN, and False otherwise.
* math.isnan(x)
  * Return True if 'x' is a NaN (not a number), and False otherwise.
* math.ldexp(x, i)
  * Return 'x' * (2**'i').
* math.log(x, base=math.e)
  * With one argument, return the natural logarithm of 'x' (to base e). With two arguments, return the logarithm of 'x' to the given 'base'.
* math.modf(x)
  * Return the fractional and integer parts of x. Both results carry the sign of x and are floats.
* math.pow(x, y)
  * Return 'x' raised to the power 'y'.
* math.radians(x)
  * Convert angle 'x' from degrees to radians.
* math.sin(x)
  * Return the sine of 'x' radians.
* math.sqrt(x)
  * Return the square root of 'x'.
* math.tan(x)
  * Return the tangent of 'x' radians.
* math.trunc(x)
  * Return the Real value 'x' truncated to an Integral (usually an integer).
## microbit
## micropython
## mqtt
## music
## neopixel
* neopixel.NeoPixel(pin, n)
 * Create a list representing a strip of 'n' neopixels controlled from the\nspecified pin (e.g. hifive.pin0). Use the resulting object to change each pixel by position (starting from 0). Individual pixels are given RGB (red, green, blue) values between 0-255 as a tupe. For example, (255, 255, 255) is white:
 * ```
   np = neopixel.NeoPixel(hifive.pin0, 8)
   np[0] = (255, 0, 128)
   np.show()```
* neopixel.NeoPixel.clear()
  * Clear all the pixels.
* neopixel.NeoPixel.show()
  * Show the pixels. Must be called for any updates to become visible.
## network
## os
* os.listdir()
  * Return a list of the names of all the files contained within the local\non-device file system.
* os.remove(filename)
  * Remove (delete) the file named filename.
* os.size(filename)
  * Return the size, in bytes, of the file named filename.
* os.uname()
  * Return information about MicroPython and the device.
## radio
* radio.config(length=32, queue=3, channel=7, power=0, address=0x75626974, group=0, data_rate=radio.RATE_1MBIT)
  * Configures the various settings relating to the radio. The specified default values are sensible. 'length' is the maximum length, in bytes, of a message. It can be up to 251 bytes long. 'queue' is the number of messages to store on the message queue. 'channel' (0-100) defines the channel to which the radio is tuned. 'address' is an arbitrary 32-bit address that's used to filter packets. 'group' is an 8-bit value used with 'address' when filtering packets. 'data_rate' is the throughput speed. It can be one of: radio.RATE_250KbIT, radio.RATE_1MbIT (the default) or radio.2MBIT.
* radio.on()
  * Turns on the radio. This needs to be called since the radio draws power and\ntakes up memory that you may otherwise need.
* radio.off()
  * Turns off the radio, thus saving power and memory.
* radio.receive()
  * eceive the next incoming message from the message queue as a string. Returns 'None' if there are no pending messages.
* radio.receive_bytes()
  * Receive the next incoming message from the message queue. Returns 'None' if\nthere are no pending messages. Messages are returned as bytes.
* radio.reset()
  * Reset the settings to their default value.
* radio.send(message)
  * Send a message string.
* radio.send_bytes(message)
  * Sends a message containing bytes.
* 
## random
The following import statements may be needed to test the 'random' API's
```
import hifive
import random
```
* random.getrandbits(n)
  * Return an integer with n random bits.
  * `random.getrandbits(16)`  
* random.seed(n)
  * Initialise the random number generator with a known integer 'n'.
  * `random.seed(hifive.running_time())`
* random.randint(a,b)
  * Return a random whole number between a and b (inclusive).
  * `rnd = random.randint(1, 6)` # Dice Roll
* random.randrange(stop)
  * Return a random whole number between 0 and up to (but not including) stop.
  * `random.randrange(24)` 
* random.choice(seq)
  * Return a randomly selected element from a sequence of objects (such as a list).
* random.random()
  * Return a random floating point number between 0.0 and 1.0.
* random.uniform(a, b)
  * Return a random floating point number between a and b (inclusive).
## speech
* speech.pronounce(phonemes, pitch=64, speed=72, mouth=128, throat=128)
  * Pronounce the phonemes in the string 'phonemes'. Override the optional pitch, speed, mouth and throat settings to change the tone of voice.
* speech.say(words, pitch=64, speed=72, mouth=128, throat=128)
  * Say the English words in the string 'words'. Override the optional pitch, speed, mouth and throat settings to change the tone of voice.
* speech.sing(song, pitch=64, speed=72, mouth=128, throat=128)
  * Sing the phonemes in the string 'song'. Add pitch information to a phoneme with a hash followed by a number between 1-255 like this: '#112DOWWWWWWWW'. Override the optional pitch, speed, mouth and throat settings to change the tone of voice.
* speech.translate(words)
  * Return a string containing the phonemes for the English words in the string 'words'.
## struct
## sys
Notes: If shown without parentheses, then none are needed.  
No documentation available, so returened values are shown. Not likely to change.
* sys.version 
  * returns `'3.4.0'`
* sys.version_info
  * returns `(3, 4, 0)`
* sys.implementation
  * returns `(name='micropython', version=(0, 0, 1))`
* sys.platform
  * returns `'hifive'`
* sys.byteorder
  * returns `'little'`
* sys.print_exception(ex)
  * Print to the REPL information about the exception 'ex'.
  * ```
    try :
    // Code
    except Exception as ex :
      sys.print_exception(ex)
    ```
## this
Note: Not really useful, but interesting enought to include here
* this.authors()
  * returns `MicroPython on the HiFive IoT is brought to you by: SiFive, Damien P. George, Miodrag Milanovic ...`
## time
## uart
Note: I was unable to get uarts to work as expected. 
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
## ubluetooth
## ucollections
## usocket
## ustruct
## utime



