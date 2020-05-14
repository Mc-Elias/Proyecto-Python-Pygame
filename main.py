import pygame
from pygame.locals import *

# tamaño de la pantalla
SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480

class Posicion():
    
    def __init__(self):
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.fondo = pygame.image.load("fondo.jpg").convert()
        self.balon = pygame.image.load("balon.png").convert_alpha()
        self.arco = pygame.image.load("arco.png").convert_alpha()
        self.balon_posicion_x = 500
        self.balon_posicion_y = 200
        self.arco_posicion_x = 50
        self.arco_posicion_y = 70
        self.width = 20
        self.height = 20
        self.vel = 1
        self.abajo = 0
        self.derecha = 0
        self.arriba = 0
        self.izquierda = 0
        self.goles = 0
        self.fuente = pygame.font.Font(None, 20)

    def pocisionar(self):
        self.screen.blit(self.balon, (self.balon_posicion_x, self.balon_posicion_y))
        self.screen.blit(self.arco, (self.arco_posicion_x, self.arco_posicion_y))
        self.screen.blit(self.fondo, (0, 0))

    
     
class Correr_el_juego(Posicion):
    def correr_juego(self):
        while True:
            ''' 
            procesamos con la movida del arco sumando, restando posiciones del arco.
            Ademas al mismo tiempo igualamos sus posiciones del balon y el arco, asi aumenta el numero de gol.

            '''

            # para abajo
            if self.abajo == 0:
                if self.arco_posicion_x == self.balon_posicion_x and self.arco_posicion_y == self.balon_posicion_y:
                    self.goles = self.goles + 1 
                self.arco_posicion_y = self.arco_posicion_y + 1
                if self.arco_posicion_y > 400:               
                    self.abajo = 1
                    self.arco_posicion_x = 50
                    self.arco_posicion_y = 400
            else:
                #para derecha
                if self.derecha == 0:
                    if self.arco_posicion_x == self.balon_posicion_x and self.arco_posicion_y == self.balon_posicion_y:
                        self.goles = self.goles + 1 
                    self.arco_posicion_x = self.arco_posicion_x + 1
                    if self.arco_posicion_x > 571:
                        self.derecha = 1
                        self.arco_posicion_x = 570
                        self.arco_posicion_y = 400
                else:
                    # para arriba
                    if self.arriba == 0:
                        if self.arco_posicion_x == self.balon_posicion_x and self.arco_posicion_y == self.balon_posicion_y:
                            self.goles = self.goles + 1 
                        self.arco_posicion_y = self.arco_posicion_y - 1
                        if self.arco_posicion_y < 71:
                            self.arriba = 1
                            self.arco_posicion_x = 570
                            self.arco_posicion_y = 70
                    else:
                        # para izquierda
                        if self.izquierda == 0:
                            if self.arco_posicion_x == self.balon_posicion_x and self.arco_posicion_y == self.balon_posicion_y:
                                self.goles = self.goles + 1 
                            self.arco_posicion_x = self.arco_posicion_x - 1
                            if self.arco_posicion_x < 51:
                                self.arco_posicion_x = 50
                                self.arco_posicion_y = 70
                                self.abajo = 0
                                self.derecha = 0
                                self.arriba = 0 
        
            # variable texto que se va imprimir
            text = "Goles: " + str(self.goles) + "                                                    <<Usar las flechas del teclado>>"
        
            # variable mensaje que se va mostrar en la pantalla
            mensaje = self.fuente.render(text, 1, (255, 255, 255))

            # Redibujamos todos los elementos de la pantalla
            self.screen.blit(self.fondo, (0, 0))
            self.screen.blit(self.arco, (self.arco_posicion_x, self.arco_posicion_y))
            self.screen.blit(self.balon, (self.balon_posicion_x, self.balon_posicion_y))
            self.screen.blit(mensaje, (15, 5))

            # se muestran lo cambios en pantalla
            pygame.display.flip()
            
            # Posibles entradas del teclado y mouse
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            keys = pygame.key.get_pressed()

            if keys[pygame.K_LEFT] and self.balon_posicion_x > 0:
                self.balon_posicion_x -= self.vel

            if keys[pygame.K_RIGHT] and self.balon_posicion_x < 600 - self.width:
                self.balon_posicion_x += self.vel

            if keys[pygame.K_UP] and self.balon_posicion_y > 0:
                self.balon_posicion_y -= self.vel

            if keys[pygame.K_DOWN] and self.balon_posicion_y < 450 - self.height:
                self.balon_posicion_y += self.vel

def main():

    pygame.init()
    pygame.display.set_caption("Proyecto_poo_PyData")
    posion = Posicion()
    posion.pocisionar()
    pygame.display.flip()
    corre_el_juego = Correr_el_juego()
    corre_el_juego.correr_juego()

if __name__ == "__main__":
    main()