import csv
from colorama import Fore, Style, init
from sys import argv
from itertools import cycle

init()

with open(argv[1]) as csvfile:
    file = csv.reader(csvfile)
    header = True
    for row in file:
        if header == True:
            for text, color in zip(row, cycle([Fore.RED, Fore.YELLOW, Fore.GREEN, Fore.CYAN, Fore.BLUE, Fore.MAGENTA])):
                print(color + text, end='')
                for x in range(len(text), 20): print(' ', end='')
            print(Style.RESET_ALL)
            header = False
        else:
            for text in row:
                print(text, end='')
                for x in range(len(text), 20): print(' ', end='')
            print("")