from abc import ABC, abstractmethod
from os import read
from PIL import Image, ImageDraw

class Escritor(ABC):
    @abstractmethod
    def escribir(self, usrtxt:str):
       pass
        

class InsertarTexto(Escritor):
    
    def enImagen(texto:str):
        texto = texto + "usamos python para esto :)"
        imagenAUsar = Image.open("imagen.jpg")
        imagenEditable = ImageDraw.Draw(imagenAUsar)
        imagenEditable.text((15,15), texto, (255,255,255))
        imagenAUsar.save("resultado.jpg")


if __name__ == "__main__":
    textoAUsar = input('Escribe palabras a insertar en la imagen')
    InsertarTexto.enImagen(textoAUsar)
 
