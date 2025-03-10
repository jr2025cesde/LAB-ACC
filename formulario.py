import tkinter as tk
from tkinter import ttk

class VentanaTkinter(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Aplicación con Tkinter")
        self.geometry("400x500")

        # Establecer el color de fondo de la ventana principal a celeste
        self.config(bg="#87CEEB")  # Color celeste

        # ─────────────────────── CREACIÓN DE WIDGETS ───────────────────────
        
        # Etiqueta
        tk.Label(self, text="Nombre:", font=("Algerian", 12), bg="#87CEEB").pack(pady=5)

        # Entrada de texto
        self.entrada = tk.Entry(self, width=30)
        self.entrada.pack(pady=5)

        # Botón
        tk.Button(self, text="Mostrar", command=self.mostrar_texto).pack(pady=5)
    

        # Área de texto
        self.texto = tk.Text(self, height=4, width=40)
        self.texto.pack(pady=5)

        # Casilla de verificación
        self.var_check = tk.BooleanVar()
        self.check = tk.Checkbutton(self, text="Aceptar términos", variable=self.var_check, bg="#87CEEB")
        self.check.pack(pady=5)

        # RadioButton
        self.var_radio = tk.StringVar(value="Opción 1")
        tk.Radiobutton(self, text="Opción 1", variable=self.var_radio, value="Opción 1", bg="#87CEEB").pack()
        tk.Radiobutton(self, text="Opción 2", variable=self.var_radio, value="Opción 2", bg="#87CEEB").pack()

        # Lista desplegable
        self.combo = ttk.Combobox(self, values=["Python", "Java", "C++", "JavaScript", "C#", "html"])
        self.combo.pack(pady=5)
        self.combo.set("Selecciona un lenguaje")

        # ───────────────────── MINI FORMULARIO DE INICIO DE SESIÓN ─────────────────────

        tk.Label(self, text="Inicio de Sesión", font=("Arial", 14, "bold"), bg="#87CEEB").pack(pady=10)
        tk.Label(self, text="Usuario:", bg="#87CEEB").pack()
        self.usuario = tk.Entry(self, width=30)
        self.usuario.pack()

        tk.Label(self, text="Contraseña:", bg="#87CEEB").pack()
        self.contraseña = tk.Entry(self, width=30, show="*")
        self.contraseña.pack()

        tk.Button(self, text="Iniciar Sesión", command=self.iniciar_sesion).pack(pady=10)

    def mostrar_texto(self):
        self.texto.insert(tk.END, f"Hola, {self.entrada.get()}!\n")

    def iniciar_sesion(self):
        usuario = self.usuario.get()
        contraseña = self.contraseña.get()
        print(f"Usuario: {usuario}, Contraseña: {contraseña}")

if __name__ == "__main__":
    app = VentanaTkinter()
    app.mainloop()





