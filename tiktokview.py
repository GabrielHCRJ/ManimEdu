from manim import *
from numpy import *

SCALE_FACTOR=1
tmp_pixel_height=config.pixel_height
config.pixel_height = config.pixel_width
config.pixel_width = tmp_pixel_height

config.frame_height = config.frame_height / SCALE_FACTOR
config.frame_width = config.frame_height *9/16

FRAME_HEIGHT=config.frame_height
FRAME_WIDTH=config.frame_width

class TikTokView(MovingCameraScene):  
     
     def setup(self, add_border=True):
        if add_border:
            self.border=Rectangle(
                width=FRAME_WIDTH,
                height=FRAME_HEIGHT,
                color=WHITE
            )
     def construct(self):
         pass