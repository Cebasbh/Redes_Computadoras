import numpy as np

def F(x, y, z):
    return (x & y) | (~x  & z)

def G(x, y, z):
    return (x & z) | (y & ~z)

def H(x, y, z):
    return x ^ y ^ z

def I(x, y, z):
    return y ^ (x | ~z)
def T():
    T = []
    for i in range(64):
        value = int((2**32) * np.abs(np.sin(i + 1))) & 0xFFFFFFFF
        T.append(value)
    return T
def left_rotate(x, amount):
    x &= 0xFFFFFFFF  # asegura que x es de 32 bits
    return ((x << amount) | (x >> (32 - amount))) & 0xFFFFFFFF
def little_endian(string:str) -> list[str]:
    stringvolteado = []
    while len(string) > 0:
        aux = string[-8:]
        stringvolteado.append(aux)
        string = string[:-8]
    return stringvolteado
def concatenar_lista(lista:list[str]) -> str:
    sum = ""
    for i in lista:
        sum = sum + i
    return sum
def slicear_lista(sum:str, trozos:int) -> list[str]:
    lista = []
    # Separamos el binario en binarios de 32 bits
    while len(sum) >= trozos:
        aux = sum[:trozos]
        lista.append(aux)
        sum = sum[trozos:]
    return lista
