import pandas as pd
import fuzzy

books = pd.read_csv("datasets/nytkids_yearly.xls", delimiter=';')

first_name = []
for name in books['Author']:
    first_name.append(name.split()[0])

books['first_name'] = first_name

firstname_nysiis = []
for firstname in books['first_name']:
    firstname_nysiis.append(fuzzy.nysiis(firstname))

books['firstname_nysiis'] = firstname_nysiis

babynames = pd.read_csv("datasets/babynames_nysiis.xls", delimiter=';')

gender = []
for f, m in zip(babynames['perc_female'], babynames['perc_male']):
    if f > m:
        gender.append('F')
    elif m > f:
        gender.append('M')
    else:
        gender.append('N')

babynames['gender'] = gender

def findInList(list, element):
    loc_in_list = list.index(element) if element in list else -1

    return loc_in_list

author_gender = []
for name in books['firstname_nysiis']:
    nloc = findInList(list(babynames['babynysiis']), name)
    
    if nloc == -1:
        author_gender.append('Unkown')
    else:
        author_gender.append(babynames['gender'][nloc])

books['author_gender'] = author_gender

print(books)