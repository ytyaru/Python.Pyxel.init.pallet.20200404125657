#!/usr/bin/env python3
# coding: utf8
import os, glob, pyxel
class App:
    def __init__(self):
        self.palette = Palette()
        self.window = Window()
#        pyxel.init(self.window.Width, self.window.Height, border_width=0, caption=self.window.Caption, palette=self.palette.Colors)
        pyxel.run(self.update, self.draw)
    def update(self): self.window.update()
    def draw(self):
        pyxel.cls(0)
        self.palette.draw()
        pyxel.text(0, 0, 'Press the SPACE key: ' + str(self.palette.FileId) + "\npyxel error: failed to initialize SDL Audio in 'Audio'", 7)

class Window:
    def __init__(self):
        self.__palette = Palette()
        self.__init()
    @property
    def Width(self): return 256
    @property
    def Height(self): return 96
    @property
    def Caption(self): return "init() palette. SPACEキー押下して2回目のinit()するとpyxel error: failed to initialize SDL Audio in 'Audio'"
    @property
    def BorderWidth(self): return 0
    def update(self): 
        if pyxel.btnp(pyxel.KEY_SPACE):
            self.Palette.update()
#            pyxel.init(self.Width, self.Height, self.border_width=self.BorderWidth, caption=self.Caption, palette=self.Palette.Colors)
            self.__init()
    def draw(self): self.Palette.draw()
    @property
    def Palette(self): return self.__palette
    def __init(self):
        pyxel.init(self.Width, self.Height, border_width=self.BorderWidth, caption=self.Caption, palette=self.Palette.Colors)

class Palette:
    def __init__(self):
        self.__fid = 0
        self.get_palette_file_list()
        self.load_palette()
    def update(self):
#        if pyxel.btnp(pyxel.KEY_SPACE):
#            self.__increment_file_id()
#            self.load_palette()
        self.__increment_file_id()
        self.load_palette()

    def draw(self):
        for c in range(len(self.__colors)):
            pyxel.rect(0 + ((c % 8) * 16), 10 + (int(c / 8) * 16), 16, 16, c)
    def get_palette_file_list(self):
        self.__files = glob.glob(os.path.join(self.ResDir, '*'))
    def load_palette(self):
        with open(self.__files[self.__fid], 'r') as f:
            self.__colors = list(map(lambda l: int(l, 16), f))
#            print(self.__colors)
    def __increment_file_id(self):
        if self.__fid < len(self.__files) - 1: self.__fid += 1
        else: self.__fid = 0
    def __palette_file_path(self, pid=0): return os.path.join(self.ResDir, self.__palette_file_name(pid))
    def __palette_file_name(self, pid=0): return 'palette' + str(pid) + '.txt'
    @property
    def FileId(self): return self.__fid
    @property
    def Colors(self): return self.__colors
    @property
    def ResDir(self):
        this = os.path.abspath(__file__)
        here = os.path.dirname(this)
        parent = os.path.dirname(here)
        return os.path.join(parent, 'res')

App()

