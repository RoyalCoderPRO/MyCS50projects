from pyfiglet import Figlet
import sys

x = input('Input: ')
if len(sys.argv) == 1:
    f = Figlet(font='big')
    print(f.renderText(x))
    if sys.argv[1] == '-f' or sys.argv[1] == '--font'