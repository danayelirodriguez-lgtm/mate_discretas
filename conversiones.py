import tkinter as tk
from tkinter import messagebox


def convertir():
    valor = entry_input.get().strip()
    opcion = menu_var.get()

    try:
        if opcion == "Binario a Decimal":
            resultado = int(valor, 2)
        elif opcion == "Decimal a Binario":
            resultado = bin(int(valor))[2:]
        elif opcion == "Hexadecimal a Binario":
            # Hex -> Dec -> Bin
            resultado = bin(int(valor, 16))[2:]
        elif opcion == "Binario a Hexadecimal":
            # Bin -> Dec -> Hex
            resultado = hex(int(valor, 2))[2:].upper()
        elif opcion == "Decimal a Octal":
            resultado = oct(int(valor))[2:]
        elif opcion == "Octal a Decimal":
            resultado = int(valor, 8)
        else:
            resultado = "Selecciona una opción"

        label_resultado.config(text=f"Resultado: {resultado}", fg="#00FF00")
    except ValueError:
        messagebox.showerror("Error", "Entrada inválida para la base seleccionada")


# Configuración de la Ventana Principal
root = tk.Tk()
root.title("Conversor de Bases Numéricas")
root.geometry("400x300")
root.config(padx=20, pady=20)

# Widgets
tk.Label(root, text="Introduce el número:", font=("Arial", 10, "bold")).pack(pady=5)
entry_input = tk.Entry(root, font=("Arial", 12), justify="center")
entry_input.pack(pady=5)

# Menú de opciones
opciones = [
    "Binario a Decimal",
    "Decimal a Binario",
    "Hexadecimal a Binario",
    "Binario a Hexadecimal",
    "Decimal a Octal",
    "Octal a Decimal"
]
menu_var = tk.StringVar(root)
menu_var.set(opciones[0])
selector = tk.OptionMenu(root, menu_var, *opciones)
selector.pack(pady=10)

# Botón de conversión
btn_convertir = tk.Button(root, text="Convertir", command=convertir, bg="#4CAF50", fg="white",
                          font=("Arial", 10, "bold"))
btn_convertir.pack(pady=15)

# Etiqueta de resultado
label_resultado = tk.Label(root, text="Resultado: ", font=("Arial", 12, "bold"))
label_resultado.pack(pady=10)

root.mainloop()