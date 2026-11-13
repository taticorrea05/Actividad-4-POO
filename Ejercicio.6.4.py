
import tkinter as tk
from tkinter import scrolledtext


class PruebaExcepciones:
    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.title("Ejercicio 6.4 - Excepciones")
        self.ventana.geometry("620x380")

        tk.Label(
            ventana,
            text="Demostración de try, except y finally",
            font=("Arial", 15, "bold")
        ).pack(pady=12)

        self.salida = scrolledtext.ScrolledText(
            ventana, width=70, height=14,
            font=("Consolas", 11), state="disabled"
        )
        self.salida.pack(
            padx=12, pady=8, fill="both", expand=True
        )

        tk.Button(
            ventana,
            text="Ejecutar excepciones",
            command=self.ejecutar_ejemplo
        ).pack(pady=12)

    @staticmethod
    def obtener_mensajes():
        mensajes = []

        try:
            mensajes.append("Ingresando al primer try")
            cociente = 10000 / 0
            mensajes.append(f"Después de la división: {cociente}")
        except ZeroDivisionError:
            mensajes.append("División por cero")
        finally:
            mensajes.append("Ingresando al primer finally")

        try:
            mensajes.append("Ingresando al segundo try")
            objeto = None
            objeto.toString()
            mensajes.append("Imprimiendo objeto")
        except ZeroDivisionError:
            mensajes.append("División por cero")
        except Exception:
            mensajes.append("Ocurrió una excepción")
        finally:
            mensajes.append("Ingresando al segundo finally")

        return mensajes

    def ejecutar_ejemplo(self):
        self.salida.configure(state="normal")
        self.salida.delete("1.0", tk.END)
        self.salida.insert(
            tk.END, "\n".join(self.obtener_mensajes())
        )
        self.salida.configure(state="disabled")


if __name__ == "__main__":
    raiz = tk.Tk()
    PruebaExcepciones(raiz)
    raiz.mainloop()
