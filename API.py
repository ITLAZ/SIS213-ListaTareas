from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from models.task import Task

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:8000",
    "http://localhost:3000",
    "http://localhost:8080",
    "http://localhost:5500",
    "http://localhost:5000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

tareas = []

@app.get("/tasks")
def get_tasks():
    return tareas

@app.post("/tasks")
def create_task(task: Task):
    tareas.append(task)
    return tareas

@app.put("/tasks/{task_id}")
def update_task(id: int, task: Task):
    for i, item in enumerate(tareas):
        if item[id] == id:
            tareas[i]["title"] = task.title
            tareas[i]["description"] = task.description
            tareas[i]["status"] = task.status
            tareas[i]["due_date"] = task.due_date
        else:
            return {"message": "Task not found"}
    return tareas

@app.delete("/tasks/{task_id}")
def delete_task(id: int):
    for i, item in enumerate(tareas):
        if item[id] == id:
            tareas.remove(i)
        else:
            return {"message": "Task not found"}
    return tareas

@app.get("/tasks/{task_id}")
def get_taskByID(id: int):
    return list(filter(lambda x: x["id"] == id, tareas))

@app.get("/tasks/{status}")
def get_taskByStatus(status: str):
    return list(filter(lambda x: x["status"] == status, tareas))