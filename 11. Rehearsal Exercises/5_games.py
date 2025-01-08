import xml.etree.ElementTree as ET
import numpy as np
import matplotlib.pyplot as plt

def read_xml(filename):
    xmlDoc = ET.parse(filename)
    root = xmlDoc.getroot()

    output = []
    for element in root.iter('ROW'):
        child_list = [element[0].text, element[2].text]
        output.append(child_list)

    return output

def read_txt(textfile):
    loaded_data = np.genfromtxt(fname=textfile, delimiter=';', dtype='int', skip_header=1, filling_values=0)
    return loaded_data

users = read_xml('users.xml')
array = read_txt('games.csv')

rownumber = 0
i = 0

while i < len(array):
    zoekind = int(array[i][0])
    user = users[rownumber]
    tank = np.array([], dtype='int')
    damage = np.array([], dtype='int')
    support = np.array([], dtype='int')

    while i < len(array) and zoekind == int(array[i][0]):
        tank = np.append(tank, int(array[i][1]))
        damage = np.append(damage, int(array[i][2]))
        support = np.append(support, int(array[i][3]))
        i+=1
    rownumber += 1

    plt.figure(figsize=(10,3))
    plt.subplot(1,3,1)
    plt.plot(tank, 'r', label='Tank')
    plt.legend()
    plt.subplot(1,3,2)
    plt.plot(damage, 'b', label='Damage')
    plt.legend()
    plt.subplot(1,3,3)
    plt.plot(support, 'g', label='Support')
    plt.suptitle(user[1],weight='bold')
    plt.legend()
    plt.show()





