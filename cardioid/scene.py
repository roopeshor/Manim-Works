from manim import *
from math import *
import numpy as np

def arr (x, y, z = 0):
	return np.array([x, y, z])

class MmodNTracker(Scene):
	def construct(self):
		circle = Circle(radius=3)
		mod_tracker = ValueTracker(0)
		self.number_of_lines = 400
		self.gradient_colors = [RED,YELLOW,BLUE]
		self.end_value = 100
		self.total_time = 180

		lines = self.get_m_mod_n_objects(circle,mod_tracker.get_value())
		lines.add_updater(
			lambda mob: mob.become(
				self.get_m_mod_n_objects(circle,mod_tracker.get_value())
				)
			)
		self.add(circle,lines)
		self.wait(3)
		self.play(
			mod_tracker.animate.set_value(self.end_value),
      rate_func=linear, run_time=180
		)
		self.wait(3)

	def get_m_mod_n_objects(self,circle,x,y=None):
		if y==None:
			y = self.number_of_lines
		lines = VGroup()
		for i in range(y):
			start_point = circle.point_from_proportion((i%y)/y)
			end_point = circle.point_from_proportion(((i*x)%y)/y)
			line = Line(start_point,end_point).set_stroke(width=1)
			lines.add(line)
		lines.set_color_by_gradient(*self.gradient_colors)
		return lines
