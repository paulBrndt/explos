from manimlib import *


CIRCLE = BLUE
DOT = RED
TRIANGLE = TEAL
ANGLE = PURPLE
RADIUS = GREEN
BETA = YELLOW

class ThalesScene(InteractiveScene):

    def getNormalized(self, first, second, center):
        v1 = normalize(first - center)
        v2 = normalize(second - center)

        return (v1, v2)
    
    def getAngleLabel(self, first, second, center, name = "alpha", positionDOWN = 1, color = ANGLE):
        (v1, v2) = self.getNormalized(first, second, center)
        angleRad = np.arccos(np.clip(np.dot(v1, v2), -1.0, 1.0))
        angleDeg = np.degrees(angleRad)

        text = Tex(R"\{name} = {deg:.1f}^\circ".format(name=name, deg=angleDeg))
        text = text.to_edge(LEFT)
        text = text.shift(positionDOWN * DOWN)
        text.set_color(color)

        return text


    def getAngleArc(self, first, second, center, radius = 0.5, color = BLACK, opacity = 1):
            (v1, v2) = self.getNormalized(first, second, center)

            startAngle = np.arctan2(v2[1], v2[0])
            endAngle = np.arctan2(v1[1], v1[0])

            angle = (endAngle - startAngle) % TAU

            if angle > PI:
                angle -= TAU

            return Arc(
                radius=radius,
                start_angle=startAngle,
                angle=angle,
                arc_center=center,
                color=color,
                opacity=opacity
            )



    def getAlpha(self):
        return self.getAngleArc(
            self.circle.get_left(),
            self.circle.get_right(),
            self.P.get_center(),
            color=ANGLE
        )
    
    def getAlphaLabel(self):
        return self.getAngleLabel(
            self.circle.get_left(),
            self.circle.get_right(),
            self.P.get_center()
        )

    def getBeta(self):
       return self.getAngleArc(
           self.P.get_center(),
           self.circle.get_left(),
           self.circle.get_right(),
           color=BETA
       )
    
    def getBetaLabel(self):
        return self.getAngleLabel(
           self.P.get_center(),
           self.circle.get_left(),
           self.circle.get_right(),
           name="beta",
           color=BETA
        )


    def construct(self):
        # ---------- TRACKERS ----------
        self.radiusTracker = ValueTracker(1)
        self.theta = ValueTracker(2 * PI)
        self.midpointCoord = ORIGIN

        # ---------- CIRCLE ----------
        self.introWords = Text("""
            Lass uns einen Kreis zeichnen
                          """)  
        self.introWords.to_edge(UP)


        self.circle = always_redraw(lambda:
                Circle(stroke_color=CIRCLE, radius=self.radiusTracker.get_value())
                )
        
        self.midpoint = Dot(self.midpointCoord, radius=0.1, fill_color=RADIUS)

        # ---------- DIAMETER ----------

        self.diameter = always_redraw(lambda:
            Line(self.circle.get_left(), self.circle.get_right(), color=RADIUS)
        )

        self.diameterLabel = always_redraw(lambda:
                Tex("{:.2f}".format(self.radiusTracker.get_value()))
                .to_edge(LEFT)
                .shift(UP)
                .set_fill(RADIUS)
                )
        
        # ---------- DOT ----------


        def getP():
            angle = self.theta.get_value()
            direction = np.array([np.cos(angle), np.sin(angle), 0])
            return Dot(self.midpointCoord + self.radiusTracker.get_value() * direction, radius=0.1, fill_color=DOT)
        
        self.P = always_redraw(getP)


        self.PLabel = always_redraw(lambda: 
            Tex("({:.2f}, {:.2f})".format(self.P.get_x(), self.P.get_y()))
            .set_fill(RED)
            .to_edge(LEFT)
        )


        # ---------- RADIUS ----------
        self.radius = always_redraw(lambda:
                                    Line(self.circle.get_center(), self.P.get_center(), color=RADIUS)
                                    )

        self.radiusLabel = always_redraw(lambda:
                Tex("{:.2f}".format(self.radiusTracker.get_value()))
                .to_edge(LEFT)
                .set_fill(RADIUS)
                )


        # ---------- TRIANGLE ----------

        self.triangle = always_redraw(lambda:
                                      Polygon(self.circle.get_right(), self.circle.get_left(), self.P.get_center(), color=TRIANGLE, fill_color=TRIANGLE, fill_opacity=0.5)
                                      )
        
        self.lineL = always_redraw(lambda:
                                   Line(self.circle.get_left(), self.P.get_center())
                                   )
        
        self.lineR = always_redraw(lambda:
                                   Line(self.circle.get_right(), self.P.get_center())
                                   )
        





        # ---------- ANGLES ----------

        self.alpha = always_redraw(self.getAlpha)
        self.alphaLabel = always_redraw(self.getAlphaLabel)

        # ---------- BOXES ----------

        self.box = SurroundingRectangle(
            self.alphaLabel, color = ANGLE, buff = 0.2
        )


        # ---------- SUPPORT-ANGLES ----------

        self.beta = always_redraw(self.getBeta)
        self.betaLabel = always_redraw(self.getBetaLabel)

        # ---------- Z-INDEX ----------

        self.circle.z_index = 0
        self.triangle.z_index = 1
        self.diameter.z_index = 2
        self.midpoint.z_index = 3
        self.P.z_index = 3
        self.alpha.z_index = 4

        # ---------- ANIMATION ----------

        # add Intro and Circle
       # self.play(Write(self.introWords))
        self.play(
            ShowCreation(self.circle)
        )

        self.add(self.midpoint)
        self.wait(.5)
        #Add Diameter
        
        self.play(
            ShowCreation(self.diameter),
        )

        self.play(
            Write(self.diameterLabel)
        )

        #Add Point and Label

        self.play(
            ShowCreation(self.P),
        )

        self.play(
            Write(self.PLabel)
        )


        # #Add Radius

        self.play(
             ShowCreation(self.radius),
        )

        #Move stuff around

        self.play(
            self.radiusTracker.animate.set_value(3),
        )

        self.play(
            self.theta.animate.set_value(0), run_time=2
        )

        self.play(
            self.theta.animate.set_value(PI / 4), run_time=2
        )

        self.play(
            FadeIn(self.triangle)
        )

        self.play(
            ShowCreation(self.alpha),
            Write(self.alphaLabel)
        )

        self.play(
            self.theta.animate.set_value(self.theta.get_value() + 2 * PI), run_time = 5
        )

        # BUT WHY

        self.play(
            ShowCreation(self.beta),
        )

        self.play(
            Write(self.betaLabel)
        )
        self.embed()