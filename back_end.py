import customtkinter as ctk
from tkinter import messagebox
from datetime import datetime
import json
import os
# ==========================================
# 1. THE DATA MODELS
# ==========================================
class Category:
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return self.name

class Task:
    def __init__(self, title, category, is_completed=False):
        self.title = title
        self.category = category
        self.is_completed = is_completed

    def mark_as_done(self):
        self.is_completed = True

    def __str__(self):
        status = "✅ Done" if self.is_completed else "❌ Pending"
        return f"[{self.category}] {self.title} - {status}"

# ==========================================
# 2. THE ENGINE (Logic Layer)
# ==========================================
class TaskManager:
    def __init__(self):
        self.tasks = []
        self.db_file = "tasks_database.json"
        self.load_data()

    def add_task(self, task_obj):
        self.tasks.append(task_obj)
        self.save_data()

    def __len__(self):
        return len(self.tasks)

    def __getitem__(self, index):
        return self.tasks[index]

    def save_data(self):
        prepared_data = []
        for t in self.tasks:
            prepared_data.append({
                "title": t.title,
                "category": t.category.name,
                "is_completed": t.is_completed
            })
        with open(self.db_file, "w") as f:
            json.dump(prepared_data, f, indent=4)

    def load_data(self):
        if os.path.exists(self.db_file):
            try:
                with open(self.db_file, "r") as f:
                    raw_data = json.load(f)
                    for item in raw_data:
                        cat = Category(item["category"])
                        task = Task(item["title"], cat, item["is_completed"])
                        self.tasks.append(task)
            except:
                pass

class HistoryLog:
    def __init__(self):
        self.logs = []
    def add_log(self, action):
        now = datetime.now().strftime("%H:%M:%S")
        self.logs.append(f"[{now}] {action}")
