from back_end import *



# ==========================================
# 3. THE UI (Valorant Theme)
# ==========================================
class ValorantTaskApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("VALORANT PROTOCOL // Task Manager")
        self.geometry("950x600")
        
        # Valorant Colors
        self.VAL_RED = "#FF4655"      
        self.VAL_DARK = "#0F1923"     
        self.VAL_SURFACE = "#1F2326"  
        self.VAL_TEXT = "#ECE8E1"     

        ctk.set_appearance_mode("dark")
        self.configure(fg_color=self.VAL_DARK)

        self.manager = TaskManager()
        self.logger = HistoryLog()

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        self._build_sidebar()
        self._build_main_frame()
        self.show_add_task_view()

    def _build_sidebar(self):
        self.sidebar_frame = ctk.CTkFrame(self, width=220, corner_radius=0, fg_color=self.VAL_SURFACE)
        self.sidebar_frame.grid(row=0, column=0, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(6, weight=1)

        logo = ctk.CTkLabel(self.sidebar_frame, text="PROTOCOL\n// MENU", 
                            font=ctk.CTkFont(size=24, weight="bold"), text_color=self.VAL_RED)
        logo.grid(row=0, column=0, padx=20, pady=40)

        self._create_menu_btn("1. Add Task", self.show_add_task_view, 1)
        self._create_menu_btn("2. Show Tasks", self.show_tasks_view, 2)
        self._create_menu_btn("3. Mark Task as Done", self.show_mark_done_view, 3)
        self._create_menu_btn("4. Show History", self.show_history_view, 4)
        
        exit_btn = ctk.CTkButton(self.sidebar_frame, text="5. Exit", command=self.quit,
                                fg_color="transparent", border_width=2, border_color=self.VAL_RED,
                                text_color=self.VAL_RED, hover_color=self.VAL_RED)
        exit_btn.grid(row=6, column=0, padx=20, pady=20, sticky="s")

    def _create_menu_btn(self, text, cmd, row):
        btn = ctk.CTkButton(self.sidebar_frame, text=text, command=cmd, fg_color="transparent",
                            text_color=self.VAL_TEXT, hover_color=self.VAL_RED, anchor="w",
                            font=ctk.CTkFont(size=15, weight="bold"))
        btn.grid(row=row, column=0, padx=20, pady=10, sticky="ew")

    def _build_main_frame(self):
        self.main_frame = ctk.CTkFrame(self, corner_radius=15, fg_color=self.VAL_DARK)
        self.main_frame.grid(row=0, column=1, sticky="nsew", padx=30, pady=30)
        self.main_frame.grid_rowconfigure(1, weight=1)
        self.main_frame.grid_columnconfigure(0, weight=1)

    def clear_view(self):
        for widget in self.main_frame.winfo_children():
            widget.destroy()

    # --- VIEWS ---
    def show_add_task_view(self):
        self.clear_view()
        ctk.CTkLabel(self.main_frame, text="// ADD NEW TASK", font=ctk.CTkFont(size=30, weight="bold")).grid(row=0, pady=20)
        
        self.entry = ctk.CTkEntry(self.main_frame, placeholder_text="Task Title...", height=50, width=500, border_color=self.VAL_RED)
        self.entry.grid(row=1, pady=10)

        self.cat_var = ctk.StringVar(value="Personal")
        ctk.CTkOptionMenu(self.main_frame, values=["Personal", "Work", "Study"], variable=self.cat_var, fg_color=self.VAL_RED).grid(row=2, pady=10)

        ctk.CTkButton(self.main_frame, text="Add Task", command=self._add_action, height=50, fg_color=self.VAL_RED).grid(row=3, pady=40)

    def show_tasks_view(self):
        self.clear_view()
        ctk.CTkLabel(self.main_frame, text="// ALL TASKS", font=ctk.CTkFont(size=26, weight="bold")).pack(pady=10)
        
        scroll = ctk.CTkScrollableFrame(self.main_frame, fg_color=self.VAL_SURFACE)
        scroll.pack(fill="both", expand=True, padx=10, pady=10)

        for task in self.manager.tasks:
            color = "#4CAF50" if task.is_completed else self.VAL_TEXT
            ctk.CTkLabel(scroll, text=str(task), text_color=color, font=ctk.CTkFont(size=16)).pack(pady=5, anchor="w")

    def show_mark_done_view(self):
        self.clear_view()
        ctk.CTkLabel(self.main_frame, text="// MARK TASK AS DONE", font=ctk.CTkFont(size=26, weight="bold")).pack(pady=10)
        
        scroll = ctk.CTkScrollableFrame(self.main_frame, fg_color=self.VAL_SURFACE)
        scroll.pack(fill="both", expand=True, padx=10, pady=10)

        for i, task in enumerate(self.manager.tasks):
            if not task.is_completed:
                f = ctk.CTkFrame(scroll, fg_color="transparent")
                f.pack(fill="x", pady=5)
                ctk.CTkLabel(f, text=task.title, font=ctk.CTkFont(size=16)).pack(side="left", padx=10)
                ctk.CTkButton(f, text="Done", width=80, fg_color=self.VAL_RED, command=lambda idx=i: self._done_action(idx)).pack(side="right")

    def show_history_view(self):
        self.clear_view()
        txt = ctk.CTkTextbox(self.main_frame, fg_color=self.VAL_SURFACE, font=("Consolas", 14))
        txt.pack(fill="both", expand=True)
        txt.insert("0.0", "\n".join(self.logger.logs))
        txt.configure(state="disabled")

    # --- ACTIONS ---
    def _add_action(self):
        t = self.entry.get()
        if t:
            self.manager.add_task(Task(t, Category(self.cat_var.get())))
            self.logger.add_log(f"Added task: {t}")
            self.entry.delete(0, 'end')
            messagebox.showinfo("Success", "Task added and saved.")
        else:
            messagebox.showwarning("Error", "Please enter a title.")

    def _done_action(self, idx):
        self.manager[idx].mark_as_done()
        self.manager.save_data()
        self.logger.add_log(f"Completed: {self.manager[idx].title}")
        self.show_mark_done_view()

