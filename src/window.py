#!/usr/bin/env python3
# coding: utf8
import os, pyxel
class App:
    def __init__(self):
        self.palette = Palette()
        self.window = Window()
        pyxel.run(self.update, self.draw)
    def update(self): self.window.update()
    def draw(self):
        pyxel.cls(0)
        self.palette.draw()

class Window:
    def __init__(self):
        self.__palette = Palette()
        self.__init()
    @property
    def Width(self): return 128
    @property
    def Height(self): return 32
    @property
    def Caption(self): return "init() pallet"
    @property
    def BorderWidth(self): return 0
    def update(self): pass
    def draw(self): self.Palette.draw()
    @property
    def Palette(self): return self.__palette
    def __init(self):
        pyxel.init(self.Width, self.Height, border_width=self.BorderWidth, caption=self.Caption, palette=self.Palette.Colors)

class Palette:
    def __init__(self):
        self.__fid = 0
        self.load_palette()
    def draw(self):
        for c in range(len(self.__colors)):
            pyxel.rect(0 + ((c % 8) * 16), 0 + (int(c / 8) * 16), 16, 16, c)
    def load_palette(self):
        with open(self.__palette_file_path(self.__fid), 'r') as f:
            self.__colors = list(map(lambda l: int(l, 16), f))
            print(self.__colors)
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

