import time
import board
import microcontroller
from digitalio import DigitalInOut, Direction, Pull
# import busio if board.UART() is not available
#import busio
import serial_lcd_kit

lcd = serial_lcd_kit.SerialLCDKit(board.UART())
# if the above doesn't work, or if you need to use a secondary UART, use busio
#uart = busio.UART(board.TX, board.RX, baudrate=9600)
#lcd = serial_lcd_kit.SerialLCDKit(uart)

#switch = DigitalInOut(board.D9)
#switch.direction = Direction.INPUT
#switch.pull = Pull.UP

lcd.set_backlight_pct(30)
lcd.clear_display()
time.sleep(1)
lcd.write("Hello from...")
time.sleep(1)
lcd.line_feed()
lcd.write("Circuit Python")
time.sleep(1)
lcd.clear_display()

#lcd.set_cursor_at(1)
#lcd.write("Switch:")
lcd.set_cursor_at(16)
lcd.write("CPU Temp:")
          
while True:
#  lcd.set_cursor_at(9)
#  lcd.write(str(switch.value))
  lcd.set_cursor_at(26)
  lcd.write(str(microcontroller.cpu.temperature) + " C")
  time.sleep(1)
