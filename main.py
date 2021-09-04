from pygame.constants import WINDOWHITTEST
from globals import * #Copy over the namespace
import dude

pygame.init()

#GAME OVER message
def draw_endgame():
    draw_endgame = ENDGAME_FONT.render("GAME OVER", 25, (0,0,0))
    screen.blit(draw_endgame,WIDTH/2-draw_endgame.get_width() /2 , HEIGHT/2 - draw_endgame.get_height()/2)

def draw_window():
    
    screen.blit(BACKGROUND, (0,0))
    # showing the remaining lives
    Lives_text = HEALTH_FONT.render("Lives: ", 15, (0,0,0))
    screen.blit(Lives_text, (WIDTH - Lives_text.get_width()- LIFE.get_width()*5 - 15, 0)) #Lives: ***** |
    for i in range(LIVES):
        #LIVES_REM= HEALTH_FONT.render("Lives: "+ str(LIVES), 25, (0,0,0))
        screen.blit(LIFE, (WIDTH - LIFE.get_width()*5 - 15 + LIFE.get_width()*i, LIFE.get_height()/2)) # let i = 2, |    Lives: 
    
    # Add the Bins on NESW of screen
    screen.blit(BLUE_BIN, (WIDTH/2-BLUE_BIN.get_width()/2, 0 ))
    screen.blit(GREEN_BIN, (0,(HEIGHT/2-GREEN_BIN.get_height()/2)))
    screen.blit(BLACK_BIN, (WIDTH/2-BLACK_BIN.get_width()/2, HEIGHT-BLACK_BIN.get_height()))
    screen.blit(YELLOW_BIN, (WIDTH-YELLOW_BIN.get_width(),HEIGHT/2-YELLOW_BIN.get_height()/2))

    # Draw a solid blue circle in the center
    pygame.draw.circle(screen, (245, 245, 220), CIRCLE_COORDS, CIRCLE_RADIUS)

    #pygame.display.flip() # Flip the display


def main():
    clock = pygame.time.Clock()
    # Run until the user asks to quit
    running = True
    guy = dude.Dude(LIVES) #There should only ever be one Dude instance

    while running:
        clock.tick(FPS)
        draw_window() #Init screen

        ##Game logic goes here!##
        guy.draw() #Only draw inside of a game loop!

        # If guy dies, end game message shows
        #   guy.death() is called in Dude menthod (upon health <= 0)
        #draw_endgame()

        # Did the user click the window close button?
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            ##Grab more events here!##
            guy.events_processor(event)
            

        # Update the screen
        pygame.display.update()
    # Done! Time to quit.
    pygame.quit()

if __name__ == "__main__":
    main()
