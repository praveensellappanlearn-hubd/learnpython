#Q1
def meth1():
    return 'praveen'

#q2:

def method2(a):
    print(a)


#Q3
def concat(a,b):
    return a+b

data3=concat('hello','world')
print(data3)

#q4:
def sumofnum(arr_num):
   # print(arr_num)
    total=0
    for i in arr_num:
        #print(i)
        total=total+i
    return total

arr_list=[1,2,3,4]  
data4=sumofnum(arr_list)  
print(data4)

#q5:

data_dic={'first_name':"praveen",'last_name':"kumar"}
def dictionarystring(data_dic):
    #print(data_dic['first_name'])
    name=data_dic['first_name']+' '+data_dic['last_name']
    data_dic['full_name']=name
    print(data_op)
    return name

data_op=dictionarystring(data_dic)
 
#reusing the older available method

data5 concat(data_dic)