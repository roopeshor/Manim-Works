from manim import *
from manim_editor import PresentationSectionType

def arr (x, y, z = 0):
  return np.array([x, y, z])

class Test(Scene):
  def construct(self):
    self.next_section(type=PresentationSectionType.NORMAL)
    t = Text("Hello World")
    c = Circle(radius=1.2, color=YELLOW)
    r = Rectangle(height=2, width=3, color=BLUE)
    self.play(Write(t), run_time=2)
    self.wait(1)
    self.next_section(type=PresentationSectionType.NORMAL)
    self.play(t.animate.move_to(arr(0, 3)), run_time=1)
    self.play(Create(c), run_time=1)
    self.wait(1)
    self.play(Transform(c, r), run_time=1)
    self.wait(1)
    # self.next_section("Names are still supported.", type=PresentationSectionType.SKIP)
