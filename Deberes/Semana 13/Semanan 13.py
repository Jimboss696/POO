import tkinter as tk

class AplicacionGUI:
    def __init__(self, ventana):
        # Constructor de la clase, crea la interfaz gráfica
        self.ventana = ventana
        self.ventana.title("Aplicación de Ejemplo")  # Título de la ventana

        # Etiqueta para indicar al usuario que ingrese información
        self.etiqueta = tk.Label(ventana, text="Ingrese la información:")
        self.etiqueta.pack()  # Coloca la etiqueta en la ventana

        # Campo de texto para que el usuario ingrese la información
        self.campo_texto = tk.Entry(ventana)
        self.campo_texto.pack()  # Coloca el campo de texto en la ventana

        # Botón "Agregar" para agregar la información a la lista
        self.boton_agregar = tk.Button(ventana, text="Agregar", command=self.agregar_info)
        self.boton_agregar.pack()  # Coloca el botón "Agregar" en la ventana

        # Lista para mostrar la información ingresada por el usuario
        self.lista = tk.Listbox(ventana)
        self.lista.pack()  # Coloca la lista en la ventana

        # Botón "Limpiar" para limpiar la lista de información
        self.boton_limpiar = tk.Button(ventana, text="Limpiar", command=self.limpiar_info)
        self.boton_limpiar.pack()  # Coloca el botón "Limpiar" en la ventana

    def agregar_info(self):
        # Método para agregar la información ingresada por el usuario a la lista
        info = self.campo_texto.get()  # Obtiene la información del campo de texto
        if info:  # Verifica si hay información ingresada
            self.lista.insert(tk.END, info)  # Inserta la información en la lista
            self.campo_texto.delete(0, tk.END)  # Borra el contenido del campo de texto después de agregar la información

    def limpiar_info(self):
        # Método para limpiar la lista de información
        self.lista.delete(0, tk.END)  # Borra todos los elementos de la lista

if __name__ == "__main__":
    # Crear la ventana principal de la aplicación
    ventana_principal = tk.Tk()

    # Crear una instancia de la clase AplicacionGUI y pasarle la ventana principal
    app = AplicacionGUI(ventana_principal)

    # Iniciar el bucle principal de la aplicación
    ventana_principal.mainloop()
