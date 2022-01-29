import math
from lottie import Point, Color
from lottie.objects import easing
from lottie import objects

class Emotionless:
   def animate(an, layer):
      layer.transform.position.value = Point(116, 128)
      layer.transform.scale.value = Point(100, 100)
      easy = easing.EaseOut(1 / 4)

      # Scale
      layer.transform.scale.add_keyframe(0, Point(140, 140), easy)
      layer.transform.scale.add_keyframe(15, Point(120, 120), easy)
      layer.transform.scale.add_keyframe(30, Point(100, 100), easy)
      layer.transform.scale.add_keyframe(45, Point(120, 120), easy)
      layer.transform.scale.add_keyframe(60, Point(140, 140), easy)

      # Position
      layer.transform.position.add_keyframe(0,  Point(66, 64), easy)
      layer.transform.position.add_keyframe(15, Point(88, 96), easy)
      layer.transform.position.add_keyframe(30, Point(116, 128), easy)
      layer.transform.position.add_keyframe(45, Point(88, 96), easy)
      layer.transform.position.add_keyframe(60,  Point(66, 64), easy)

      # Color Effect
      last_frame = 60
      n_frames = 24
      for fill in layer.find_all((objects.Fill, objects.Stroke)):
         if isinstance(fill.color.value, list):
            import pdb; pdb.set_trace(); pass
         color = fill.color.value.converted(Color.Mode.LCH_uv)
      
         for frame in range(n_frames):
            off = frame / (n_frames-1)
            color.hue = (color.hue + math.tau / (n_frames-1)) % math.tau
            fill.color.add_keyframe(off * last_frame, color.to_rgb())
      
      
