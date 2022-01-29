from lottie import Point, Color
from lottie.objects.text import TextJustify
from lottie.utils import color 
from lottie.utils.animation import follow_path
from lottie.objects import easing
from lottie.utils.font import FontStyle
from lottie import objects
from lottie.parsers.svg import parse_svg_file

import os
import sys
sys.path.insert(0, os.path.join(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
    "lib"
))

class WinkBase:
   def animate(an, layer, delay=0):
      layer.transform.scale.value = Point(120, 120)

      easy = easing.EaseOut(1 / 4)
      layer.transform.position.add_keyframe(delay, Point(455, 275), easy)
      layer.transform.position.add_keyframe(50, Point(240, 275), easy)
      layer.transform.position.add_keyframe(60, Point(455, 275), easy)

      layer.transform.rotation.add_keyframe(0, 0, easy)
      layer.transform.rotation.add_keyframe(120, -30, easy)
      layer.transform.rotation.add_keyframe(180, 0, easy)

class Wink:
   def animate(an, layer):
      WinkBase.animate(an, layer)
      
      google = parse_svg_file(os.path.join(
          os.path.dirname(os.path.abspath(__file__)),
          "assets/images/google2.svg"
      )).layers[0]
      google.transform.scale.value = Point(1000, 1000)
      google.transform.position.value = Point(128, 128)
      an.add_layer(google)
      
class Wink2:
   def animate(an, layer):
      WinkBase.animate(an, layer, 15)
     
      text_layer = objects.ShapeLayer()
      an.add_layer(text_layer)
      style = FontStyle("animations/assets/fonts/Pacifico-Regular.ttf", 64, justify=TextJustify.Center)
      t = text_layer.add_shape(style.render("You're\nthe\nbest!")) 
      t.transform.position.value.y = 196 
      t.transform.position.value.x = 256
     
      stroke = text_layer.add_shape(objects.Stroke(Color(1, 1, 1), 12))
      stroke.opacity.add_keyframe(0, 0)
      stroke.opacity.add_keyframe(45, 0)
      stroke.opacity.add_keyframe(60, 100)

      marker = parse_svg_file(os.path.join(
          os.path.dirname(os.path.abspath(__file__)),
          "assets/images/marker.svg"
      )).layers[0]
      an.insert_layer(0, marker)
      marker.transform.scale.value = Point(80, 80)
      for fill in marker.find_all((objects.Fill)):
         fill.color.value = color.from_uint8(255, 83, 83) 

      transforms = []
      paths = []
      line = 0
      for shape in text_layer.shapes[0].shapes:
         if str(shape) != "Group": 
            continue

         transform = shape.shapes[-1] 

         count = 0
         for path in shape.find_all((objects.Path)):
            count += 1
            paths.append((path, transform.position.value))

         transforms.append((shape, transform, count))
         line += 1

      count = len(paths)
      start_time = 0
      for (group, transform, lenght) in transforms:
         duration = int(lenght/count*60)
         end_time = 60

         transform.opacity.add_keyframe(0, 0)
         transform.opacity.add_keyframe(start_time, 0)
         transform.opacity.add_keyframe(start_time + duration, 100)
         transform.opacity.add_keyframe(60, 100)

         fill = group.add_shape(objects.Fill(color.from_uint8(255, 83, 83))) 
         if start_time == 0:
            fill.opacity.add_keyframe(0, 0)
            fill.opacity.add_keyframe(start_time, 0)
            fill.opacity.add_keyframe(start_time + duration, 100)
            fill.opacity.add_keyframe(60, 100)

         start_time += duration
   
      index = 0
      for (path, position) in paths:
         start_time = int(index/count*60)
         end_time = int(index/count*60+60/count)

         follow_path(marker.transform.position, path.shape.value, start_time, end_time, 60, False, Point(position.x + 256, position.y + (512 - t.line_height)/2 - 46))
                  
         index += 1