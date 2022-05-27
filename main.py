import time
import pygame
import numpy as np

COLOR_GB = (10, 10 ,10)
COLOR_GRID = (40, 40, 40)
COLOR_DIE_NEXT = (170, 140, 140)
COLOR_ALIVE_NEXT =(255, 255, 255)
WIDTH, HEIGHT = 800, 600
cellsize = 10
hi, wow = 60, 80
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
                update_cells[row, col] = 1
                if with_porgress:
                    color = COLOR_ALIVE_NEXT
                    
        pygame.draw.rect(screen, color, (col * size, row * size, size - 1, size - 1) )
    
    return update_cells

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    
    cells = np.zeros((60, 80))
    screen.fill(COLOR_GRID)
    undate(screen, cells, cellsize)

    pygame.display.flip()
    pygame.display.update()
    
    run = False
    
    while True:
        for event in pygame.event.get():
            if  event.type == pygame.QUIT:
                pygame.quit()
                return
            elif event.type == pygame.KEYDOWN:
                if  event.key == pygame.K_SPACE:
                    print("space")
                    run = not run
                    undate(screen, cells, cellsize)
                    pygame.display.update()
            if pygame.mouse.get_pressed()[0]:
                pos = pygame.mouse.get_pos()
                cells[pos[1] // cellsize, pos[0] // cellsize] = 1
                undate(screen, cells, cellsize)
                pygame.display.update()
                
        screen.fill(COLOR_GRID)
        
        if run:
            cells = undate(screen, cells, cellsize, with_porgress=True)
            pygame.display.update()
            
        time.sleep(0.001)
        
if __name__ == '__main__':
    main()