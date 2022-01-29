from lottie import Point, Color
from lottie.utils import color 
from lottie.utils.animation import shake
from lottie import objects
from lottie.objects import easing
from lottie.objects.text import TextJustify
from lottie.utils.font import FontStyle

import os
import sys
sys.path.insert(0, os.path.join(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
    "lib"
))
import copy

class Please:
   def animate(an, layer):
      layer.transform.position.value = Point(88, 64)
      layer.transform.scale.value = Point(120, 120)

      easy = easing.EaseOut(1 / 4)

      text_layer = objects.ShapeLayer()
      an.insert_layer(0, text_layer)
      style = FontStyle("Ubuntu", 64, emoji_svg="animations/assets/twemoji/assets/svg/")
      t = text_layer.add_shape(style.render("\U0001F607")) 
      t.transform.position.value.y += t.line_height + 48
      t.transform.position.value.x += 54

      shake(text_layer.transform.position, 
         x_radius=5, 
         y_radius=5, 
         start_time=0, 
         end_time=59, 
         n_frames=25,
         interp=easy)

      text_layer = objects.ShapeLayer()
      an.add_layer(text_layer)
      style = FontStyle("animations/assets/fonts/Pacifico-Regular.ttf", 64, justify=TextJustify.Center)
      t = text_layer.add_shape(style.render("Pleeeease")) 
      t.transform.position.value.x = 184
      t.transform.position.value.y = 274
      text_layer.add_shape(objects.Fill(color.from_uint8(255, 83, 83))) 
      stroke = text_layer.add_shape(objects.Stroke(Color(1, 1, 1), 12))

      point = copy.deepcopy(t.transform.position.value)
      easy = easing.Sigmoid(0)
      text_layer.transform.position.add_keyframe(0, Point(point.x-120, point.y-64), easy)
      text_layer.transform.position.add_keyframe(20, Point(point.x-80, point.y-64), easy)
      text_layer.transform.position.add_keyframe(40, Point(point.x-160, point.y-64), easy)
      text_layer.transform.position.add_keyframe(60, Point(point.x-120, point.y-64), easy)
      
      text_layer = objects.ShapeLayer()
      an.insert_layer(0, text_layer)
      style = FontStyle("Ubuntu", 64, emoji_svg="animations/assets/twemoji/assets/svg/")
      t = text_layer.add_shape(style.render("\U0001F607")) 
      t.transform.position.value.y += t.line_height + 42
      t.transform.position.value.x += 338

      shake(text_layer.transform.position, 
         x_radius=5, 
         y_radius=5, 
         start_time=0, 
         end_time=59, 
         n_frames=25,
         interp=easy)