from manimlib import *

## GETTING INTO MANIM

class TransformTex(Scene):
    def construct(self):
        #Label Function F1
        self.f1 = Tex(r"f(x)=\frac{1}{5x}")
        self.f1.to_corner(UL)
        
        #Label Function F2
        self.f2 = Tex(r"f(x)*5x=1")
        self.f2.to_corner(UL)
        
        self.play(Write(self.f1))
        self.wait()
        self.play(TransformMatchingTex(self.f1, self.f2))
        
        self.embed()
        
        
class TransformShapes(Scene):
    def construct(self):
        #declare stuff
        self.circle = Circle()
        self.square = Square()
        
        #animate
        self.play(ShowCreation(self.circle))
        self.wait()
        self.play(ReplacementTransform(self.circle, self.square))
        
        self.embed()
        
        
class PointyArrowScene(Scene):
    def construct(self):
        #declare arrow
        self.arrow = Arrow(LEFT, RIGHT)
        self.arrow.scale(1.5)
        
        #declare text
        self.definition = Text("Hi there, I want to tell you something!", font_size=20)
        self.definition.next_to(self.arrow, LEFT)
        
        #animate stuff
        self.play(ShowCreation(self.arrow))
        self.wait()
        self.play(Write(self.definition))
        
        self.play(
            self.definition.animate.next_to(self.arrow)
        )
        
        self.play(
            self.arrow.animate.rotate(TAU / 2)
        )
        
        self.embed()
        
class CoordinateSystem(Scene):
    def construct(self):
        x_range=(-1, 10)
        #create axes
        axes = Axes(
            x_range=x_range,
            y_range=(-1, 6),
            height=6,
            width=10
        )
        axes.add_coordinate_labels(font_size=20, num_decimal_places=1)
        self.add(axes)
        
        # add point
        function = axes.get_graph(lambda x: x*1/2+1, x_range=x_range)
        function.color = RED
        
        x_tracker = ValueTracker(5)
        dot = Dot()
        dot.move_to(axes.i2gp(2, function))
        h_line = always_redraw(lambda: axes.get_h_line(dot.get_bottom()))
        v_line = always_redraw(lambda: axes.get_v_line(dot.get_left()))
        
        self.play(FadeIn(dot, scale=.5))
        self.wait()

        h_line = always_redraw(lambda: axes.get_h_line(dot.get_left()))
        v_line = always_redraw(lambda: axes.get_v_line(dot.get_bottom()))
        
        self.play(
            ShowCreation(h_line),
            ShowCreation(v_line),
        )
        self.wait()

        self.play(
            dot.animate.move_to(axes.i2gp(x_tracker.get_value(), function))
        )
        self.wait()
        
        dot.add_updater(lambda m: m.move_to(axes.i2gp(x_tracker.get_value(), function)))
        
        self.play(x_tracker.animate.set_value(1), run_time=3)
        self.play(x_tracker.animate.set_value(9), run_time=3)

        
        self.embed()
        
class ParabolaExample(Scene):
    def construct(self):
        pass
        