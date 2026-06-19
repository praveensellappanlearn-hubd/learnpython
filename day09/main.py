from fastapi import FastAPI
app=FastAPI()

@app.get('/')
def home():
    return "hello world to API"

@app.get("/user/{id}")
def get_user(id:int):
    users=[{'id':1,'name':'praveen','email':'p@gmail.com'},
    {'id':2,'name':'gogul','email':'g@gmail.com'}]
    for user in users:
        if user['id']==id:
            return user
        
value1=home()
print(value1)

value2=get_user(2)
print(value2)
