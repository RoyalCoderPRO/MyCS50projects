from pyfiglet import Figlet
import sys

x = input('Input: ')
if len(sys.argv) == 1:
    font_style = 'big'

try:
    if sys.argv[1] == '-f' or sys.argv[1] == '--font':
        font_style = sys.argv[2]
except (ValueError, IndexError):
    sys.exit()

f = Figlet(font=font_style)
print(f.renderText(x))

