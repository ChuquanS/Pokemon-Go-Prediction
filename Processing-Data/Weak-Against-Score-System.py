import csv
def single_score(typeA1,typeA2,typeB1,typeB2,dict):
    score1 = 0.0
    score2 = 0.0
    if typeA1 == '':
        typeA1 = typeA2
    else:
        typeA1 = typeA1
    if typeA2 == '':
        typeA2 = typeA1
    else:
        typeA2 = typeA2
    if typeB1 == '':
        typeB1 = typeB2
    else:
        typeB1 = typeB1
    if typeB2 == '':
        typeB2 = typeB1
    else:
        typeB2 = typeB2
    if typeB1 in against[typeA1]['StrongAgainst'].values():
        score1 += 1.0
        if typeB2 in against[typeA1]['StrongAgainst'].values():
            score1 += 1.0
        elif typeB2 in against[typeA1]['WeakAgainst'].values():
            score1 -= 1.0
        else:
            score1 = 0.0
    elif typeB1 in against[typeA1]['WeakAgainst'].values():
        score1 -= 1.0
        if (typeB2 in against[typeA1]['StrongAgainst'].values()):
            score1 += 1.0
        elif (typeB2 in against[typeA1]['WeakAgainst'].values()):
            score1 -= 1.0
        else:
            score1 = 0.0
    else:
        score1 = 0.0
    
    if typeB1 in against[typeA2]['StrongAgainst'].values():
        score2 += 1.0
        if typeB2 in against[typeA2]['StrongAgainst'].values():
            score2 += 1.0
        elif typeB2 in against[typeA2]['WeakAgainst'].values():
            score2 -= 1.0
        else:
            score2 = 0.0
    elif typeB1 in against[typeA2]['WeakAgainst'].values():
        score2 -= 1.0
        if (typeB2 in against[typeA2]['StrongAgainst'].values()):
            score2 += 1.0
        elif (typeB2 in against[typeA2]['WeakAgainst'].values()):
            score2 -= 1.0
        else:
            score2 = 0.0
    else:
        score2 = 0.0
    score = (score1 + score2)/4.0
    return score

against = {
    'Normal': 
    {
        'StrongAgainst': {},
        'WeakAgainst': {'a':'Rock','b':'Ghost','c':'Steel'}
    },
    'Fighting': 
    {
        'StrongAgainst': {'a':'Normal','b':'Rock','c':'Steel','d':'Ice','e':'Dark'},
        'WeakAgainst': {'a':'Flying','b':'Poison','c':'Psychic','d':'Bug','e':'Ghost','f':'Fairy'}
    },
    'Flying':
    {
        'StrongAgainst': {'a':'Fighting','b':'Bug','c':'Grass'},
        'WeakAgainst': {'a':'Rock','b':'Steel','c':'Electric'}
    },
    'Poison':
    {
        'StrongAgainst': {'a':'Grass','b':'Fairy'},
        'WeakAgainst': {'a':'Poison','b':'Ground','c':'Rock','d':'Ghost','e':'Steel'}
    },
    'Ground':
    {
        'StrongAgainst': {'a':'Poison','b':'Rock','c':'Steel','d':'Fire','e':'Electric'},
        'WeakAgainst': {'a':'Flying','b':'Bug','c':'Grass'}
    },
    'Rock':
    {
        'StrongAgainst': {'a':'Flying','b':'Bug','c':'Fire','d':'Ice'},
        'WeakAgainst': {'a':'Fighting','b':'Ground','c':'Steel'}
    },
    'Bug':
    {
        'StrongAgainst': {'a':'Grass','b':'Psychic','c':'Dark'},
        'WeakAgainst': {'a':'Fighting','b':'Flying','c':'Poison','d':'Ghost','e':'Steel','f':'Fire','g':'Fairy'}
    },
    'Ghost':
    {
        'StrongAgainst': {'a':'Ghost','b':'Psychic'},
        'WeakAgainst': {'a':'Normal','b':'Dark'}
    },
    'Steel':
    {
        'StrongAgainst': {'a':'Rock','b':'Ice','c':'Fairy'},
        'WeakAgainst': {'a':'Steel','b':'Fire','c':'Water','d':'Electric'}
    },
    'Fire':
    {
        'StrongAgainst': {'a':'Bug','b':'Steel','c':'Grass','d':'Ice'},
        'WeakAgainst': {'a':'Rock','b':'Fire','c':'Water','d':'Dragon'}
    },
    'Water':
    {
        'StrongAgainst': {'a':'Ground','b':'Rock','c':'Fire'},
        'WeakAgainst': {'a':'Water','b':'Grass','c':'Dragon'}
    },
    'Grass':
    {
        'StrongAgainst': {'a':'Ground','b':'Rock','c':'Water'},
        'WeakAgainst': {'a':'Flying','b':'Poison','c':'Bug','d':'Steel','e':'Fire','f':'Grass','g':'Dragon'}
    },
    'Electric':
    {
        'StrongAgainst': {'a':'Flying','b':'Water'},
        'WeakAgainst': {'a':'Ground','b':'Grass','c':'Electric','d':'Dragon'}
    },
    'Psychic':
    {
        'StrongAgainst': {'a':'Fighting','b':'Poison'},
        'WeakAgainst': {'a':'Steel','b':'Psychic','c':'Dark'}
    },
    'Ice':
    {
        'StrongAgainst': {'a':'Flying','b':'Ground','c':'Grass','d':'Dragon'},
        'WeakAgainst': {'a':'Steel','b':'Fire','c':'Water','d':'Ice'}
    },
    'Dragon':
    {
        'StrongAgainst': {'a':'Dragon'},
        'WeakAgainst': {'a':'Steel','b':'Fairy'}
    },
    'Fairy':
    {
        'StrongAgainst': {'a':'Fighting','b':'Dragon','c':'Dark'},
        'WeakAgainst': {'a':'Poison','b':'Steel','c':'Fire'}
    },
    'Dark':
    {
        'StrongAgainst': {'a':'Ghost','b':'Psychic'},
        'WeakAgainst': {'a':'Fighting','b':'Dark','c':'Fairy'}
    }
}


r_poke = csv.reader(file('pokemon.csv'))
r_comb = csv.reader(file('combats.csv'))
type_dict = {}
other_dict = {}
f = file('comb_type.txt','wb')
for row in r_poke:
    if row[0] == '#':
        continue
    if row[3] == '':
        row[3] = row[2]
    type_dict[row[0]] = [row[2],row[3]]
    other_dict[row[0]] = [row[4],row[5],row[6],row[7],row[8],row[9],row[10],row[11]]

for row1 in r_comb:
    if row1[0] in type_dict:
        f.writelines(row1[0]+'\t')
        for item in type_dict[row1[0]]:
            f.writelines(item+'\t')
        for item1 in other_dict[row1[0]]:
            f.writelines(item1+'\t') 
        if row1[1] in type_dict:
            f.writelines(row1[1]+' ')
            for item in type_dict[row1[1]]:
                f.writelines(item+'\t')
            for item1 in other_dict[row1[1]]:
                f.writelines(item1+'\t')
        A_B_score = single_score(type_dict[row1[0]][0],type_dict[row1[0]][1],type_dict[row1[1]][0],type_dict[row1[1]][1],against)
        B_A_score = single_score(type_dict[row1[1]][0],type_dict[row1[1]][1],type_dict[row1[0]][0],type_dict[row1[0]][1],against)
        f.writelines(row1[2]+'\t')  
        f.writelines(str(A_B_score)+'\t')
        f.writelines(str(B_A_score)+'\n')
