import random
import xml.etree.ElementTree as ET
def read_figures():
     figure_list=[]
     xmlDoc = ET.parse ("figures.xml")
     root = xmlDoc.getroot()
     for figure in root.iter('figure'):
         figure_list.append(figure[1].text+' '+ figure[0].text)

     print (*figure_list)
     return figure_list

def read_names():
    names = []
    with open('names.txt') as file:
        line = file.readline()
        while line:
            record = line.rstrip().split('/')
            random_number = random.randint(0,4)
            random_name = record[random_number]
            names.append(random_name)
            line = file.readline()
    names.sort()
    print('lengte :', len(names))
    print(*names)
    return names

figure_list = read_figures()
names_list = read_names()
print('A figure has been chosen for the following toddlers:')
for name in names_list:
     length = len(name)
     figure = figure_list [length-1]
     print(name,'\t',figure)




