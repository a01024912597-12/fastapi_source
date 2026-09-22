
from fastapi import APIRouter
from models.model import TodoItem, Todo
from fastapi import APIRouter, HTTPException, status

task_router = APIRouter(prefix="/tasks")

tasks = [
    { id: 0, "text": "Visit Kafka Museum", "done": True },
    { id: 1, "text": "Watch a puppet show", "done": False },
    { id: 2, "text": "Lennon Wall pic", "done": False },
]

