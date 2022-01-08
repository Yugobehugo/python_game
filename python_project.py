import sys,random
import pygame
import time


class Snake:
    # contenir toutes les variables ainsi que les fonctions utiles pour le bon deroulement du jeu

    def __init__(self):
        """
        :rtype: object
        """

        self.ecran = pygame.display.set_mode((1000, 1000))# la taille de la fenetre. 

        pygame.display.set_caption('Jouez à Snake')# On donne un titre à la fenetre. 
        self.jeu_actif = True

        # creer les variables de position initial et de direction du serpent
        self.position_x_snake = 300
        self.position_y_snake = 300
        self.direction_x_snake = 0
        self.direction_y_snake = 0
     

        # cree la position pour la pomme

          
        # fixer les fps
        self.clock = pygame.time.Clock()

        #creer une liste qui rescence toutes les positions du serpent
        self.positions_snake = []

        # creer la variable en rapport avec la taille du serpent
        self.taille_du_serpent = 1

        self.ecran_du_debut = True

        self.easymode = False


        # Charger l'image

        self.image = pygame.image.load('snake-game.jpg')
        # retrecir l'image
        self.image_titre = pygame.transform.scale(self.image,(400,200))

        # creer la variable score

        self.score = 0

    def ecran_mort(self): # Je crée une fonction pour gérer l'écran de mort
        self.ecran.fill((0,0,0))

        self.ecran.blit(self.image_titre,(300,50,100,50))

        self.message('moyenne','Vous êtes mort gros naze', (200, 450, 200, 5),
                                    (255, 255, 255)) # Elle afiche ce message. 
        

        pygame.display.flip()

    def fonction_principale(self):

        # permet de gerer les evenements , et d'afficher les éléments du jeu avec la boucle While. 

        while self.ecran_du_debut:

            for evenement in pygame.event.get():# verifier les evenements lorsque le jeu est en cours
                #print(evenement)
                if evenement.type == pygame.QUIT:
                    sys.exit()

                if evenement.type == pygame.KEYDOWN: 

                    # Si on appuie sur l abarre d'espace, le jeu lance le mode facile
                     if evenement.key == pygame.K_SPACE:
                         self.easymode = True
                         self.ecran_du_debut = False

               
                     if evenement.key == pygame.K_RETURN:
                    # Si on appuie sur entrer, le jeu lance le mode normal. 
                        self.ecran_du_debut = False

                self.ecran.fill((0,0,0))

                self.ecran.blit(self.image_titre,(300,50,100,50))
                #self.message('petite','Snake',(300,300,100,50),(255,255,255))
                self.message('petite','Le serpent doit grossir le plus possible '
                                    , (250, 300, 200, 5), (240, 240, 240))
                self.message('petite'," pour ça, il doit manger les pommes dès qu'elles aparaissent",
                                    (190, 320, 200, 5), (240, 240, 240))
                self.message('moyenne','Appuyer sur Entrer pour lancer le mode normal', (200, 450, 200, 5),
                                    (255, 255, 255))
                self.message('moyenne','Appuyer sur Espace pour lancer le mode facile', (200, 500, 200, 5),
                                    (255, 255, 255))


                pygame.display.flip()

               # La musique de fond
                file = 'mountain-king.mp3'
                pygame.init()
                pygame.mixer.init()
                pygame.mixer.music.load(file)
                pygame.mixer.music.play(-1) 

                
        if self.easymode == False:
            self.serpent_corps = 10 # taille de la tête du serpent
            self.position_x_apple = random.randrange(110,890,10)
            self.position_y_apple = random.randrange(110,890,10)
            self.pomme = 10

        else:
             self.serpent_corps = 30 # taille de la tête du serpent
             self.position_x_apple = random.randrange(110,890,30)
             self.position_y_apple = random.randrange(110,890,30)
             self.pomme = 30


        while self.jeu_actif: # la boucle se répetre à chaque fois que la condition jeu_actif == true est vrai. 

            # creer un while loop pour creer l'ecran de debut /events /afficher l'image ...

            for evenement in pygame.event.get():# cette méthode permet de recevoir les évnènements quand le jeu est en cours (souris qui bouge, touche appuyé etc...)
                #print(evenement)
                if evenement.type == pygame.QUIT: #Si j'appuie sur la croix de la fenetre...
                    sys.exit() # ... ça quitte le programme. 

                # creer les evenements qui permettent de bouger le serpent

                if evenement.type == pygame.KEYDOWN: # si une touche est pressé

                    if evenement.key == pygame.K_RIGHT:
                        # Quand on presse la fleche droite
                        self.direction_x_snake = 10
                        self.direction_y_snake = 0
                       

                    if evenement.key == pygame.K_LEFT:
                        # Quand on presse la fleche gauche

                        self.direction_x_snake = -10
                        self.direction_y_snake = 0
                       

                    if evenement.key == pygame.K_DOWN:
                         # Quand on presse la fleche du bas

                        self.direction_y_snake = 10
                        self.direction_x_snake = 0
                        

                    if evenement.key == pygame.K_UP:
                         # Quand on presse la fleche du haut

                        self.direction_y_snake = -10
                        self.direction_x_snake = 0
                      



            # faire bouger le serpent si il se trouve dans les limites du jeu

            if self.position_x_snake <= 100 or self.position_x_snake >= 900 \
                or self.position_y_snake <= 100 or self.position_y_snake >= 900 :
                # si la position du serpent depasse les limites alors la partie est terminé et on retourne sur l'écran d'accueil. 
                  Snake().fonction_principale()




            self.serpent_mouvement()

            # cree la cond si le serpent mange la pomme

            if self.position_y_apple == self.position_y_snake and self.position_x_snake == self.position_x_apple: #si la position de la pomme est la même que celle du sprpent (en x et y)...

                print('la pomme est mangé')
                # ... alors on re-régénère une pomme...
                self.position_x_apple = random.randrange(110,890,10)
                self.position_y_apple = random.randrange(110,890,10)

                # ... et on augmente la taille du serpent...

                self.taille_du_serpent += 1
                #... et le score
                self.score += 1

            # creer une liste pour les qui stocke la position de la tete du serpent
            head_snake = []
            head_snake.append(self.position_x_snake)
            head_snake.append(self.position_y_snake)


            # append dans la liste des positions du serpent

            self.positions_snake.append(head_snake)

            # cond pour resoudre le probleme des positions du serpent avec la taille du serpent
            if len(self.positions_snake) > self.taille_du_serpent:

                self.positions_snake.pop(0)
                print(self.positions_snake)


            self.afficher_les_elements()
            self.mordu(head_snake)

          

            # afficher les limites
            self.limites()
            
            if self.easymode == True:

                self.clock.tick(15) #On définit le nombre d'images par seconde, et donc la vitesse du serpent

            else:
                 self.clock.tick(15 + (self.taille_du_serpent *1.5)) #On définit le nombre d'images par seconde, et donc la vitesse du serpent. 
                 #La vitesse augmente dès que le serpent mange une pomme. 

            pygame.display.flip()# mettre a jour l'ecran


    # creer une fonction qui permet de creer un rectangle qui representera les limites du jeu (dimension 100,100,600,500),3


    def limites(self):
        # afficher les limites du jeu

        pygame.draw.rect(self.ecran,(255,0,0),(100,100,800,800),3) # je définie un rectangle avec : une couleur, une taille, et une épaisseur. 

    def serpent_mouvement(self):

        # faire bouger le serpent

        self.position_x_snake += self.direction_x_snake  # faire bouger le serpent a gauche ou a droite
        self.position_y_snake += self.direction_y_snake  # faire bouger le serpent en haut ou en bas

        # print(self.position_x_snake,self.position_y_snake)


    def afficher_les_elements(self):

        self.ecran.fill((0, 50, 50))  # j'attribue une couleur à l'écran

        # Afficher le serpent
        pygame.draw.rect(self.ecran, (255, 0, 0), (self.position_x_snake, self.position_y_snake,
                                                   self.serpent_corps, self.serpent_corps))

        # afficher la pomme
        colorpomme =  (255, 0, 0)
        
        pygame.draw.rect(self.ecran, colorpomme,
                         (self.position_x_apple, self.position_y_apple, self.pomme, self.pomme))

        self.afficher_Serpent()


    def afficher_Serpent(self):
        # afficher les autres parties du serpent

        for partie_du_serpent in self.positions_snake[:-1]:
            pygame.draw.rect(self.ecran, (0, 255, 0),
                             (partie_du_serpent[0], partie_du_serpent[1], self.serpent_corps, self.serpent_corps))

    def mordu(self,tete_serpent):


        # le seprent se mord

        for partie_serpent in self.positions_snake[:-1]:
            if partie_serpent == tete_serpent :
                # L'écran de mort s'affiche 4 secondes, puis c'est l'écran principal. 
                Snake().ecran_mort()
                time.sleep(4)
                Snake().fonction_principale()

# creer une fonction qui permet d'afficher des messages

        self.message('grande','Snake Game', (320, 10, 100, 50), (255, 255, 255), )
        self.message('grande','{}'.format(str(self.score)), (375, 50, 50, 50), (255, 255, 255), )

    def message(self,font,message,message_rectangle,couleur):

        if font == 'petite':
            font = pygame.font.SysFont('Lato',20,False)

        elif font == 'moyenne':
            font = pygame.font.SysFont('Lato',30,False)

        elif font == 'grande':
            font = pygame.font.SysFont('Lato',40,True)

        message = font.render(message,True,couleur)

        self.ecran.blit(message,message_rectangle)



if __name__ == '__main__':

    pygame.init()# initie pygame
    Snake().fonction_principale()
    Snake().ecran_mort()
    pygame.quit()# quitte pygame



    