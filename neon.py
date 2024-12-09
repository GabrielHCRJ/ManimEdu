from manim import *

class NeonLine(Scene):
    def construct(self):
        # Define as cores neon
        neon_color = "#39FF14"  # Verde neon
        
        # Crie a linha
        line = Line(start=3*LEFT, end=3*RIGHT, color=neon_color)
        
        # Adicione um brilho à linha para o efeito neon
        glow = line.copy().set_stroke(width=10, opacity=0.1).set_color(neon_color)
        
        # Adicione os objetos à cena
        
        self.play(Create(line),Create(glow),run_time=5)

# Para renderizar a cena, você precisa executar o comando correspondente no terminal:
# manim -pql <nome_do_seu_arquivo>.py NeonLine
