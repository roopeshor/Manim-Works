
from manim import *
import numpy as np

SHIFT  = np.array([-1.5, -2, 0])
ang    = PI/4
circle = Circle(radius=5, color=None).set_stroke(GRAY, opacity=0.5)
dot    = Dot(point=circle.point_from_proportion(ang/TAU))
dot_center= dot.get_center()

def get_unit_line (u_brace=False, u_brace_ang=PI/2):
  unit_line = Line(
    start=ORIGIN,
    end=dot_center
  )
  unit_line_brace = rotated_brace(unit_line, "1", u_brace_ang)
  g = Group(unit_line)
  if u_brace: g.add(unit_line_brace)
  return g
def basis (u_brace=True, u_brace_ang=PI/2):
  axes = Axes(tips=False, axis_config={
      "include_ticks": False
  }, x_length=100, y_length=100)
 
  
  g = Group(
    axes,
    circle,
    theta(),
    get_unit_line(u_brace, u_brace_ang),
    dot,
  )
  return g.shift(SHIFT)
def theta ():
  th = Angle(
    line1=Line(start=ORIGIN, end=np.array([1, 0, 0])),
    line2=Line(start=ORIGIN, end=dot_center),
  )
  theta_text = MathTex("\\theta").next_to(ORIGIN, np.array([2, 0.5, 0.0]))

  return Group(th, theta_text)
def sin_cos ():
  sin_line = Line(
    start=dot_center,
    end=np.array([dot_center[0], 0, 0])
  )
  cos_line = Line(
    start=ORIGIN,
    end=np.array([dot_center[0], 0, 0])
  )
  cos_brace = Brace(cos_line)
  cos_brace_text = cos_brace.get_tex("cos(\\theta)", buff=0.08)
  
  _sin = Group(
    sin_line,
    rotated_brace(sin_line, "sin(\\theta)", PI/2, -0.3, PI/2)
  ).set_color(GREEN_C)

  _cos = Group(
    cos_line,
    cos_brace,
    cos_brace_text
  ).set_color(YELLOW_C)

  return Group(_sin, _cos).shift(SHIFT)

class Sin_And_Cos (Scene):
  def construct(self):
    self.add(basis(), sin_cos())

