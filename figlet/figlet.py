from pyfiglet import Figlet
import sys

x = input('Input: ')
if len(sys.argv) == 1:
    f = Figlet(font='slant')
    print(f.renderText(x))