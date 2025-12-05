def avgsco(player):
    return sum(player['scores'])/len(player['scores'])

import datetime

def calage(player):
    curyear = datetime.datetime.now().year
    return curyear - player['BY']

Virat={
    'FName': 'Virat',
    'LName': 'Kohli',
    'BY': 1987,
    'scores': [],
    'Contry': 'India'
}

Virat['scores'].append(50)
Virat['scores'].append(75)
Virat['scores'].append(49)

print(avgsco(Virat))
print(calage(Virat))


David={
    'FName': 'David',
    'LName': 'Warne',
    'BY': 1982,
    'scores': [],
    'Contry': 'India'
}

David['scores'].append(47)
David['scores'].append(45)
David['scores'].append(20)

print(avgsco(David))
print(calage(David))
