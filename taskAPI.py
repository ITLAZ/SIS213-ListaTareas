from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from models.task import Task

app = FastAPI()

origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:8080",
    "http://127.0.0.1:8000",
    "http://127.0.0.1:5500",
]


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

tareas = [
    { "id": 1, "title": "Tarea 1", "description": "Detalles de la tarea 1", "status": "Pendiente", "due_date": "01-01-2022" },
    { "id": 2, "title": "Tarea 2", "description": "Detalles de la tarea 2", "status": "Pendiente", "due_date": "01-01-2022" },
    { "id": 3, "title": "Tarea 3", "description": "Detalles de la tarea 3", "status": "Finalizada", "due_date": "01-01-2022" },
    { "id": 4, "title": "Tarea 4", "description": "Detalles de la tarea 4", "status": "En Progreso", "due_date": "01-01-2022" },  
    { "id": 5, "title": "Tarea 5", "description": "Detalles de la tarea 5", "status": "Finalizada", "due_date": "01-01-2022" },
    { "id": 6, "title": "Tarea 6", "description": "Detalles de la tarea 6", "status": "Pendiente", "due_date": "01-01-2022" },
]

@app.get("/tasks")
def get_tasks():
    return tareas

@app.post("/tasks")
def create_task(task: Task):
    tareas.append(task)
    return tareas

@app.put("/tasks/{id}")
def update_task(id: int, task: Task):
    for index, item in enumerate(tareas):
        if item["id"] == id:
            tareas[index] = task
            break
    else:
        return {"message": "Task not found"}
    return tareas

@app.delete("/tasks/{id}")
def delete_task(id: int):
    for index, item in enumerate(tareas):
        if item["id"] == id:
            tareas.pop(index)
            break
    else:
        return {"message": "Task not found"}
    return tareas

@app.get("/tasks/{id}")
def get_taskByID(id: int):
    return list(filter(lambda x: x["id"] == id, tareas))


@app.get("/tasks/status/{status}")
def get_tasks_by_status(status: str):
     filtered_tasks = [task for task in tareas if task["status"] == status] 
     return filtered_tasks