from manim import *
from numpy import *

class Circunferencia(Scene):
    def construct(self):
        
        circulo = Circle(radius = 2, color = BLUE)
        
        self.play(Create(circulo), run_time=3)
        self.wait(2)