
from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/gettodos")
def getTodos():
    print("Get todos called")
    return "gettodos called"

@app.post("/gettodos")
def getTodosPost():
    print("Get Post method todos called")
    return "post gettodos called"

@app.get("/")
def hello():
    return "Hello Sudarshan"
@app.get("/getSingleTodo")
def getSingleTodo():
    print("Get todo called")
    return "getSingleTodo called"

@app.put("/updateTodo")
def updateTodo():
    return "updateTodo called"

@app.get("/check")
def check():
    retutn :"check kr liya bout reload"

def start():
    uvicorn.run("src.hello_fastapi.main:app",host="127.0.0.1",port = 8040,reload=True)