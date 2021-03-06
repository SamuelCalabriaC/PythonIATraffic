import pygame
import numpy as np

NEGRO = (0, 0, 0)
BLANCO = (255, 255, 255)
AZUL = (0, 0, 255)
VERDE = (0, 255, 0)
ROJO = (255, 0, 0)
VIOLETA = (255, 0, 255)
GRIS = (150,152,154)
GRIS2 = (170,160,150)
GRIS3 = (190,130,80)
ROSA = (255,192,203)

class Pared(pygame.sprite.Sprite):
    """Esta clase representa la barra inferior que controla el protagonista """

    def __init__(self, x, y, largo, alto, color):
        """ Función Constructor """

        # Llama al constructor padre
        super().__init__()

        # Crea una pared AZUL, con las dimensiones especificadas en los parámetros
        self.image = pygame.Surface([largo, alto])
        self.image.fill(color)

        # Establece como origen la esquina superior izquierda.
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x

        self.t1Coche = 0
        self.nCoches = 0
        self.tCoches = 0
        self.nSalientes = 1
        self.nPeatones = 0
        self.tPeatones = 0
        self.ultimocambio = 0
        self.rojo = 0 #En verde predeterminado


    def calculo_cambio(self):
        if self.rojo.__eq__(0):
            value = abs((self.nCoches * self.tCoches * self.nSalientes) / (60 - self.ultimocambio))
            if value > 2.66: return 1 #1 cambia de color
            else: return 0
        elif self.rojo.__eq__(1):
            value = abs(self.nPeatones*self.tPeatones/(60-self.ultimocambio))
            if value > 2.4: return 1
            else: return 0

    def set_nCoches(self,n):
        self.nCoches = n

    def set_tCoches(self,n):
        self.tCoches = n

    def set_t1Coches(self,n):
        self.t1Coche = 1

    def set_nSalientes(self, n):
            self.nSalientes = n

    def set_nPeatones(self,n):
        self.nPeatones = n

    def set_tPeatones(self,n):
        self.tPeatones = n

    def set_ultimoCambio(self,n):
        self.ultimocambio = n

    def setRojo(self,n):
        self.rojo = n

    def get_Rojo(self):
        return self.rojo

    def get_Values(self):
        return np.array([[self.get_nCoches(),self.get_tCoches(),self.get_t1Coche(),self.get_nSalientes(),self.get_nPeatones(), self.get_tPeatones(), self.get_ultimoCambio() ]])
        #predictionData = np.array([[1,10,40,1.1,80,30,12]])

    def get_nSalientes(self):
        return self.nSalientes
    def get_t1Coche(self):
        return self.t1Coche

    def get_nCoches(self):
        return self.nCoches
    def get_tCoches(self):
        return self.tCoches
    def get_nPeatones(self):
        return self.nPeatones
    def get_tPeatones(self):
        return self.tPeatones
    def get_ultimoCambio(self):
        return self.ultimocambio