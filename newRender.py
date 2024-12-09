from manim import *


class Example(ZoomedScene):
    def construct(self):
        vals = [1, 2, 3, 4] #HEREFROM
        labels = [
            'foo',
            'bar',
            'foo3',
            'foo2',
        ]
        colors = ['#58508d', '#58508d', '#bc5090', '#bc5090']
        bar = BarChart(
            vals,
            bar_colors=colors,
            bar_names=labels,
        ) #HERETO
        self.play(Create(bar),run_time=5) 
       