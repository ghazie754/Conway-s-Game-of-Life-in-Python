import time
import pygame
import numpy as np
import colorsys


COLOR_GB = (10, 10 ,10)
COLOR_GRID = (40, 40, 40)
COLOR_DIE_NEXT = (255, 10, 10)
COLOR_ALIVE_NEXT = (234, 233, 23)
WIDTH, HEIGHT = 1200, 800
cellsize = 10
wow, hi = int(WIDTH/10), int(HEIGHT/10)
def undate(screen, cells, size , with_porgress=False):
    update_cells = np.zeros((cells.shape[0], cells.shape[1]))
    for row, col in np.ndindex(cells.shape):
        alive = np.sum(cells[row-1:row+2,col-1:col+2]) - cells[row, col]
        color = COLOR_GB if cells[row, col] == 0 else COLOR_ALIVE_NEXT

        if cells[row, col] == 1 :
            if alive < 2 or alive > 3:
                if with_porgress:
                    color = COLOR_DIE_NEXT
            elif 2 <= alive <= 3:
                update_cells[row, col] = 1
                if with_porgress:
                    color = COLOR_ALIVE_NEXT
        else:
            if alive == 3:
                update_cells[row, col] = 2
                if with_porgress:
                    color = COLOR_ALIVE_NEXT
            if alive == 9:
                update_cells[row, col] = 1
                if with_porgress:
                    color = COLOR_ALIVE_NEXT
            if alive == 8:
                update_cells[row, col] = 3
                if with_porgress:
                    color = COLOR_ALIVE_NEXT
        pygame.draw.rect(screen, color, (col * size, row * size, size - 1, size - 1))
    
    
    return update_cells

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    
    cells = np.zeros((hi, wow))
    screen.fill(COLOR_GRID)
    undate(screen, cells, cellsize)

    pygame.display.flip()
    pygame.display.update()
    
    run = False
    
    while True:
        for event in pygame.event.get():
            if  event.type == pygame.QUIT:
                pygame.quit()
                pygame.Color.update((0,0,0,255))
                return
            elif event.type == pygame.KEYDOWN:
                if  event.key == pygame.K_SPACE:
                    run = not run
                    undate(screen, cells, cellsize)
                    pygame.display.update()
            if pygame.mouse.get_pressed()[0]:
                pos = pygame.mouse.get_pos()
                cells[pos[1] // cellsize, pos[0] // cellsize] = 1
                undate(screen, cells, cellsize)
                pygame.display.update()
        
        for W in range(0, int(wow/10)):
            for H in range(0, int(hi/10)):
                if cells[W, 0] == 1 or cells[0, H] == 1 :
                    cellscells[w,h] = 0
                if cells[W, 119] == 1 or cells[79, H] == 1 :
                    cells[W, HEIGHT] = 0
                    cells[WIDTH, H] = 0
        screen.fill(COLOR_GRID)
        
        if run:
            cells = undate(screen, cells, cellsize, with_porgress=True)
            pygame.display.update()
            
        time.sleep(0.0003)
        
if __name__ == '__main__':
    main()