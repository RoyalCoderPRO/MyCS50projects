from pyfiglet import Figlet
import sys
figlet = Figlet()
x = input('Input: ')
try:
    if len(sys.argv) == 1:
        font_style = 'big'
    elif sys.argv[1] == '-f' or sys.argv[1] == '--font':
        font_style = sys.argv[2]
        assert font_style in figlet.getFonts()
except (ValueError, IndexError, NameError, AssertionError):
    sys.exit()

print('Output: ')
f = Figlet(font=font_style)
print(f.renderText(x))

Figlet