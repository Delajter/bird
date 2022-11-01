
import pygame as pg
import sys
from lib import *
import time
from game import*


def menu(proc):

    mouse = Mouse_and_menu()
    wall = pg.Rect(0, 0, 1920, 1080)
    pg.init()
    win = pg.display.set_mode()
    background = pg.image.load("img/wall.png")
    background = pg.transform.scale(background, (1920, 1080)).convert()

    # pg.mouse.set_visible(0)
    mouse.body.center = mouse.play_button.center
    chose = 0
    while proc is True:
        win.fill((201, 201, 201))

        for event in pg.event.get():
            if event.type == pg.QUIT:
                proc = False
                sys.exit(0)

        userInput = pg.key.get_pressed()
        if userInput[pg.K_ESCAPE]:
            proc = False
            sys.exit(0)

        if userInput[pg.K_w]:
            if chose is not 0:
                chose -= 1
                time.sleep(0.15)

        if userInput[pg.K_s]:
            if chose is not 3:
                chose += 1
                time.sleep(0.2)

        if userInput[pg.K_RETURN]:
            if chose == 0:
                ptk = game(True)
                mouse.score_lbl = mouse.my_font.render(
                    str(f'SC:{ptk}'), False, (255, 255, 255))

            if chose == 1:
                proc = False
            if chose == 2:
                pass  # !----------------------------------------------------
            if chose == 3:
                pass

        for i in range(len(mouse.BUTTON_TABLE)):
            if chose is i:
                mouse.body.center = mouse.BUTTON_TABLE[i].center
        win.blit(background, wall)
        pg.draw.rect(win, (255, 0, 0), mouse.body)
        pg.draw.rect(win, (0, 255, 0), mouse.play_button)
        pg.draw.rect(win, (0, 255, 0), mouse.quit_button)
        pg.draw.rect(win, (0, 255, 0), mouse.top_points_button)
        pg.draw.rect(win, (0, 255, 0), mouse.your_points_button)
        map.win.blit(mouse.paly_lbl,
                     ((mouse.play_button.x+mouse.button_w/2-mouse.paly_lbl.get_width()/2), (mouse.play_button.y+mouse.button_h/2-mouse.paly_lbl.get_height()/2)))

        map.win.blit(mouse.quit_lbl,
                     ((mouse.quit_button.x+mouse.button_w/2-mouse.quit_lbl.get_width()/2), (mouse.quit_button.y+mouse.button_h/2-mouse.quit_lbl.get_height()/2)))

        map.win.blit(mouse.top_lbl,
                     ((mouse.top_points_button.x+mouse.button_w/2-mouse.top_lbl.get_width()/2), (mouse.top_points_button.y+mouse.button_h/2-mouse.top_lbl.get_height()/2)))
        map.win.blit(mouse.score_lbl,
                     ((mouse.your_points_button.x+mouse.button_w/2-mouse.score_lbl.get_width()/2), (mouse.your_points_button.y+mouse.button_h/2-mouse.score_lbl.get_height()/2)))
        pg.time.delay(5)
        pg.display.update()


if __name__ == '__main__':
    menu(True)
    sys.exit(0)
