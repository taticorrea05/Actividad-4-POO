
import tkinter as tk
from tkinter import ttk, messagebox


class Programador:
    def __init__(self, nombre, apellidos):
        self.nombre = nombre
        self.apellidos = apellidos


class EquipoMaratonProgramacion:
    def __init__(self, nombre_equipo, universidad, lenguaje):
        self.nombre_equipo = nombre_equipo
        self.universidad = universidad
        self.lenguaje_programacion = lenguaje
        self.programadores = []
        self.tamano_equipo = 0

    def esta_lleno(self):
        return self.tamano_equipo == 3

    @staticmethod
    def validar_campo(campo):
        if not campo:
            raise ValueError(
                "El campo no puede estar vacío."
            )

        if any(caracter.isdigit() for caracter in campo):
            raise ValueError(
                "El nombre no puede tener dígitos."
            )

        if len(campo) >= 20:
            raise ValueError(
                "La longitud debe ser menor a 20 caracteres."
            )

        if not all(
            caracter.isalpha() or caracter.isspace()
            for caracter in campo
        ):
            raise ValueError(
                "El campo solo debe contener letras."
            )

    def anadir_programador(self, programador):
        if self.esta_lleno():
            raise ValueError(
                "El equipo está completo. "
                "No se pudo agregar programador."
            )

        self.validar_campo(programador.nombre)
        self.validar_campo(programador.apellidos)

        self.programadores.append(programador)
        self.tamano_equipo += 1


class InterfazEquipo:
    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.title(
            "Ejercicio 6.7 - Validación de campos"
        )
        self.ventana.geometry("650x620")

        marco = ttk.Frame(ventana, padding=15)
        marco.pack(fill="both", expand=True)

        ttk.Label(
            marco,
            text="Equipo de Maratón de Programación",
            font=("Arial", 16, "bold")
        ).pack(pady=10)

        ttk.Label(
            marco,
            text="Nombre del equipo:"
        ).pack(anchor="w")

        self.nombre_equipo = ttk.Entry(marco)
        self.nombre_equipo.pack(fill="x", pady=4)

        ttk.Label(
            marco,
            text="Universidad:"
        ).pack(anchor="w")

        self.universidad = ttk.Entry(marco)
        self.universidad.pack(fill="x", pady=4)

        ttk.Label(
            marco,
            text="Lenguaje de programación:"
        ).pack(anchor="w")

        self.lenguaje = ttk.Entry(marco)
        self.lenguaje.pack(fill="x", pady=4)

        ttk.Button(
            marco,
            text="Crear equipo",
            command=self.crear_equipo
        ).pack(pady=10)

        ttk.Separator(
            marco,
            orient="horizontal"
        ).pack(fill="x", pady=10)

        ttk.Label(
            marco,
            text="Datos del integrante",
            font=("Arial", 13, "bold")
        ).pack(pady=5)

        ttk.Label(
            marco,
            text="Nombre:"
        ).pack(anchor="w")

        self.nombre = ttk.Entry(marco)
        self.nombre.pack(fill="x", pady=4)

        ttk.Label(
            marco,
            text="Apellidos:"
        ).pack(anchor="w")

        self.apellidos = ttk.Entry(marco)
        self.apellidos.pack(fill="x", pady=4)

        ttk.Button(
            marco,
            text="Añadir programador",
            command=self.agregar_programador
        ).pack(pady=10)

        self.resultado = tk.Text(
            marco,
            height=8,
            font=("Consolas", 10),
            state="disabled"
        )
        self.resultado.pack(
            fill="both", expand=True, pady=10
        )

        self.equipo = None

    def mostrar_resultado(self):
        if self.equipo is None:
            return

        texto = (
            f"Equipo: {self.equipo.nombre_equipo}\n"
            f"Universidad: {self.equipo.universidad}\n"
            f"Lenguaje: {self.equipo.lenguaje_programacion}\n"
            f"Integrantes: {self.equipo.tamano_equipo}/3\n\n"
        )

        for i, programador in enumerate(
            self.equipo.programadores, start=1
        ):
            texto += (
                f"{i}. {programador.nombre} "
                f"{programador.apellidos}\n"
            )

        self.resultado.configure(state="normal")
        self.resultado.delete("1.0", tk.END)
        self.resultado.insert(tk.END, texto)
        self.resultado.configure(state="disabled")

    def crear_equipo(self):
        nombre = self.nombre_equipo.get().strip()
        universidad = self.universidad.get().strip()
        lenguaje = self.lenguaje.get().strip()

        if not nombre or not universidad or not lenguaje:
            messagebox.showerror(
                "Error",
                "Todos los datos del equipo son obligatorios."
            )
            return

        self.equipo = EquipoMaratonProgramacion(
            nombre, universidad, lenguaje
        )

        self.mostrar_resultado()

        messagebox.showinfo(
            "Equipo creado",
            "El equipo fue creado correctamente."
        )

    def agregar_programador(self):
        if self.equipo is None:
            messagebox.showerror(
                "Error",
                "Primero debe crear el equipo."
            )
            return

        nombre = self.nombre.get().strip()
        apellidos = self.apellidos.get().strip()

        try:
            programador = Programador(
                nombre, apellidos
            )

            self.equipo.anadir_programador(
                programador
            )

            self.mostrar_resultado()

            self.nombre.delete(0, tk.END)
            self.apellidos.delete(0, tk.END)

            messagebox.showinfo(
                "Registro exitoso",
                "Programador agregado correctamente."
            )

        except ValueError as error:
            messagebox.showerror(
                "Excepción",
                str(error)
            )


if __name__ == "__main__":
    raiz = tk.Tk()
    InterfazEquipo(raiz)
    raiz.mainloop()
