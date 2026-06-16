import os 

name="string"
names=['praveen','kaustuba','gokul']
for i in names:
    print(i)

for index,name in enumerate(names):
    print(index,name)

print(names[0])
print(names[0:2])
print(len(names))
names.append('aravind')
for i in names:
    print(i)

names.remove('aravind')
for i in names:
    print(i)

print('******************')
'''names.pop()
print(names)

names.pop()
print(names)'''

if 'aravind' in names:
    print('aravind is  here')
#print('aravind' in names)

if 'aravind' not in names:
    print('aravind is not  here')

cities=['chennai','chennai','chennai','canada','dubai']
cities_india=['mumbai','hyd','delhi']
print(cities.count('chennai'))
cities.extend(cities_india)
print(cities)

cities.clear()
print(cities)



print(os.getcwd())
print(os.listdir('.'))
print(os.listdir('./day07'))

for file in os.listdir('./day07'):
    if file.endswith('.md') or file.endswith('.csv'):
        print(file)


# what is the dif b/w json and dict
#

sample_json='{"name":"praven","age":"30"}'

print(sample_json)

sample_dict={'name': 'praven', 'age': '30'}