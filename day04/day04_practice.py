
file_work='day04_practice.json' #assinging fileinto one variable
file_name_data=open(file_work) #storig the values of open  the file wit open method ,it shows the name detils of the file
print(open(file_work)) # printing the open method  ---> <_io.TextIOWrapper name='day04_practice.json' mode='r' encoding='cp1252'>
print(file_name_data.read())# read method used to read the file contents as like it is

import pandas as d  #panda is an external lib to data analysis
file_new='day04_practice.json'  #assinging fileinto one variable
file_data=d.read_json(file_new) #using pandas th file content will be read into table format from json
print(file_data) # printig the table format data

print(file_data['age']>23) #here we are filtering the file content with condition using [], o/p like true and false
file_condition_result=file_data['age']>23 #storing that values into one varibale

print(file_data[file_condition_result]) #here we are taking the filtered data of condition 

'''
xtra:
df = pd.read_json('data_lines.json', lines=True)'''
