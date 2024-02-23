from pydantic import BaseModel, Field
from typing import Optional
from datetime import date

class Task(BaseModel):
    id: Optional[int] = 0
    title: str = Field(default="Tarea Nueva", min_length=3, max_length=50)
    description: Optional[str] = Field(default="Detalles de la tarea", max_length=250)
    status: str = Field(default="Pendiente", max_length=20)
    created_at: Optional[str] = Field(default=date.today().strftime("%d-%m-%Y"))
    due_date: str = Field(default=date.today().strftime("%d-%m-%Y"))