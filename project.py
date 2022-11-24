from manim import *
import numpy as np 
class graficaXY(Scene):
    def construct(self):
        # Inicio de animacion
        titulo = Text("Ajuste por Mínimos Cuadrados").scale(0.5).to_edge(UP)
        self.play(Write(titulo), run_time = 1.7)
        axes = Axes(
            y_range=[-2,11,1],
            x_range = [-3,11,1],
            y_length= 7.2
        )
        axes.add_coordinates()
        self.play(Write(axes), run_rime = 2.8)
        self.wait(1.3)

        # Agregar puntos
        p1 = Dot((-2.5,-0.28,0), color=BLUE_B)
        labelP1 = Text("(1,4)").next_to(p1,RIGHT).scale(0.75)

        p2 = Dot((-5.1,0.3,0), color=BLUE_B)
        labelP2 = Text("(-2,5)").next_to(p2,DOWN).scale(0.75)

        p3 = Dot((-0.84,-3.11,0), color=BLUE_B)
        labelP3 = Text("(3,-1)").next_to(p3,DOWN).scale(0.6)
        
        p4 = Dot((0.05,-1.9,0), color=BLUE_B)
        labelP4 = Text("(4,1)").next_to(p4,RIGHT).scale(0.75)

        self.wait(1)
        self.play(GrowFromCenter(p1), run_rime = 1.8)
        self.play(Write(labelP1), run_rime = 1)
        self.wait(1)
        self.play(GrowFromCenter(p2), run_rime = 1.8)
        self.play(Write(labelP2), run_rime = 1)
        self.wait(1)
        self.play(GrowFromCenter(p3), run_rime = 1.8)
        self.play(Write(labelP3), run_rime = 1)
        self.wait(1)
        self.play(GrowFromCenter(p4), run_rime = 1.8)
        self.play(Write(labelP4), run_rime = 1)

        self.wait(2.7)
        # Grafica
        graph = axes.plot(
            lambda x: -0.88*x + 3.57,
            color = GREEN
        )
        self.play(Write(graph), run_time = 3.1)
        self.wait(4.7)

