from pyfiglet import Figlet
import sys

x = input('Input: ')
try:

    if len(sys.argv) == 1:
        font_style = 'big'
    elif sys.argv[1] == '-f' or sys.argv[1] == '--font':
        font_style = sys.argv[2]
except (ValueError, IndexError, NameError):
    sys.exit()
print(Figlet.getFonts())
print('Output: ')
f = Figlet(font=font_style)
print(f.renderText(x))

