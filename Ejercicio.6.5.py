
import tkinter as tk
from tkinter import ttk, messagebox


class Vendedor:
    def __init__(self, nombre, apellidos):
        self.nombre = nombre
        self.apellidos = apellidos
        self.edad = None

    def verificar_edad(self, edad):
        if edad < 0 or edad > 120:
            raise ValueError(
                "La edad no puede ser negativa ni mayor a 120."
            )

        if edad <= 18:
            raise ValueError(
                "El vendedor debe ser mayor de 18 años."
            )

        self.edad = edad

    def imprimir(self):
        return (
            f"Nombre del vendedor = {self.nombre}\n"
            f"Apellidos del vendedor = {self.apellidos}\n"
            f"Edad del vendedor = {self.edad}"
        )


class InterfazVendedor:
    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.title(
            "Ejercicio 6.5 - Lanzamiento de excepciones"
        )
        self.ventana.geometry("550x400")

        marco = ttk.Frame(ventana, padding=20)
        marco.pack(fill="both", expand=True)

        ttk.Label(
            marco,
            text="Registro de vendedor",
            font=("Arial", 16, "bold")
        ).pack(pady=10)

        ttk.Label(
            marco,
            text="Nombre del vendedor:"
        ).pack(anchor="w")

        self.nombre = ttk.Entry(marco)
        self.nombre.pack(fill="x", pady=5)

        ttk.Label(
            marco,
            text="Apellidos del vendedor:"
        ).pack(anchor="w")

        self.apellidos = ttk.Entry(marco)
        self.apellidos.pack(fill="x", pady=5)

        ttk.Label(
            marco,
            text="Edad del vendedor:"
        ).pack(anchor="w")

        self.edad = ttk.Entry(marco)
        self.edad.pack(fill="x", pady=5)

        ttk.Button(
            marco,
            text="Registrar vendedor",
            command=self.registrar_vendedor
        ).pack(pady=15)

        self.resultado = tk.StringVar()

        ttk.Label(
            marco,
            textvariable=self.resultado,
            justify="left",
            font=("Arial", 11)
        ).pack(anchor="w", pady=10)

    def registrar_vendedor(self):
        nombre = self.nombre.get().strip()
        apellidos = self.apellidos.get().strip()
        edad_texto = self.edad.get().strip()

        if not nombre or not apellidos or not edad_texto:
            messagebox.showerror(
                "Error",
                "Todos los campos son obligatorios."
            )
            return

        try:
            edad = int(edad_texto)

            vendedor = Vendedor(nombre, apellidos)
            vendedor.verificar_edad(edad)

            self.resultado.set(vendedor.imprimir())

            messagebox.showinfo(
                "Registro exitoso",
                "El vendedor fue registrado correctamente."
            )

        except ValueError as error:
            self.resultado.set("")
            messagebox.showerror(
                "Excepción",
                str(error)
            )


if __name__ == "__main__":
    raiz = tk.Tk()
    InterfazVendedor(raiz)
    raiz.mainloop()

