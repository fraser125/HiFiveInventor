from hifive import uart, compass, sys

ABOUT = "HiFive Inventor MicroPython"
DOT = "."
CAL_CLEAR = "Calibration Cleared"
NEWLINE = r"\n"

try :
    uart.init()
    uart.write(ABOUT)
    compass.clear_calibration()
    uart.write(CAL_CLEAR)
    compass.calibrate()

    while not compass.is_calibrated() :
        uart.write(DOT)

    while True:
        uart.write(compass.heading())
        uart.write(NEWLINE)

except Exception as ex :
    sys.print_exception(ex)
