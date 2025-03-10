import tkinter as tk
from tkinter import ttk

class VentanaTkinter(tk.Tk):   
    def __init__(self):
        super().__init__()
        self.title("Aplicaciones con Tkinter")
        self.geometry("400x400")
        self.resizable(False, True)
        tk.Label(self, text="¡Javier Bienvenido a Tkinter!", font=("Arial", 14)).pack(pady=20)
        botones_frame = tk.Frame(self)
        botones_frame.pack(pady=10)
        tk.Button(botones_frame, text="Aceptar", command=self.quit,width="20").pack(side="left", padx=10,pady=50)
        tk.Button(botones_frame, text="Cancelar", command=self.quit,width="20").pack(side="right", padx=10)
       


if __name__ == "__main__":
        app = VentanaTkinter()
        app.mainloop()



