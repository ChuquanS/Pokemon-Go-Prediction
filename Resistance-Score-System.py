from sys import argv
import csv
script, combatFileName, pokemonFileName = argv
def g(name,ke,bei):
   global dic
   ke = ke.split(',')
   bei = bei.split(',')
   dic.setdefault(name,[]).append(ke)
   dic.setdefault(name,[]).append(bei)

def c12(a,b1,b2):
    global dic
    if b1 in dic[a][0]:
        if b2 in dic[a][1]:
            return 0
        else:
            return 1
    if b2 in dic[a][0]:
        if b1 in dic[a][1]:
            return 0
        else:
            return 1
    if b1 in dic[a][1]:
        if b2 in dic[a][0]:
            return 0
        else:
            return -1
    if b2 in dic[a][1]:
        if b1 in dic[a][0]:
            return 0
        else:
            return -1
    return 0

def compare(a1,b1,a2,b2):
    global dic
    sum1 = float(c12(a1,a2,b2) + c12(b1,a2,b2))/2
    sum2 = float(c12(a2,a1,b1) + c12(b2,a1,b1))/2   
    return [sum1,sum2]

dic = {}
g('Fighting','Normal,Rock,Steel,Ice,Dark','Rock,Bug,Dark')
g('Normal','','Rock,Ghost,Steel')
g('Flying','Fighting,Bug,Grass','Rock,Steel,Electric')
g('Poison','Grass,Fairy','Poison,Ground,Rock,Ghost,Steel')
g('Ground','Poison,Rock,Steel,Fire,Electric','Flying,Bug,Grass')
g('Rock','Flying,Bug,Fire,Ice',"Fighting,Ground,Steel")
g('Bug','Grass,Psychic,Dark','Fighting,Flying,Poison,Ghost,Steel,Fire,Fairy')
g('Ghost','Ghost,Psychic','Normal,Dark')
g('Steel','Rock,Ice,Fairy','Steel,Fire,Water,Electric')
g('Fire','Bug,Steel,Grass,Ice','Rock,Fire,Water,Dragon')
g('Water','Ground,Rock,Fire','Water,Grass,Dragon')
g('Grass','Ground,Rock,Water','Flying,Poison,Bug,Steel,Fire,Grass,Dragon')
g('Electric','Flying,Water','Ground,Grass,Electric,Dragon')
g('Psychic','Fighting,Poison','Steel,Psychic,Dark')
g('Ice','Flying,Ground,Grass,Dragon','Steel,Fire,Water,Ice')
g('Dragon','Dragon','Steel,Fairy')
g('Fairy','Fighting,Dragon,Dark','Poison,Steel,Fire')
g('Dark','Ghost,Psychic','Fighting,Dark,Fairy')
g('','','')

pokemonDic = {}
with open(pokemonFileName) as f:
    f = csv.reader(f)
    for row in f:
        pokemonDic.setdefault(row[0],[]).extend([row[2],row[3],row]) 

with open(combatFileName) as f:
    f = csv.reader(f)
    for row in f:
        if row[0] == 'First_pokemon':
            continue
        a1 = pokemonDic[row[0]][0]
        b1 = pokemonDic[row[0]][1]
        if b1 == '':
            b1 = a1
        a2 = pokemonDic[row[1]][0]
        b2 = pokemonDic[row[1]][1]
        if b2 == '':
            b2 = a2
        result = compare(a1,b1,a2,b2)
        for item in pokemonDic[row[0]][2]:
            print(item+'\t'),
        for item in pokemonDic[row[1]][2]:
            print(item+'\t'),
        if row[0] == row[2]:
            win = 'True'
        else:
            win = 'False'
        print(str(result[0])+'\t'+str(result[1])+'\t'+win)
