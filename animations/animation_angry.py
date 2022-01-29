import random
import math
import grapheme
from lottie import Point, Color
from lottie.utils import color 
from lottie.utils.animation import shake
from lottie.objects import easing
from lottie.utils.font import FontStyle
from lottie import objects
from lottie.utils import animation as anutils
from lottie import PolarVector

class Angry:
   def animate(an, layer):
      layer.transform.position.value = Point(32, 96)
      layer.transform.scale.value = Point(120, 120) 

      easy = easing.EaseOut(1 / 4)
      layer.transform.scale.add_keyframe(0, Point(120, 120), easy)
      layer.transform.scale.add_keyframe(30, Point(130, 130), easy)
      layer.transform.scale.add_keyframe(60, Point(120, 120), easy)

      shake(layer.transform.position, 
         x_radius=6, 
         y_radius=6, 
         start_time=0, 
         end_time=60, 
         n_frames=60,
         interp=easing.EaseOut(1 / 10))
     
      style = FontStyle(
         "animations/assets/fonts/Pacifico-Regular.ttf", 300, 
         emoji_svg="animations/assets/emoji/"
      ) 

      particle_start = Point(216, 250)
      particle_scale = Point(16, 16)
      particle_end = Point(512, 512)
      partical_radius = 320.0
      start_len_min = 0
      start_len_max = 60
      opacity_start = 100
      opacity_end = 0
      last_frame = 60

      particle_count = 7
      elements = list(grapheme.graphemes("😡 😡 😡 😡"))
      le = len(elements)
      if le > 0:
         for i in range(0, particle_count):

            layer = objects.ShapeLayer()
            an.insert_layer(0, layer)
            t = layer.add_shape(style.render(elements[i % le]))
            layer.add_shape(objects.Fill(color.from_uint8(255, 83, 83)))
            layer.add_shape(objects.Stroke(Color(1, 1, 1), width=6)) 

            t.transform.position.value.y += t.line_height
            layer.transform.position.value = particle_start.clone()
            layer.transform.scale.value = particle_scale.clone()

            t = i / particle_count
            for thing in layer.shapes:
               if hasattr(thing,'opacity'):
                  thing.opacity.add_keyframe(0, opacity_start + (opacity_end - opacity_start) * t)
                  thing.opacity.add_keyframe((1 - t) * last_frame, opacity_end)
                  thing.opacity.add_keyframe((1 - t) * last_frame+1, opacity_start)
                  thing.opacity.add_keyframe(last_frame, opacity_start + (opacity_end - opacity_start) * t)
               elif hasattr(thing, 'shapes'):
                  for thingy in thing.shapes:
                     if hasattr(thingy, 'opacity'):
                        thingy.opacity.add_keyframe(0, opacity_start + (opacity_end - opacity_start) * t)
                        thingy.opacity.add_keyframe((1 - t) * last_frame, opacity_end)
                        thingy.opacity.add_keyframe((1 - t) * last_frame+1, opacity_start)
                        thingy.opacity.add_keyframe(last_frame, opacity_start + (opacity_end - opacity_start) * t)

            bezier = objects.Bezier()
            outp = PolarVector(random.uniform(start_len_min, start_len_max), random.random() * math.pi)
            angle = (random.random() * 2 - 1) * math.pi * 0.2
            particle_end = particle_start.clone()
            particle_end.x += partical_radius * math.cos(angle)
            particle_end.y += partical_radius * math.sin(angle)
            bezier.add_point(particle_start, outp=outp)
            bezier.add_point(particle_end, outp)

            anutils.follow_path(layer.transform.position, bezier, 0, last_frame, 10, start_t=t)