import tkinter as tk

# Funciones para las operaciones
def click_boton(valor):
    current = entrada.get()
    entrada.delete(0, tk.END)
    entrada.insert(0, current + str(valor))

def borrar():
    entrada.delete(0, tk.END)

def calcular():
    try:
        result = eval(entrada.get())  # eval ejecuta la expresión matemática en la entrada
        entrada.delete(0, tk.END)
        entrada.insert(0, str(result))
    except Exception as e:
        entrada.delete(0, tk.END)
        entrada.insert(0, "Error")

# Crear la ventana principal
root = tk.Tk()
root.title("Calculadora")  # Título de la ventana
root.geometry("400x500")  # Tamaño de la ventana

# Crear el campo de entrada para mostrar los resultados
entrada = tk.Entry(root, width=16, font=("Arial", 24), borderwidth=2, relief="solid", justify="right")
entrada.grid(row=0, column=0, columnspan=4)

# Crear los botones
botones = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('+', 4, 2), ('=', 4, 3),
    ('C', 5, 0)
]

# Agregar los botones a la ventana
for (texto, fila, columna) in botones:
    if texto == '=':
        boton = tk.Button(root, text=texto, width=5, height=2, font=("Arial", 18), command=calcular)
    elif texto == 'C':
        boton = tk.Button(root, text=texto, width=5, height=2, font=("Arial", 18), command=borrar)
    else:
        boton = tk.Button(root, text=texto, width=5, height=2, font=("Arial", 18), command=lambda valor=texto: click_boton(valor))
    boton.grid(row=fila, column=columna)

# Ejecutar la aplicación
root.mainloop()
