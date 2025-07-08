from operaciones import *
from Bloques import *
import datetime

def main():
    code = input("Ingrese su texto a hashear: ")
    hash(code)
class Log(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Generador MD5")
        self.resizable(0, 0)
        self.geometry("460x280")
        self.grid_columnconfigure((0), weight=3)
        self.grid_columnconfigure((1), weight=3)
        self.grid_columnconfigure((2), weight=3)
        self.grid_columnconfigure((3), weight=3)
        self.grid_columnconfigure((4), weight=1)
        
        entry = Entry(master = self, width = 280)
        entry.grid(row=1, column=0, padx=(20,20), pady=(0,10), sticky="ew", columnspan=5)

        hashed = Entry(master = self, width = 280)
        hashed.grid(row=3, column=0, padx=(20,20), pady=(0,10), sticky="ew", columnspan=5)
        hashed.configure(state="disabled")

        timestamp = Entry(master = self, width=280)
        timestamp.grid(row=5, column=0, padx=(20, 20), pady=(0,10), sticky="ew", columnspan=5)
        timestamp.configure(state="disabled")
        #
        def hashear():
            hashed.configure(state="normal")
            timestamp.configure(state="normal")

            hashed.delete(0, "end")
            timestamp.delete(0, "end")

            # Insertar hash
            hashed.insert(0, hash(entry.get()))

            # Insertar timestamp
            now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            timestamp.insert(0, now)

            hashed.configure(state="disabled")
            timestamp.configure(state="disabled")

        def copiar():
            if hashed.get() == "":
                inform.configure(text = "No hay nada :(", text_color = "red")
            else:
                self.clipboard_clear()
                self.clipboard_append(hashed.get())
                inform.configure(text = "Copiado!", text_color = "green")
            self.update()
            borrar_mensaje()
        def borrar_mensaje():
            self.after(2000, lambda: inform.configure(text=""))

        hashbutton = Button(master = self, text="Hash!", command = hashear, width = 130)
        hashbutton.grid(row=6, column=4, padx=(0,20), pady=(13,0), sticky="e")

        copybutton = Button(master = self, text="Copy!", command = copiar, width = 130)
        copybutton.grid(row=6, column=3, padx=(0,5), pady=(13,0), sticky="e")

        text = Label(master = self, text="Texto a hashear: ")
        text.grid(row=0, column=0, padx=(20,0), pady=(10,0), sticky="w", columnspan=4)

        text1 = Label(master = self, text="Texto a hasheado: ")
        text1.grid(row=2, column=0, padx=(20,0), pady=0, sticky="w", columnspan=4)

        label_timestamp = Label(master=self, text="Fecha y hora de generación:")
        label_timestamp.grid(row=4, column=0, padx=(20, 0), pady=0, sticky="w", columnspan=4)

        inform = Label(master = self, text="")
        inform.grid(row=6, column=0, padx=(45,0), pady=(12,0))

def hash(code:str):
    A = 1732584193
    B = 4023233417
    C = 2562383102
    D = 271733878
    S = [
        7, 12, 17, 22,  7, 12, 17, 22,  7, 12, 17, 22,  7, 12, 17, 22,
        5,  9, 14, 20,  5,  9, 14, 20,  5,  9, 14, 20,  5,  9, 14, 20,
        4, 11, 16, 23,  4, 11, 16, 23,  4, 11, 16, 23,  4, 11, 16, 23,
        6, 10, 15, 21,  6, 10, 15, 21,  6, 10, 15, 21,  6, 10, 15, 21
    ]
    # Paso 1
    # Solicitar el string
    lista = []
    # Convertir el string a número con utf-8 y posterior a eso convertir en binario
    utf = code.encode("utf-8")
    longitud = len(utf)
    for i in utf:
        i = format(i, "08b")
        lista.append(i)
    # Agregar un flag, el cuál diga hasta dónde llega el mensaje
    lista.append(format(128,"08b"))
    # Agregar 0s hasta que queden 8 espacios, para la longitud. De pasarse de 56, Rellenar el bloque y proseguir hasta el siguiente
    while len(lista)%64 != 56:
        lista.append(format(0,"08b"))
    # Convertir la longitud de bytes a bits para ingresarlo en la lista
    longitud_lista = []
    longitud = longitud * 8
    longitud = format(longitud, "08b")
    # Corta el binario en trozos de 8 y los va poniendo en la lista en formato little-endian
    longitud_lista = little_endian(longitud)
    # Agergar Agregar 0s para completar el número de 8 bits si la longitud era de 9 bits o más
    while len(longitud_lista[-1]) < 8:
        longitud_lista[-1] = "0" + longitud_lista[-1]
    # Agregar 0s para completar los 8 bytes
    while len(longitud_lista) < 8:
        longitud_lista.append(format(0,"08b"))
    lista.extend(longitud_lista)
    # Agregar display acá por debugging
    # Eliminando variables que ya no serán usadas
    del longitud, utf, code, longitud_lista
    # Paso 2
    # Convertir todo en un binario larguísimo
    sum = concatenar_lista(lista)
    bloques = slicear_lista(sum,512)

    # Paso 3
    a, b, c, d = A, B, C, D
    #Operaciones exhaustivas 
    T_table = T()
    for bloque in bloques:
        palabras = slicear_lista(bloque, 32)

        for i, v in enumerate(palabras):
            auxlista = little_endian(v)
            palabra_bin = concatenar_lista(auxlista)
            palabras[i] = int(palabra_bin, 2)
        
        A_temp, B_temp, C_temp, D_temp = a, b, c, d
        for i in range(64):
            if 0 <= i <= 15:
                f = F(B_temp, C_temp, D_temp)
                g = i
            elif 16 <= i <= 31:
                f = G(B_temp, C_temp, D_temp)
                g = (5 * i + 1) % 16
            elif 32 <= i <= 47:
                f = H(B_temp, C_temp, D_temp)
                g = (3 * i + 5) % 16
            else:
                f = I(B_temp, C_temp, D_temp)
                g = (7 * i) % 16
            
            temp = D_temp
            D_temp = C_temp
            C_temp = B_temp
            B_temp = (B_temp + left_rotate((A_temp + f + T_table[i] + palabras[g]) & 0xFFFFFFFF, S[i])) & 0xFFFFFFFF
            A_temp = temp

        a = (a + A_temp) & 0xFFFFFFFF
        b = (b + B_temp) & 0xFFFFFFFF
        c = (c + C_temp) & 0xFFFFFFFF
        d = (d + D_temp) & 0xFFFFFFFF

    hash = [a, b, c, d]
    #Por cada elemento, lo convertimos a binario
    for i, v in enumerate(hash):
        v = format(v, "032b")
        while len(v) % 8 != 0:
            v = "0" + v
        #Luego a little endian
        binario = concatenar_lista(little_endian(v))
        entero = int(binario, 2)
        #Finalmente formateamos como hexadecimal
        hash[i] = format(entero, '08x')
    return concatenar_lista(hash)

if __name__ == "__main__":
    app = Log()
    app.mainloop()