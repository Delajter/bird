
import pygame as pg
import time
from lib import*

map = MapTails()
paint = Color()
bird = Player()


def game(continued):
    pg.init()
    map.points = 0
    map.score = 0

    map.win.fill(paint.l_gray)
    pg.draw.rect(map.win, paint.d_gray, map.border_l)
    pg.draw.rect(map.win, paint.d_gray, map.border_r)
    # pg.draw.rect(map.win, paint.d_gray, map.border_top)

    while continued is True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                continued = False
        userInput = pg.key.get_pressed()
        if userInput[pg.K_ESCAPE]:
            continued = False

        bird.check_side()
        # points adding--------------------------------------------------------------------------------------------------
        if bird.bird_old_place > bird.body.x and bird.way is True:
            map.points += 1
            map.points_lbl = map.my_font.render(
                str(map.points), False, paint.l_gray)
            for i in range(7):
                map.Spike_r[i].x = (map.screen_x/4)*3 - \
                    map.spike_size+map.screen_x/64*3.1  # !---------------------------------------------

            map.turn()
        if bird.bird_old_place < bird.body.x and bird.way is False:
            map.points += 1
            map.points_lbl = map.my_font.render(
                str(map.points), False, paint.l_gray)
            for i in range(7):
                # *---------------------------------------------
                map.Spike_r[i].x = map.screen_x / \
                    4-map.spike_size-map.screen_x/64+map.screen_x/53
            map.turn()
        bird.bird_old_place = bird.body.x
        bird.move_to_right(bird.way)
        # drawing--------------------------------------------------------------------------------------------------------
        pg.draw.rect(map.win, paint.l_gray, map.bg)
        pg.draw.rect(map.win, paint.d_gray, map.point_bg,
                     map.sieze_of_table, map.sieze_of_table)
        map.win.blit(map.points_lbl, (map.screen_x/2 -
                     map.sieze_of_table/3+map.screen_x/384, map.screen_y/2-map.sieze_of_table/2-map.screen_y/108))
        pg.draw.rect(map.win, paint.red, bird.body)
        for i in range(7):
            if not bird.way:
                map.win.blit(
                    map.Roteted_spike[i], (map.screen_x / 4-map.spike_size+map.screen_x/64, map.Spike_r[i].y))
            else:
                map.win.blit(map.Roteted_spike[i], ((map.screen_x/4)*3 -
                                                    map.spike_size+map.screen_x/64, map.Spike_r[i].y))
        # movement-------------------------------------------------------------------------------------------------------
        bird.gravity()
        if userInput[pg.K_p]:
            bird.pause()
        if userInput[pg.K_w] and bird.pause_var is False:
            if bird.body.y-bird.speed*3 > 0:
                bird.body.y -= bird.speed*3
        # points---------------------------------------------------------------------------------------------------------
        if map.points >= 9:
            map.points = 0
            bird.speed += 1
        # dead-----------------------------------------------------------------------------------------------------------
        if bird.body.y > bird.map.screen_y:
            time.sleep(1.5)
            continued = False

        for i in range(7):
            if bird.body.colliderect(map.Spike_r[i]):
                time.sleep(1.5)
                continued = False

                # sys.exit(0)  # ?----------------------------------------------

        # game loop settings --------------------------------------------------------------------------------------------
        pg.time.delay(5)
        pg.display.update()
    return map.score


# if __name__ == '__main__':
#     game(True)
#     sys.exit(0)
