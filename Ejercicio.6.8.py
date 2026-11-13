
import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import io


class LeerArchivo:
    def __init__(self):
        self.nombre_archivo = ""

    def leer_archivo(self, ruta):
        try:
            contenido = []

            with open(ruta, "rb") as archivo:
                with io.TextIOWrapper(
                    archivo,
                    encoding="utf-8-sig"
                ) as lector:
                    for linea in lector:
                        contenido.append(linea)

            self.nombre_archivo = ruta
            return "".join(contenido)

        except (OSError, UnicodeError):
            raise ValueError(
                "No se pudo leer el archivo."
            )


class InterfazLeerArchivo:
    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.title(
            "Ejercicio 6.8 - Lectura de archivos"
        )
        self.ventana.geometry("650x450")

        self.lector = LeerArchivo()

        marco = ttk.Frame(ventana, padding=20)
        marco.pack(fill="both", expand=True)

        ttk.Label(
            marco,
            text="Lectura de archivos de texto",
            font=("Arial", 16, "bold")
        ).pack(pady=10)

        ttk.Label(
            marco,
            text="Seleccione un archivo .txt:"
        ).pack(anchor="w")

        self.ruta = tk.StringVar()

        ttk.Entry(
            marco,
            textvariable=self.ruta,
            state="readonly"
        ).pack(fill="x", pady=8)

        ttk.Button(
            marco,
            text="Seleccionar archivo",
            command=self.seleccionar_archivo
        ).pack(pady=5)

        ttk.Button(
            marco,
            text="Leer archivo",
            command=self.leer_archivo
        ).pack(pady=5)

        ttk.Label(
            marco,
            text="Contenido del archivo:"
        ).pack(anchor="w", pady=8)

        self.contenido = tk.Text(
            marco,
            height=12,
            font=("Consolas", 11),
            state="disabled"
        )
        self.contenido.pack(
            fill="both", expand=True
        )

    def seleccionar_archivo(self):
        archivo = filedialog.askopenfilename(
            title="Seleccionar archivo de texto",
            filetypes=[
                ("Archivos de texto", "*.txt"),
                ("Todos los archivos", "*.*")
            ]
        )

        if archivo:
            self.ruta.set(archivo)

            self.contenido.configure(state="normal")
            self.contenido.delete("1.0", tk.END)
            self.contenido.configure(state="disabled")

    def leer_archivo(self):
        ruta = self.ruta.get()

        if not ruta:
            messagebox.showerror(
                "Error",
                "Debe seleccionar un archivo."
            )
            return

        try:
            texto = self.lector.leer_archivo(ruta)

            self.contenido.configure(state="normal")
            self.contenido.delete("1.0", tk.END)
            self.contenido.insert(tk.END, texto)
            self.contenido.configure(state="disabled")

            messagebox.showinfo(
                "Lectura exitosa",
                "El archivo fue leído correctamente."
            )

        except ValueError as error:
            messagebox.showerror(
                "Excepción",
                str(error)
            )


if __name__ == "__main__":
    raiz = tk.Tk()
    InterfazLeerArchivo(raiz)
    raiz.mainloop()
