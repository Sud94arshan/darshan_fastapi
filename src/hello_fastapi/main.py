
from fastapi import FastAPI
import uvicorn

app = FastAPI()

students = [{
    "userName":"Sudarshan",
    "rollNo": 1
},
{
    "class": 12,
    "company":"vwits"
}]

@app.get("/students")
def get_students():
    return students

@app.get("/addStudent")
def addStudent(userName:str,rollNo:str):
    global students
    students.append({"userName":userName,"rollNo":rollNo})
    return students

@app.get("/gettodos/{userName:str}/{rollNum:str}")
def getTodos(userName,rollNum):
    print("Get todos called",userName,rollNum)
    return userName,rollNum,"sud"

@app.post("/gettodos")
def getTodosPost():
    print("Get Post method todos called")
    return "post gettodos called"

@app.get("/")
def hello():
    return {"hello":"world"}
@app.get("/getSingleTodo")
def getSingleTodo(userName:str,rollNo:str,balance:int):
    print("Get todo called",userName,rollNo,balance)
    return userName,rollNo, balance

@app.put("/updateTodo")
def updateTodo():
    return "updateTodo called"

@app.get("/check")
def check():
    return "check kr liya "

def start():
    uvicorn.run("src.hello_fastapi.main:app",host="127.0.0.1",port = 8040,reload=True)