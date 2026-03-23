# 🎯 Valorant Task Protocol // Advanced OOP Manager

[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue)](https://www.python.org/)
[![UI Framework](https://img.shields.io/badge/UI-CustomTkinter-red)](https://github.com/TomSchimansky/CustomTkinter)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)

An advanced, game-themed Task Management System built with **Python** and **Object-Oriented Programming (OOP)** principles. This project features a modern UI inspired by the **Valorant** game interface.

---

## 🚀 Key Features
- **Modern UI/UX**: Dark-themed, responsive interface built with `CustomTkinter`.
- **Game-Inspired Design**: Sidebar navigation and "Mission Deployment" styling.
- **Data Persistence**: Automatic saving and loading of tasks using `JSON` database.
- **System Logging**: Track every action (Adding, Completing, Starting) with time-stamped logs.
- **Robust Architecture**: Built strictly on **OOP Principles** (Composition, Encapsulation, and Magic Methods).

---

## 🛠️ Tech Stack & Architecture
- **Language**: Python 3.10+
- **GUI Library**: CustomTkinter (Modern Tkinter wrapper)
- **Data Storage**: JSON (Local Persistence)
- **Design Pattern**: Composition (The App owns the Manager and Logger)

### Class Diagram (UML)
> *The system is designed with a clear separation of concerns:*
- `ValorantTaskApp`: The Orchestrator (UI/UX Layer).
- `TaskManager`: The Engine (Business Logic & Data Persistence).
- `Task` & `Category`: The Data Models.
- `HistoryLog`: The Audit Trail.

---

## 📸 Screenshots
*(Add your screenshots here after uploading them to GitHub)*
`![Main Dashboard](link-to-your-screenshot-1.png)`
`![Add Task View](link-to-your-screenshot-2.png)`

---

## 📥 Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/YOUR_USERNAME/Valorant-Task-Protocol.git](https://github.com/YOUR_USERNAME/Valorant-Task-Protocol.git)
   cd Valorant-Task-Protocol
