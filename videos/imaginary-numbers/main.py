from manimlib import *

class IntroductionScene(InteractiveScene):
	def construct(self):
		# axes
		frame = self.frame
		axes = ThreeDAxes()
		self.add(axes)

		self.embed()