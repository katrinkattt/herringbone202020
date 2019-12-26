from time import sleep
from random import randint
from colorama import Fore, Style

txt1 = "Happy New Year"
txt2 = str(txt1)
base = len(txt1)
base += 1
while True:
    print('\033c')
    for x in range(1, base, 2):
        y = randint(2, 12)
        if x == 1:
            print(Style.BRIGHT+Fore.YELLOW+"{:^40}".format("\u2721"))
        elif y % 5 == 0:
            print(Fore.RED +"{:^40}".format(txt1[:x]))
        elif y % 3 == 0:
            print(Fore.GREEN + "{:^40}".format(txt1[:x]))
        else:
            
