
import random as r
import pygame as pg
import sys


class Color:
    def __init__(self):
        self.l_gray = (201, 201, 201)
        self.d_gray = (77, 77, 77)
        self.red = (255, 0, 0)


class MapTails:
    def __init__(self):
        self.paint = Color()
        self.win = pg.display.set_mode()
        self.screen_x = self.win.get_width()
        self.screen_y = self.win.get_height()
        self.sieze_of_table = 350
        self.points = 0
        self.score = 0
        # borders
        self.border_l = pg.Rect(0, 0, self.screen_x/4, self.screen_y)
        self.border_r = pg.Rect((self.screen_x/4)*3, 0,
                                self.screen_x/4, self.screen_y)
        self.border_top = pg.Rect(0, 0, self.screen_x, self.screen_y/50)
        self.bg = pg.Rect(self.screen_x/4, 0, self.screen_x/2, self.screen_y)
        # points
        self.score = 0
        pg.font.init()
        self.my_font = pg.font.SysFont(pg.font.get_default_font(), 600)
        self.point_bg = pg.Rect((self.screen_x/2-self.sieze_of_table/2, self.screen_y/2-self.sieze_of_table/2),
                                (self.sieze_of_table, self.sieze_of_table))
        self.points_lbl = self.my_font.render(
            str(self.points), False, self.paint.l_gray)

        # enemy
        self.spike_size = 100

        self.spike_r_1 = pg.Rect(0, 0, self.spike_size, self.spike_size)
        self.spike_r_2 = pg.Rect(0, 0, self.spike_size, self.spike_size)
        self.spike_r_3 = pg.Rect(0, 0, self.spike_size, self.spike_size)
        self.spike_r_4 = pg.Rect(0, 0, self.spike_size, self.spike_size)
        self.spike_r_5 = pg.Rect(0, 0, self.spike_size, self.spike_size)
        self.spike_r_6 = pg.Rect(0, 0, self.spike_size, self.spike_size)
        self.spike_r_7 = pg.Rect(0, 0, self.spike_size, self.spike_size)
        self.Spike_r = [self.spike_r_1, self.spike_r_2, self.spike_r_3,
                        self.spike_r_4, self.spike_r_5, self.spike_r_6, self.spike_r_7]
        self.spike_s = pg.Surface(
            (self.spike_size, self.spike_size)).convert_alpha()
        pg.Surface.fill(self.spike_s, self.paint.d_gray)
        self.roteted_spike_1 = pg.transform.rotate(self.spike_s, 45)
        self.roteted_spike_2 = pg.transform.rotate(self.spike_s, 45)
        self.roteted_spike_3 = pg.transform.rotate(self.spike_s, 45)
        self.roteted_spike_4 = pg.transform.rotate(self.spike_s, 45)
        self.roteted_spike_5 = pg.transform.rotate(self.spike_s, 45)
        self.roteted_spike_6 = pg.transform.rotate(self.spike_s, 45)
        self.roteted_spike_7 = pg.transform.rotate(self.spike_s, 45)

        # pg.transform.scale(self.spike, (self.spike_size, self.spike_size*2))
        self.Roteted_spike = [self.roteted_spike_1, self.roteted_spike_2, self.roteted_spike_3,
                              self.roteted_spike_4, self.roteted_spike_5, self.roteted_spike_6, self.roteted_spike_7]

    def turn(self):
        for i in range(7):
            self.Spike_r[i].y = self.screen_y*2

            self.win.blit(self.Roteted_spike[i], self.Spike_r[i])
        many = r.randint(3, 7)  # {1,7}
        # self.spike_r.x = self.screen_x/4-self.spike_size+self.screen_x/64
        for i in range(many):
            place = r.randint(1, 8)  # {1,8}*lp index
            location = (r.randint(0, 7))*135  # 135*lp
            self.Spike_r[i].y = location
            self.win.blit(self.Roteted_spike[i], self.Spike_r[i])
        self.score += 1


class Mouse_and_menu:
    def __init__(self):
        map = MapTails()
        pg.font.init()
        self.my_font = pg.font.SysFont(pg.font.get_default_font(), 100)
        self.paly_lbl = self.my_font.render(
            str('PLAY'), False, (255, 255, 255))
        self.quit_lbl = self.my_font.render(
            str('QUIT'), False, (255, 255, 255))
        self.top_lbl = self.my_font.render(
            str('TOP'), False, (255, 255, 255))
        self.score_lbl = self.my_font.render(
            str('SC'), False, (255, 255, 255))

        self.width = 400
        self.height = 100
        self.menu_buttons_y = map.screen_y/2
        self.mouse_x = map.screen_x/2-self.width/2
        self.mouse_y = map.screen_y/2-self.height/2
        self.body = pg.Rect(self.mouse_x, self.mouse_y,
                            self.width, self.height)
        self.button_w = self.width/10*9
        self.button_h = self.height/4*3

        self.button_space = map.screen_y/10.8
        self.play_button = pg.Rect(
            self.mouse_x, self.menu_buttons_y, self.button_w, self.button_h)
        self.menu_buttons_y += self.button_space
        self.quit_button = pg.Rect(
            self.mouse_x, self.menu_buttons_y, self.button_w, self.button_h)

        self.menu_buttons_y += self.button_space
        self.top_points_button = pg.Rect(
            self.mouse_x, self.menu_buttons_y, self.button_w, self.button_h)
        self.menu_buttons_y += self.button_space
        self.your_points_button = pg.Rect(
            self.mouse_x, self.menu_buttons_y, self.button_w, self.button_h)
        self.BUTTON_TABLE = [self.play_button, self.quit_button,
                             self.top_points_button, self.your_points_button]


class Player:
    def __init__(self):
        self.map = MapTails()
        self.b_size = 80
        self.speed = 5
        self.speed_backup = 0
        self.way = True
        self.pause_var = False

        self.body = pg.Rect((self.map.screen_x/2-self.b_size),
                            (self.map.screen_y/2-self.b_size), self.b_size, self.b_size)
        # self.skin = pg.Surface((self.b_size, self.b_size))
        self.bird_old_place = 0

    def pause(self):
        if self.pause_var is False:
            self.pause_var = True
            self.speed_backup = self.speed
            self.speed = 0
        elif self.pause_var is True:
            self.pause_var = False
            self.speed = self.speed_backup

    def move_to_right(self, way):
        if way is True:
            self.body.x += self.speed
        else:
            self.body.x -= self.speed

    def check_side(self):
        if self.body.x >= (self.map.screen_x/4)*3-self.b_size-self.speed:
            self.way = False

        if self.body.x <= (self.map.screen_x/4)+self.speed:
            self.way = True

    def gravity(self):
        self.body.y += self.speed/2
