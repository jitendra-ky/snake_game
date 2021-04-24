import pygame
import random
pygame.init()
pygame.mixer.init()

# Define colors
green = (1,50,32)
red = (228, 0, 0)
snkClr = (25, 25, 25)
white = (0, 0, 0)
w_x = 450
w_y = 600

#make display 
window = pygame.display.set_mode((w_x, w_y))
pygame.display.set_caption("this is my first game")
image = pygame.image.load("grass.jpg")

# Give title
pygame.display.set_caption("PYTHON GAME")
pygame.display.update()

clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 30)
def screen_text(text, color, x, y):
    screen_text = font.render(text, True, color)
    window.blit(screen_text, [x, y])

def plot_snake(gameWindow, color, snk_list, snake_size): # function that plot the snake
    # print(snk_list)
    for i in snk_list[0: -5]:
        pygame.draw.circle(gameWindow, color, i, snake_size-15)
    # try:
    #     for i in snk_list[-5: -1]:
    #         pygame.draw.circle(gameWindow, red, i, snake_size-15)
    # except:
    #     pass


#the welcome screen
def welcome():
    exit_game = False
    while not exit_game:
        window.fill((100,100,100))
        screen_text("WELCOME",(50, 50, 50), 150, 200)
        screen_text("press scpace to play", (50, 50, 50), 100, 250)
        screen_text("*****PYTHON GAME CREATED BY JITENDRA*****", (50, 50, 50), 0, 550)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    pygame.mixer.music.load('start.mp3')
                    pygame.mixer.music.play()
                    gameloop()
                if event.key == pygame.K_RETURN:
                    pygame.mixer.music.load('start.mp3')
                    pygame.mixer.music.play()
                    gameloop()
        clock.tick(60)
        pygame.display.update()


#Game loop 
def gameloop():

    f = open("highscore.txt", "r+")
    highscore = int(f.read())
    
    #game specific vairable
    exit_game = False
    game_over = False
    snake_size = 30
    food_size = snake_size
    score = 0
    s_x =  w_x/2
    s_y =  w_y/2
    f_x = random.randint(20, w_x-20)
    f_y = random.randint(20, w_y-20)
    v_x = 0
    v_y = 0
    v = 5
    fps = 70
    snk_list = []
    snk_length = 1
    

    while not exit_game:
        if game_over:
            over = pygame.image.load("over.PNG")
            window.blit(over, (0,0))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        f.write(str(highscore))
                        welcome()
                    if event.key == pygame.K_SPACE:
                        f.write(str(highscore))
                        welcome()
        else:
            for event in pygame.event.get():
                
                if event.type == pygame.QUIT :
                    exit_game = True
                
                if event.type == pygame.KEYDOWN:
                    
                    #cheat code
                    if event.key == pygame.K_g:
                        score += 10
                    if event.key == pygame.K_o:
                        game_over = True
                    if event.key == pygame.K_v:
                        fps += 5
                    if event.key == pygame.K_c:
                        fps -= 5

                    #movement
                    if (event.key == pygame.K_RIGHT or event.key == pygame.K_d) and v_x != -v:
                        v_x = v
                        v_y = 0
                    if (event.key == pygame.K_LEFT or event.key == pygame.K_a) and v_x != v:
                        v_x = -v
                        v_y = 0
                    if (event.key == pygame.K_UP or event.key == pygame.K_w) and v_y != v:
                        v_y = -v
                        v_x = 0
                    if (event.key == pygame.K_DOWN or event.key == pygame.K_s) and v_y != -v:
                        v_y = v
                        v_x = 0
            
            if s_x > w_x :
                s_x -= w_x
            if s_x < 0 :
                s_x += w_x
            if s_y > w_y :
                s_y -= w_y
            if s_y < 0 :
                s_y += w_y
            
            # snake eat food
            if abs(f_y - s_y) < 25 and abs(f_x - s_x) < 25 :
                score += 10
                pygame.mixer.music.load('zapsplat_cartoon_bite_eat_crunch_single_003_58272.mp3')
                pygame.mixer.music.play()
                if score > highscore:
                    highscore = score
                    
                f_x = random.randint(20, w_x-20) # get the cordinates of new food
                f_y = random.randint(20, w_y-20)
                snk_length += 5
                

            window.fill(white)
            window.blit(image, (0, 0))
            if score >= highscore:
                screen_text("you are creating high score (●'◡'●)", (100,50, 50), 100, 550)
            screen_text(f"python game  SCORE : {score}   high score is {highscore}", red, 5, 5)
            pygame.draw.circle(window, green, [s_x, s_y], snake_size-15 ) # draw mouth of sname
            pygame.draw.rect(window, (0,255,0), [f_x-2, f_y-30, 5, 25]) # draw food stick
            pygame.draw.circle(window, red, [f_x, f_y], food_size-15) # make the food 
            
            s_x += v_x
            s_y += v_y

            head = []
            head.append(s_x)
            head.append(s_y)
            snk_list.append(head)

            if len(snk_list)>snk_length:
                del snk_list[0]

            plot_snake(window, snkClr, snk_list, snake_size)
            
            if  [s_x, s_y] in snk_list[0:-1]:
                pygame.mixer.music.load('over.mp3')
                pygame.mixer.music.play()
                game_over = True
            
                
            
        pygame.display.update()
        clock.tick(fps)
    f.write(str(highscore))   
    # Quit the game
    pygame.quit()
    quit()

welcome()
