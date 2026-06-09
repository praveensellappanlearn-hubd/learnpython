file_name="day04.json"
data=open(file_name)
#open(file_name)
#print(data.read())

import pandas as ppp
file_name="day04.json"
data_new=ppp.read_json(file_name)


print(open(file_name).read())

condition_rows=data_new['salary']>10000
print(data_new[condition_rows])

print()
print(data_new[data_new['salary']>10000])
#print(open(file_name).read())

#singe line in all above prints
print(ppp.read_json(file_name)[ppp.read_json(file_name)['salary']>10000])