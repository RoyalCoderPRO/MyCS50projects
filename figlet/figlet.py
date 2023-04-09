from pyfiglet import Figlet
import sys

x = input('Input: ')
if len(sys.argv) == 1:
    f = Figlet(font='big')
    print(f.renderText(x))

try:
    if sys.argv[1] == '-f' or sys.argv[1] == '--font':
        font_style = sys.argv[2]

