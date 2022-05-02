from pprint import pprint
import os
path = os.path.join(os.getcwd(), 'cook.txt')
with open(path) as file:
    result = {}
    for cook in file:
        name_cook = cook.strip()
        counter = int(file.readline().strip())
        reslut = []
        for item in range(counter):
            name, quantiti, sht = file.readline().split('|')
            reslut.append({'name': name.strip(), 'quantiti': int(quantiti.strip()), 'sht': sht.strip()})
        result[name_cook] = reslut
        file.readline()
pprint (result)



