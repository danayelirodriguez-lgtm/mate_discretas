import tkinter as tk
from tkinter import messagebox


def calcular(operacion):
    n1_str = entry_n1.get().strip()
    n2_str = entry_n2.get().strip()

    # Validación: Si los campos están vacíos
    if not n1_str or not n2_str:
        messagebox.showwarning("Atención", "Por favor, ingresa ambos números")
        return

    try:
        # Convertimos de binario (base 2) a entero decimal
        num1 = int(n1_str, 2)
        num2 = int(n2_str, 2)

        if operacion == "+":
            res_dec = num1 + num2
        elif operacion == "-":
            res_dec = num1 - num2
        elif operacion == "*":
            res_dec = num1 * num2
        elif operacion == "/":
            if num2 == 0:
                messagebox.showerror("Error", "No se puede dividir por cero")
                return
            res_dec = num1 // num2  # División entera

        # Convertimos el resultado decimal de nuevo a binario
        # Si el resultado es negativo, añadimos el signo manualmente
        if res_dec >= 0:
            resultado_binario = bin(res_dec)[2:]
        else:
            resultado_binario = "-" + bin(abs(res_dec))[2:]

        label_res.config(text=f"Resultado Binario: {resultado_binario}", fg="#2ecc71")
        label_dec.config(text=f"(En decimal: {res_dec})", fg="#bdc3c7")

    except ValueError:
        messagebox.showerror("Error", "Entrada inválida. Usa solo 0 y 1")


def limpiar():
    entry_n1.delete(0, tk.END)
    entry_n2.delete(0, tk.END)
    label_res.config(text="Resultado Binario: -", fg="white")
    label_dec.config(text="(En decimal: -)", fg="#bdc3c7")


# --- Configuración de la Interfaz ---
root = tk.Tk()
root.title("Calculadora Binaria")
root.geometry("380x500")
root.config(bg="#2c3e50", padx=20, pady=20)

# Estilos comunes
label_style = {"bg": "#2c3e50", "fg": "white", "font": ("Arial", 11, "bold")}

# Entradas de texto
tk.Label(root, text="Primer número binario:", **label_style).pack(pady=(10, 5))
entry_n1 = tk.Entry(root, font=("Consolas", 14), justify="center", bd=2)
entry_n1.pack(fill="x")

tk.Label(root, text="Segundo número binario:", **label_style).pack(pady=(15, 5))
entry_n2 = tk.Entry(root, font=("Consolas", 14), justify="center", bd=2)
entry_n2.pack(fill="x")

# Contenedor de botones de operación
frame_btns = tk.Frame(root, bg="#2c3e50")
frame_btns.pack(pady=25)

# Configuración de botones (Corregido padx)
btn_params = {"width": 6, "height": 2, "font": ("Arial", 12, "bold"), "fg": "white", "cursor": "hand2"}

tk.Button(frame_btns, text="+", bg="#3498db", command=lambda: calcular("+"), **btn_params).grid(row=0, column=0, padx=8,
                                                                                                pady=5)
tk.Button(frame_btns, text="-", bg="#e74c3c", command=lambda: calcular("-"), **btn_params).grid(row=0, column=1, padx=8,
                                                                                                pady=5)
tk.Button(frame_btns, text="×", bg="#f1c40f", command=lambda: calcular("*"), **btn_params).grid(row=1, column=0, padx=8,
                                                                                                pady=5)
tk.Button(frame_btns, text="÷", bg="#9b59b6", command=lambda: calcular("/"), **btn_params).grid(row=1, column=1, padx=8,
                                                                                                pady=5)

# Área de Resultados
label_res = tk.Label(root, text="Resultado Binario: -", bg="#2c3e50", fg="white", font=("Arial", 14, "bold"))
label_res.pack(pady=(20, 0))

label_dec = tk.Label(root, text="(En decimal: -)", bg="#2c3e50", fg="#bdc3c7", font=("Arial", 10, "italic"))
label_dec.pack()

# Botón de Limpiar
tk.Button(root, text="Limpiar campos", command=limpiar, bg="#7f8c8d", fg="white", font=("Arial", 9), bd=0).pack(
    side="bottom", pady=10)

root.mainloop()