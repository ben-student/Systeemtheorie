from tabulate import tabulate as table
import os


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

loop = True

while loop:
    riskData = [[0, 'Kan nooit optreden'],
    [],
    [1, 'Héél erg kleine kans '],
    [],
    [2, 'Matige kans'],
    [],
    [3, 'Grote kans'],
    [],
    [4, 'Erg grote kans'],
    [],
    [5, 'Gedurende de levensduur van de applicatie zal de gebeurtenis quasi zeker minstens éénmaal plaatsvinden'],
    []]
    print(bcolors.HEADER + table(riskData, headers=['Risico', 'Betekenis']))

    print(bcolors.OKCYAN + "- - - - - - - - - - -")

    print(bcolors.OKGREEN + "What is the risk factor?")


    risk = int(input())


    impactData = [[0, 'Geen effect, ook niet op lange termijn, noch voor de eindgebruiker als de eigenaar van de applicatie'],
    [],
    [1, 'De impact voor de eindgebruiker is minimaal of van zeer korte duur óf de impact situeert zich achter '],
    ['-','de schermen en heeft bijvoorbeeld op langere termijn een invloed  op de herbruikbaarheid of de onderhoudbaarheid van de broncode'],
    [],
    [2, 'Een aantal functionaliteiten zijn tijdelijk niet beschikbaar voor de eindgebruiker'],
    [],
    [3, 'Een belangrijk deel van de functionaliteiten van de applicatie is (tijdelijk) niet beschikbaar'],
    [],
    [4, 'De meeste functionaliteit van de applicatie is verloren maar er is een mogelijkheid om een aantal problemen (tijdelijk) te overbruggen'],
    [],
    [5, 'Geen enkele functionaliteit van de applicatie is beschikbaar.'],
    []]
    print(bcolors.HEADER + table(impactData, headers=['Risico', 'Betekenis']))

    print(bcolors.OKCYAN + "- - - - - - - - - - -")

    print(bcolors.OKGREEN + "What is the impact factor?")



    impact = int(input())

    priority = round((1/5) * risk * impact)

    print(bcolors.WARNING + f"Priority is {priority}")

    

    print(bcolors.ENDC + "do you want to run again (Y/N) ?")

    again = input()
    os.system("clear")

    if again=='N':
        loop = False
        

    
