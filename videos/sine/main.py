from manimlib import *

class SineCurveScene(InteractiveScene):
    def construct(self):
        y_range = 3
        frame = self.frame
        axes = Axes(
            x_range=(0, 10),
            y_range=(-y_range, y_range)
        )
        self.add(axes)
        
        sin_graph = always_redraw(axes.get_graph(
            lambda x: 2 * math.sin(x/2),
            color=BLUE,
        ))
        
        #sin_label = always_redraw(axes.get_graph_label(sin_graph, "\\sin(x)"))
        self.embed()
        #some comment
        self.add(sin_graph)
        self.add(sin_label)


