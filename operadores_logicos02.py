import tkinter as tk
from tkinter import ttk

# Funciones lógicas
def AND(a, b):
    return int(a and b)

def OR(a, b):
    return int(a or b)

def NOT(a):
    return int(not a)

# Función para mostrar resultados
def mostrar_tabla(operacion):
    resultado.delete("1.0", tk.END)

    if operacion == "AND":
        resultado.insert(tk.END, "Tabla de verdad AND\n")
        resultado.insert(tk.END, "A B | A AND B\n")
        for A in [0,1]:
            for B in [0,1]:
                resultado.insert(tk.END, f"{A} {B} | {AND(A,B)}\n")

    elif operacion == "OR":
        resultado.insert(tk.END, "Tabla de verdad OR\n")
        resultado.insert(tk.END, "A B | A OR B\n")
        for A in [0,1]:
            for B in [0,1]:
                resultado.insert(tk.END, f"{A} {B} | {OR(A,B)}\n")

    elif operacion == "NOT":
        resultado.insert(tk.END, "Tabla de verdad NOT\n")
        resultado.insert(tk.END, "A | NOT A\n")
        for A in [0,1]:
            resultado.insert(tk.END, f"{A} | {NOT(A)}\n")

# Ventana principal
ventana = tk.Tk()
ventana.title("Tablas de verdad - Compuertas lógicas")
ventana.geometry("350x300")

titulo = ttk.Label(ventana, text="Selecciona una compuerta lógica", font=("Arial",12))
titulo.pack(pady=10)

# Botones
btn_and = ttk.Button(ventana, text="Mostrar AND", command=lambda: mostrar_tabla("AND"))
btn_and.pack(pady=5)

btn_or = ttk.Button(ventana, text="Mostrar OR", command=lambda: mostrar_tabla("OR"))
btn_or.pack(pady=5)

btn_not = ttk.Button(ventana, text="Mostrar NOT", command=lambda: mostrar_tabla("NOT"))
btn_not.pack(pady=5)

# Área de texto para resultados
resultado = tk.Text(ventana, height=10, width=35)
resultado.pack(pady=10)

ventana.mainloop()