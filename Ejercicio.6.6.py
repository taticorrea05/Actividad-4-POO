
import math
import tkinter as tk
from tkinter import ttk


class CalculosNumericos:
    @staticmethod
    def calcular_logaritmo_neperiano(valor):
        try:
            if valor <= 0:
                raise ArithmeticError(
                    "El valor debe ser un número positivo"
                )
            return (
                f"Resultado del logaritmo neperiano = "
                f"{math.log(valor):.6f}"
            )
        except ArithmeticError:
            return (
                "El valor debe ser un número positivo "
                "para calcular el logaritmo"
            )

    @staticmethod
    def calcular_raiz_cuadrada(valor):
        try:
            if valor <= 0:
                raise ArithmeticError(
                    "El valor debe ser un número positivo"
                )
            return (
                f"Resultado de la raíz cuadrada = "
                f"{math.sqrt(valor):.6f}"
            )
        except ArithmeticError:
            return (
                "El valor debe ser un número positivo "
                "para calcular la raíz cuadrada"
            )


class InterfazCalculos:
    def __init__(self, ventana):
        ventana.title("Ejercicio 6.6 - Catchs múltiples")
        ventana.geometry("620x290")

        marco = ttk.Frame(ventana, padding=20)
        marco.pack(fill="both", expand=True)

        ttk.Label(
            marco,
            text="Cálculos numéricos",
            font=("Arial", 16, "bold")
        ).pack(pady=10)

        ttk.Label(
            marco,
            text="Valor numérico:"
        ).pack(anchor="w")

        self.valor = ttk.Entry(marco)
        self.valor.pack(fill="x", pady=5)

        ttk.Button(
            marco,
            text="Calcular logaritmo y raíz cuadrada",
            command=self.calcular
        ).pack(pady=12)

        self.resultado = tk.StringVar(
            value="Ingrese un número para realizar ambos cálculos."
        )

        ttk.Label(
            marco,
            textvariable=self.resultado,
            justify="left",
            wraplength=560
        ).pack(anchor="w")

    def calcular(self):
        try:
            valor = float(
                self.valor.get().strip().replace(",", ".")
            )

            if not math.isfinite(valor):
                raise ValueError(
                    "El valor debe ser un número finito."
                )

        except ValueError:
            self.resultado.set(
                "El valor debe ser numérico para calcular "
                "el logaritmo y la raíz cuadrada."
            )
            return

        logaritmo = (
            CalculosNumericos.calcular_logaritmo_neperiano(valor)
        )

        raiz = (
            CalculosNumericos.calcular_raiz_cuadrada(valor)
        )

        self.resultado.set(f"{logaritmo}\n{raiz}")


if __name__ == "__main__":
    raiz = tk.Tk()
    InterfazCalculos(raiz)
    raiz.mainloop()
