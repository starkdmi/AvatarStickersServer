from lottie import Point, Color
from lottie import objects
from lottie.objects import easing
from lottie.utils.font import FontStyle

class Sad:
   def animate(an, layer):
      layer.transform.position.value = Point(88, 128)
      layer.transform.scale.value = Point(120, 120)

      easy = easing.EaseOut(1 / 4)
      layer.transform.position.add_keyframe(0, Point(88, 128), easy)
      layer.transform.position.add_keyframe(20, Point(22, 128), easy)
      layer.transform.position.add_keyframe(40, Point(154, 128), easy)
      layer.transform.position.add_keyframe(60, Point(88, 128), easy)

      text_layer = objects.ShapeLayer()
      an.add_layer(text_layer)
      style = FontStyle("Ubuntu", 86, emoji_svg="animations/assets/twemoji/assets/svg/")
      t = text_layer.add_shape(style.render("\U0001F614")) 
      t.transform.position.value.y += t.line_height + 60
      t.transform.position.value.x += 40
      text_layer.add_shape(objects.Fill(Color(0, 0, 0)))

      x = t.transform.position.value.x
      y = t.transform.position.value.y
      text_layer.transform.position.add_keyframe(0, Point(x, y), easy)
      text_layer.transform.position.add_keyframe(20, Point(x+20, y), easy)
      text_layer.transform.position.add_keyframe(40, Point(x-20, y), easy)
      text_layer.transform.position.add_keyframe(60, Point(x, y), easy)

