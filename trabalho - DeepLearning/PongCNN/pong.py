import pygame
import random

#definindo variáveis para o jogo 
FPS = 60

#tamanho da janela 
WINDOW_WIDTH = 400
WINDOW_HEIGTH = 400

#tamanho das raquetes
PADDLE_WIDTH = 10
PADDLE_HEIGHT = 60

#tamanho da bolinha
BALL_WIDTH = 10
BALL_HEIGHT = 10

#velocidade da raquete e da bolinha 
PADDLE_SPEED = 2 
BALL_X_SPEED = 3
BALL_Y_SPEED = 2 

#paleta de cores RGB para a raquete e bolinha
WHITE = (255,255,255) 
BLACK = (0,0,0)

#inianco a tela 
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGTH))

def drawBall(ballXpos, ballYpos):
	ball = pygame.rect(ballXpos, ballYpos, BALL_WIDTH, BALL_HEIGHT)
	pygame.draw.rect(screen, WHITE, ball)

def drawPaddle1(paddle1YPos):
	paddle1 = pygame.rect(PADDLE_BUFFER, paddle1YPos, PADDLE_WIDTH, PADDLE_HEIGHT)
	pygame.draw.rect(screen, WHITE, paddle1)

def drawPaddle2(paddle2YPos):
	paddle2 = pygame.rect(WINDOW_WIDTH - PADDLE_BUFFER - PADDLE_WIDTH, paddle2YPos, PADDLE_WIDTH, PADDLE_HEIGHT)
	pygame.draw.rect(screen, WHITE, paddle2)

def updateBall(paddle1YPos, paddle2YPos, ballXpos, ballYpos, ballXDirection, ballYDirection):
	#atualizando as posições x e y 
	ballXPos = ballXpos + ballXDirection * BALL_X_SPEED
	ballYPos = ballYpos + ballYDirection * BALL_Y_SPEED
	score = 0 

	#verificando colisão, se a bola bater no lado esquerdo, ativa o aprendizado
	if(ballXPos <= PADDLE_BUFFER + PADDLE_WIDTH and ballYPos + BALL_HEIGHT >= paddle1YPos and ballYPos - BALL_HEIGHT <= paddle1YPos + PADDLE_HEIGHT):
		#troca as direções 
		ballYDirection = 1
	#passada a condição
	elif(ballYPos <= 0):
		#score negativaado
		ballXDirection = 1
		score = -1
		return[score, paddle1YPos, paddle2YPos, ballXpos, ballYpos, ballXDirection, ballYDirection]

	#se a bola colidir com topo
	if(ballYPos <= 0):
		ballYPos = 0
		ballYDirection = 1
	#se colidir com o fundo, ela se move 
	elif(ballYPos >= WINDOW_HEIGHT - BALL_HEIGHT):
		ballYPos = WINDOW_HEIGHT - BALL_HEIGHT
		ballYDirection = -1
		return [score, paddle1YPos, paddle2YPos, ballXPos, ballYPos, ballXDirection, ballYDirection]

    #atualizando a posição das raquetes 
def updatePaddle1(action, paddle1YPos):
    #se se mover para cima
    if (action[1] == 1):
        paddle1YPos = paddle1YPos - PADDLE_SPEED

    #se se mover para baixo
    if (action[2] == 1):
        paddle1YPos = paddle1YPos + PADDLE_SPEED

    #barrando nos limites da tela 
    if (paddle1YPos < 0):
        paddle1YPos = 0

    if (paddle1YPos > WINDOW_HEIGHT - PADDLE_HEIGHT):
        paddle1YPos = WINDOW_HEIGHT - PADDLE_HEIGHT
    return paddle1YPos


def updatePaddle2(paddle2YPos, ballYPos):

    #se move para baixo se a bola está acima da metade da raquete
    if (paddle2YPos + PADDLE_HEIGHT/2 < ballYPos + BALL_HEIGHT/2):
        paddle2YPos = paddle2YPos + PADDLE_SPEED

    #se move para cima se a bola está abaixo da metade da raquete
    if (paddle2YPos + PADDLE_HEIGHT/2 > ballYPos + BALL_HEIGHT/2):
        paddle2YPos = paddle2YPos - PADDLE_SPEED

    #bloqueia no limite da tela 
    if (paddle2YPos < 0):
        paddle2YPos = 0

    #bloqueia o movimento para os limites da tela 
    if (paddle2YPos > WINDOW_HEIGHT - PADDLE_HEIGHT):
        paddle2YPos = WINDOW_HEIGHT - PADDLE_HEIGHT
    return paddle2YPos

#game class 			
class PongGame:
	def _init_(self):
		#iniciando a direção de start da bola com um número aleatótio
		num = random.randint(0,9)
		#mantendo o score
		self.tally = 0
		#inicializando posição das raquetes 
		self.paddle1YPos = WINDOW_HEIGHT / 2 - PADDLE_HEIGHT / 2
		self.paddle2YPos = WINDOW_HEIGHT / 2 - PADDLE_HEIGHT / 2
		#iniciando a direção da bola 
		self.ballXDirection = 1
		self.ballYDirection = 1
		#ponto de inicialização da bola 
		self.ballXPos = WINDOW_WIDTH/2 - BALL_WIDTH/2

		#decidindo randomicamente para onde a bola vai se mover
		if (0 < num < 3):
			self.ballXDirection = 1
			self.ballYDirection = 1
		if (3 <= num < 5):
			self.ballXDirection = -1
			self.ballYDirection = 1
		if (5 <= num < 8):
			self.ballXDirection = 1
			self.ballYDirection = -1
		if (8 <= num < 10):
			self.ballXDirection = -1
			self.ballYDirection = -1
		#novo nuemro aleatório
		num = random.randint(0,9)
		#aonde vai começar na parte y(altura na tela)
		self.ballYPos = num*(WINDOW_HEIGHT - BALL_HEIGHT)/9

	#para cada frame haverá a chamda para o evento, "repintando" a tela 
	def getPresentFrame(self):
		pygame.event.pump()
		#fundo de tela preto
		screen.fill(BLACK)
		#desenhando as raquetes 
		drawPaddle1(self.paddle1YPos)
		drawPaddle2(self.paddle2YPos)
		#desenhando a bola 
		drawBall(self.ballXPos, self.ballYPos)
		#copaiando os pixels para um array 3d, isto será usado na rede neural RL
		image_data = pygame.surfarray.array3d(pygame.display.get_surface())
		#atualizando a tela 
		pygame.display.flip()
		#retornando os dados da superficie 
		return surface_data

	#autaualizando a tela
	def getNextframe(self, action):
		pygame.event.pump()
		score = 0 
		screen.fill(BLACK)
		#atualizando as raquetes 
		self.paddle1YPos = updatePaddle1(action, self.paddle1YPos)
		drawPaddle1(self.paddle1YPos)
		#atualizando a raquete AI malandrinha
		self.paddle2YPos = updatePaddle2(self.paddle2YPos, self.ballYpos)
		drawPaddle2(self.paddle2YPos)
		#atualizando as variaveis pela posição da bola
		[score, self.paddle1YPos, self.paddle2YPos, self.ballXPos, self.ballYPos, self.ballXDirection, self.ballYDirection] = updateBall(self.paddle1YPos, self.paddle2YPos, self.ballXPos, self.ballYPos, self.ballXDirection, self.ballYDirection)
		#desenhando a bola 
		drawBall(self.ballXPos, self.ballYPos)
		#pegando nos dados da superficie
		image_data = pygame.surfarray.array3d(pygame.display.get_surface())
		pygame.display.flip()
		self.tally = self.tally + score
		print ("Tally is") + str(self.tally)
		return[score, image_data]












			









