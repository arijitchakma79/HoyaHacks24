import pygame

class Screen:
    def __init__(self):
        pygame.init()

        screenInfo = pygame.display.Info()
        self.__screenWidth = screenInfo.current_w
        self.__screenHeight = screenInfo.current_h

        self.__surface = pygame.display.set_mode((self.__screenWidth, self.__screenHeight))

    def draw(self):
        self.__surface.fill((255, 255, 255))

        faceY = 60
        faceSize = (400, 250)
        borderWidth = 10

        faceX = (self.__screenWidth - faceSize[0])//2

        eyeSize = (80, 80)
        eyeSpace = 40

        # Face Shadow/Border
        pygame.draw.rect(self.__surface, (0, 0, 0), 
                         pygame.Rect(faceX - borderWidth, faceY - borderWidth, 
                                     faceSize[0] + borderWidth * 2, faceSize[1] + borderWidth * 2),  0, 30)
        
        # Face
        pygame.draw.rect(self.__surface, (207, 69, 0), 
                         pygame.Rect(faceX, faceY, faceSize[0], faceSize[1]),  0, 30)
        
        pygame.draw.rect(self.__surface, (255, 0, 0), 
                         pygame.Rect(faceX + eyeSpace, faceY + 30, eyeSize[0], eyeSize[1]),  0, 15)
        
        pygame.draw.rect(self.__surface, (255, 0, 0), 
                         pygame.Rect((faceX + faceSize[0]) - eyeSpace , faceY + 30, eyeSize[0], eyeSize[1]),  0, 15)
        

        


        
        pygame.display.flip()
        pygame.display.update()