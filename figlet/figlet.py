from pyfiglet import Figlet
import sys
figlet = Figlet()
try:
    if len(sys.argv) == 1:
        font_style = 'big'
    elif sys.argv[1] == '-f' or sys.argv[1] == '--font':
        font_style = sys.argv[2]
        assert font_style in figlet.getFonts()
    else:
        assert False
except (ValueError, IndexError, NameError, AssertionError):
    sys.exit('Invalid Usage')


x = input('Input: ')
print('Output: ')
f = Figlet(font=font_style)
print(f.renderText(x))
