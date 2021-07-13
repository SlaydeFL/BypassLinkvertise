from colored import fg, attr
import os
import requests
import json
import re
import string

def clean():
    os.system('cls')


print('\t\t\t%s ▄▄▄▄ ▓██   ██▓ ██▓███   ▄▄▄        ██████   ██████ ' % (fg(82)))
print('\t\t\t%s▓█████▄▒██  ██▒▓██░  ██▒▒████▄    ▒██    ▒ ▒██    ▒ ' % (fg(82)))
print('\t\t\t%s▒██▒ ▄██▒██ ██░▓██░ ██▓▒▒██  ▀█▄  ░ ▓██▄   ░ ▓██▄   ' % (fg(82)))
print('\t\t\t%s▒██░█▀  ░ ▐██▓░▒██▄█▓▒ ▒░██▄▄▄▄██   ▒   ██▒  ▒   ██▒' % (fg(82)))
print('\t\t\t%s░▓█  ▀█▓░ ██▒▓░▒██▒ ░  ░ ▓█   ▓██▒▒██████▒▒▒██████▒▒' % (fg(82)))
print('\t\t\t%s░▒▓███▀▒ ██▒▒▒ ▒▓▒░ ░  ░ ▒▒   ▓▒█░▒ ▒▓▒ ▒ ░▒ ▒▓▒ ▒ ░' % (fg(82)))
print('\t\t\t%s▒░▒   ░▓██ ░▒░ ░▒ ░       ▒   ▒▒ ░░ ░▒  ░ ░░ ░▒  ░ ░' % (fg(82)))
print('\t\t\t%s ░    ░▒ ▒ ░░  ░░         ░   ▒   ░  ░  ░  ░  ░  ░  ' % (fg(82)))
print('\t\t\t%s ░     ░ ░                    ░  ░      ░        ░  ' % (fg(82)))
print('\n\n%s                                                           by Slayde#1337' %(fg(82)))
print('')
print('')


url = "https://bypass.bot.nu/bypass2?url="

old_link = input('[%s+%s] %sEnter your link : %s' % (fg(93), attr('reset'), fg(93), attr('reset')))

re = url + old_link

os.system("cls")

r = requests.get(re)

link = r.json()['destination']

print('\t\t\t%s ▄▄▄▄ ▓██   ██▓ ██▓███   ▄▄▄        ██████   ██████ ' % (fg(82)))
print('\t\t\t%s▓█████▄▒██  ██▒▓██░  ██▒▒████▄    ▒██    ▒ ▒██    ▒ ' % (fg(82)))
print('\t\t\t%s▒██▒ ▄██▒██ ██░▓██░ ██▓▒▒██  ▀█▄  ░ ▓██▄   ░ ▓██▄   ' % (fg(82)))
print('\t\t\t%s▒██░█▀  ░ ▐██▓░▒██▄█▓▒ ▒░██▄▄▄▄██   ▒   ██▒  ▒   ██▒' % (fg(82)))
print('\t\t\t%s░▓█  ▀█▓░ ██▒▓░▒██▒ ░  ░ ▓█   ▓██▒▒██████▒▒▒██████▒▒' % (fg(82)))
print('\t\t\t%s░▒▓███▀▒ ██▒▒▒ ▒▓▒░ ░  ░ ▒▒   ▓▒█░▒ ▒▓▒ ▒ ░▒ ▒▓▒ ▒ ░' % (fg(82)))
print('\t\t\t%s▒░▒   ░▓██ ░▒░ ░▒ ░       ▒   ▒▒ ░░ ░▒  ░ ░░ ░▒  ░ ░' % (fg(82)))
print('\t\t\t%s ░    ░▒ ▒ ░░  ░░         ░   ▒   ░  ░  ░  ░  ░  ░  ' % (fg(82)))
print('\t\t\t%s ░     ░ ░                    ░  ░      ░        ░  ' % (fg(82)))
print('\n\n%s                                                           by Slayde#1337' %(fg(93)))
print('')
print('')

print('%s [+] Original link :' % (fg(82)), fg(93) + link)


def main():
    os.system('title Linkvertise Bypass - by Slayde // github.com/SlaydeFL')



main()