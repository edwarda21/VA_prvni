import pygame as pg
pg.init()

def resize_percentage(target_rect, percentage_x = 100, percentage_y = 100):
    height = target_rect.get_rect().height/100*percentage_x 
    width = target_rect.get_rect().width/100*percentage_y
    return height,width
def resize_percentage_circle(target_rect,percentage_r = 100):
    return (r/100*percentage_r)

screen = pg.display.set_mode([900,900], pg.RESIZABLE)
running = True
while running:
    SCREEN_WIDTH = screen.get_rect().width
    SCREEN_HEIGHT = screen.get_rect().height
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
    screen.fill((255,255,255))
    pg.draw.circle(screen,(55,155,255),(SCREEN_WIDTH/2, SCREEN_HEIGHT/2),resize_percentage_circle(75,))
    pg.display.update()

pg.quit()
    