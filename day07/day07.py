

name='praveen'
name2='kumar'
print(type(name))
#age=25
#print(type(age))
print(name[-1])
print(name[-2])
print(name[0])
print(name[1:3])
print(name[3:-1])
print(name+name2)
print('*********')

print('*' *10)

for i in [1,2,3,4,5,6,7,8,9,10]:
    print(i*'*')

for i in range(0,10):
    print(i*'-')

print(len(name))

txt='this movie is not good'
print('good' in txt)

print(txt.upper())

print(txt.lower())

movies='good bad ugly,karuppu,blast'

print(movies.split(','))

for movies in movies.split(','):
    print(movies)

import requests as rq

def get_ltp(ISIN):
    ltp=rq.get('https://api.groww.in/v1/live-data/quote?exchange=NSE&segment=CASH&trading_symbol='+ISIN)
    print(ltp.json())

ISIN='TCS'
get_ltp(ISIN)