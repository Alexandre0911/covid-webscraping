import requests
import bs4
from datetime import datetime

answer = 'y'

def UsCases():
    day_and_time = datetime.now()
    print()
    print('╔', '═'*30, ' United States ', '═'*30, '╗')
    usrequest = requests.get('https://www.worldometers.info/coronavirus/country/us/')
    ussoup = bs4.BeautifulSoup(usrequest.text, 'lxml')
    uscases = ussoup.select('title')

    with open('us.txt', 'a+') as file:
        file.write('{} >>> {}\n\n'.format(day_and_time, uscases[0].getText()))

    print('║', uscases[0].getText(), ' ║')
    print('╚', '═'*77, '╝', '\n')

def BrCases():
    day_and_time = datetime.now()
    print()
    print('╔', '═'*30, ' Brazil ', '═'*30, '╗')
    brrequest = requests.get('https://www.worldometers.info/coronavirus/country/brazil/')
    brsoup = bs4.BeautifulSoup(brrequest.text, 'lxml')
    brcases = brsoup.select('title')

    with open('br.txt', 'a+') as file:
        file.write('{} >>> {}\n\n'.format(day_and_time, brcases[0].getText()))

    print('║', brcases[0].getText(), '  ║')
    print('╚', '═'*70, '╝', '\n')

def PtCases():
    day_and_time = datetime.now()
    print()
    print('╔', '═'*30, ' Portugal ', '═'*30, '╗')
    ptrequest = requests.get('https://www.worldometers.info/coronavirus/country/portugal/')
    ptsoup = bs4.BeautifulSoup(ptrequest.text, 'lxml')
    ptcases = ptsoup.select('title')

    with open('pt.txt', 'a+') as file:
        file.write('{} >>> {}\n\n'.format(day_and_time, ptcases[0].getText()))

    print('║', ptcases[0].getText(), '      ║')
    print('╚', '═'*72, '╝', '\n')

while answer.lower() == 'y':
    UsCases()
    BrCases()
    PtCases()

    print('\nLisbon Time >>> {}'.format(datetime.now()))
    print('\n\n\n')

    answer = input('Refresh? [Y/N]: ')

    if answer != 'y' and answer != 'n':
        print('\nThe answer should be "Y" or "N" but, as the answer was none, the program will close.')
        answer = 'n'