import pygame 
import random 


pygame.init()
pygame.font.init()
pygame.display.set_caption("Flappy Ball")
screen = pygame.display.set_mode((400, 600))

scorefont = pygame.font.SysFont('Comic Sans MS', 15)


def main():


	global z
	global score 
	global y 
	global spacecount
	global highscore

	score = 0 
	highscore = 0


	restart()
	
	while True:

		screen.fill((255,255,255))


		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_SPACE:
					y -= 60
					z = pygame.time.get_ticks()/1000
					displacement = y 
					spacecount += 1 
         
		if spacecount > 0: 
			time = pygame.time.get_ticks()/1000 + 1 - z

			y = (30 * time * time) + displacement


			
			if y < 0 or y > 570: 
				restart()
				bar1.barx = 430  
				bar2.barx = 630 

		bar1.barmechanics() 
		bar1.y = y 
		bar1.spaces = spacecount

		bar2.barmechanics() 
		bar2.y = y 
		bar2.spaces = spacecount 

		scoretext = scorefont.render(f'score: {score}', False, (0, 0, 0)) 
		highscoretext = scorefont.render(f'highscore: {highscore}', False, (0, 0, 0,))
		 
		

		pygame.draw.circle(screen,(0,0,0),(200,y),10)
		screen.blit(scoretext,(330,0))
		screen.blit(highscoretext,(0,0))




		pygame.display.update()


class bar: 
	def __init__(self,barx,y,spacecount):
		self.barx = barx 
		self.bar1y = random.randint(100,500)
		self.bar2y = self.bar1y + 100
		self.y = y 
		self.start = barx 
		self.spaces = spacecount
	 

	def barmechanics(self):
		global score
		global loop 


		if self.barx < -20: 
				self.barx = 430 
				self.bar1y = random.randint(50,550)
				self.bar2y = self.bar1y + 90 
				loop += 1 

		if self.spaces > 0: 
			self.barx -= 0.08

		if self.barx < 190: 
			score = loop 

		if self.barx < 210 and self.barx > 190:
			if  self.y < self.bar1y or  self.y >  self.bar2y:
				self.barx = self.start 
				restart()
				

		pygame.draw.rect(screen,(0,0,0),(self.barx,0,30,self.bar1y))
		pygame.draw.rect(screen,(0,0,0),(self.barx,self.bar2y,30,600 - self.bar2y)) 


def restart():
	global z
	global score 
	global y 
	global spacecount
	global time 
	global displacement
	global bar1 
	global bar2
	global highscore
	global loop 


	if score > highscore: 
		 highscore = score 
 
	z = 0
	score = 0
	y = 290 
	spacecount = 0  
	time = 0 
	displacement = 0
	loop = 1



	bar1 = bar(430,y,spacecount)
	bar2 = bar(630,y,spacecount)



 








		
 
		



if __name__ == '__main__':
	main()