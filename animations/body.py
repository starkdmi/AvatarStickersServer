import os
from lottie import Point, Color
from lottie.objects import easing
from lottie.objects.text import TextJustify
from lottie.parsers.svg.importer import parse_svg_file 
from lottie import objects
from lottie.utils import color
from lottie.utils.font import FontStyle
from animations.helpers.body_color import parse_color, scale_lightness

class Body:
   def apply(an, layer, avatarStyle, style, id, offset = Point(16, 16)):
      if id not in [ 
         "artist-2218153-0", "basketball-player-2218183-0", "character-2218144-0", "character-2218171-0", 
         "character-2218185-0", "character-2218190-0", "character-2218204-0", "character-2218229-0", "lady-2218164-0", 
         "lady-teacher-2218147-0", "man-with-glass-2218163-0", "michael-jackson-2218161-0", "photographer-2218230-0", "professor-2218155-0",
         "student-2218150-0", "winner-2218184-0", "football-player-2218213-0"]: 
         return

      skinColor = style["skinColor"]
      clothesColor = style["clothesColor"]

      body = parse_svg_file(os.path.join(
         os.path.dirname(os.path.abspath(__file__)),
         "assets/gee-me/" + id + ".svg"
      )).layers[0]

      body.transform.scale.value = Point(35, 35) 
      body.transform.position.value = Point(-80 + offset.x, -80 + offset.y)
      an.add_layer(body)

      head_offset = Point(0, 0)
      if id == "artist-2218153-0":
         head_offset = Point(3, -14) # HEAD_ROUND
         # head_offset = Point(3, -11) # HEAD
      elif id == "basketball-player-2218183-0":
         head_offset = Point(-16, -13)
      elif id == "character-2218144-0":
         head_offset = Point(1.5, -13)
      elif id == "character-2218171-0":
         head_offset = Point(-2, -8)
      # elif id == "character-2218178-0":
      #    head_offset = Point(4.25, -11.75)
      elif id == "character-2218185-0":
         head_offset = Point(26, -1.5)
      elif id == "character-2218204-0":
         head_offset = Point(-15, 0.5)
      elif id == "character-2218229-0":
         head_offset = Point(4, 0)
      elif id == "lady-2218164-0":
         head_offset = Point(2, -10)
      elif id == "lady-teacher-2218147-0":
         head_offset = Point(4, -13)
      elif id == "man-with-glass-2218163-0":
         head_offset = Point(6, -20)
      elif id == "michael-jackson-2218161-0":
         head_offset = Point(4, -18)
      elif id == "photographer-2218230-0":
         head_offset = Point(0, -13)
      elif id == "professor-2218155-0":
         head_offset = Point(3, -4)
      elif id == "student-2218150-0":
         head_offset = Point(4, -30)
      elif id == "winner-2218184-0":
         head_offset = Point(28, -16)
      elif id == "football-player-2218213-0":
         head_offset = Point(9, -4)

      layer.transform.position.value = Point(34 + offset.x + head_offset.x, 4 + offset.y + head_offset.y)
      layer.transform.scale.value = Point(70, 70)

      head = body.shapes[0].shapes[0].shapes[0]
      # body = body.shapes[0].shapes[0].shapes[1]
      # legs = body.shapes[0].shapes[0].shapes[2]
      head.hidden = True 
      head.transform.opacity.value = 0

      for fill in body.find_all((objects.Fill)):
         if fill.color.value in [
            color.from_uint8(235, 186, 170), 
            color.from_uint8(246, 221, 214), 
            color.from_uint8(238, 209, 201), 
            color.from_uint8(248, 204, 190),
            color.from_uint8(245, 208, 195),
            color.from_uint8(244, 213, 204), 
            color.from_uint8(251, 210, 197), 
         ]:
            skin = parse_color(skinColor)
            fill.color.value = skin
         # if id == "artist-2218153-0" and fill.color.value == color.from_uint8(205, 199, 187): 
         #    fill.opacity.value = 0
         if id == "character-2218178-0" and fill.color.value == color.from_uint8(23, 16, 15): 
            fill.opacity.value = 0
         elif id == "character-2218229-0" and fill.color.value == color.from_uint8(241, 237, 237): 
            fill.opacity.value = 0
         elif id == "lady-2218164-0" and fill.color.value == color.from_uint8(23, 16, 15): 
            fill.opacity.value = 0
         elif id == "lady-teacher-2218147-0" and fill.color.value == color.from_uint8(61, 44, 24): 
            fill.opacity.value = 0
         elif id == "man-with-glass-2218163-0" and fill.color.value == color.from_uint8(165, 143, 117): 
            fill.opacity.value = 0
         elif id == "michael-jackson-2218161-0" and fill.color.value == color.from_uint8(217, 216, 221): 
            fill.opacity.value = 0
         elif id == "student-2218150-0" and fill.color.value == color.from_uint8(228, 228, 224): 
            fill.opacity.value = 0
         elif id == "winner-2218184-0" and fill.color.value == color.from_uint8(85, 93, 101): 
            fill.opacity.value = 0
         elif id == "character-2218204-0" and fill.color.value == color.from_uint8(220, 177, 163): 
            fill.opacity.value = 0
         # elif id == "girl-with-pink-outfit-2218165-0" and fill.color.value == color.from_uint8(45, 36, 39): 
         #    fill.opacity.value = 0

         elif id == "football-player-2218213-0":
            clothes = parse_color(clothesColor)
            if fill.color.value == color.from_uint8(233, 107, 67): 
               fill.color.value = clothes
            elif fill.color.value in [color.from_uint8(219, 91, 50), color.from_uint8(232, 107, 67), color.from_uint8(57, 88, 117)]:
               darker = scale_lightness(clothes.to_rgb()[:3], 0.94)
               fill.color.value = Color(darker[0], darker[1], darker[2])
            elif fill.color.value == color.from_uint8(9, 25, 40):
               fill.color.value = color.from_uint8(18, 43, 66)

         elif id == "basketball-player-2218183-0":
            clothes = parse_color(clothesColor)
            if fill.color.value == color.from_uint8(2, 84, 210): 
               fill.color.value = clothes
            elif fill.color.value in [color.from_uint8(7, 64, 153), color.from_uint8(10, 80, 191)]:
               darker = scale_lightness(clothes.to_rgb()[:3], 1.2)
               fill.color.value = Color(darker[0], darker[1], darker[2])
            elif fill.color.value == color.from_uint8(9, 41, 120):
               darker = scale_lightness(clothes.to_rgb()[:3], 1.1)
               fill.color.value = Color(darker[0], darker[1], darker[2])
            elif fill.color.value == color.from_uint8(0, 0, 0):
               fill.color.value = color.from_uint8(74, 81, 109)

         elif id == "character-2218185-0":
            clothes = parse_color(clothesColor)
            if fill.color.value == color.from_uint8(85, 93, 101): 
               fill.opacity.value = 0
            elif fill.color.value == color.from_uint8(226, 61, 50): 
               fill.color.value = clothes
            elif fill.color.value == color.from_uint8(204, 34, 23): 
               darker = scale_lightness(clothes.to_rgb()[:3], 0.9)
               fill.color.value = Color(darker[0], darker[1], darker[2])
            elif fill.color.value == color.from_uint8(209, 50, 39): 
               darker = scale_lightness(clothes.to_rgb()[:3], 0.94)
               fill.color.value = Color(darker[0], darker[1], darker[2])
            elif fill.color.value == color.from_uint8(240, 96, 87): 
               darker = scale_lightness(clothes.to_rgb()[:3], 1.15)
               fill.color.value = Color(darker[0], darker[1], darker[2])

            elif fill.color.value == color.from_uint8(226, 63, 52): 
               darker = scale_lightness(clothes.to_rgb()[:3], 0.95)
               fill.color.value = Color(darker[0], darker[1], darker[2])

            elif fill.color.value == color.from_uint8(182, 44, 35): 
               darker = scale_lightness(clothes.to_rgb()[:3], 0.91)
               fill.color.value = Color(darker[0], darker[1], darker[2])
            
      clothes = layer.find(str(avatarStyle) + "_Clothing").shapes[0]
      clothes.hidden = True
      clothes.transform.opacity.value = 0

      return body
      
   def basket_ball(an, layer, avatarStyle, style):
      Body.apply(an, layer, avatarStyle, style, "basketball-player-2218183-0", offset=Point(142, 38))

      ball_left = parse_svg_file(os.path.join(
            os.path.dirname(os.path.abspath(__file__)),
            "assets/images/ball_left2.svg" # ball_left
      )).layers[0]
      ball_left.transform.scale.value = Point(30, 30)

      ball_right = parse_svg_file(os.path.join(
            os.path.dirname(os.path.abspath(__file__)),
            "assets/images/ball_right2.svg" # ball_right
      )).layers[0]
      ball_right.transform.scale.value = Point(30, 30)

      offset = 140 # x moving offset
      index = 0
      for i in range(24, 500, 136):
         for j in range(-16-offset, 500+offset, offset):
            clone = None
            if index % 2 == 0:
               clone = ball_left.clone()
            else:
               clone = ball_right.clone()

            clone.transform.position.add_keyframe(0, Point(j, i))
            if index % 2 == 0:
               clone.transform.position.add_keyframe(60, Point(j+offset, i))
            else:
               clone.transform.position.add_keyframe(60, Point(j-offset, i))

            an.add_layer(clone)
         index += 1

   def football(an, layer, avatarStyle, style):
      Body.apply(an, layer, avatarStyle, style, "football-player-2218213-0", offset=Point(130, 38))

      ball = parse_svg_file(os.path.join(
            os.path.dirname(os.path.abspath(__file__)),
            "assets/images/football.svg" 
      )).layers[0]
      ball.transform.scale.value = Point(30, 30)

      offset = 140 # x moving offset
      index = 0
      for i in range(24, 500, 136):
         for j in range(-16-offset, 500+offset, offset):
            clone = ball.clone()

            clone.transform.position.add_keyframe(0, Point(j, i))
            if index % 2 == 0:
               clone.transform.position.add_keyframe(60, Point(j+offset, i))
            else:
               clone.transform.position.add_keyframe(60, Point(j-offset, i))

            an.add_layer(clone)
         index += 1

   def cool_men(an, layer, avatarStyle, style):
      Body.apply(an, layer, avatarStyle, style, "character-2218185-0", offset=Point(32, 38))

      clothesColor = parse_color(style["clothesColor"]) 

      easy = easing.EaseOut(1 / 4)

      text_layer = objects.ShapeLayer()
      an.add_layer(text_layer)
      style = FontStyle("animations/assets/fonts/FasterOne-Regular.ttf", 72, justify=TextJustify.Center)
      t = text_layer.add_shape(style.render("3")) 
      t.transform.position.value.y = 104 + t.line_height/2
      t.transform.position.value.x = 380
      fill = text_layer.add_shape(objects.Fill(clothesColor)) 
      fill.opacity.add_keyframe(0, 100, easy)
      fill.opacity.add_keyframe(8, 100, easy)
      fill.opacity.add_keyframe(12, 0, easy)
      stroke = text_layer.add_shape(objects.Stroke(Color(1, 1, 1), 5))
      stroke.opacity.add_keyframe(0, 100, easy)
      stroke.opacity.add_keyframe(8, 100, easy)
      stroke.opacity.add_keyframe(12, 0, easy)

      text_layer = objects.ShapeLayer()
      an.add_layer(text_layer)
      style = FontStyle("animations/assets/fonts/FasterOne-Regular.ttf", 72, justify=TextJustify.Center)
      t = text_layer.add_shape(style.render("2")) 
      t.transform.position.value.y = 104 + t.line_height/2
      t.transform.position.value.x = 380
      
      fill = text_layer.add_shape(objects.Fill(clothesColor))
      fill.opacity.add_keyframe(0, 0, easy)
      fill.opacity.add_keyframe(8, 0, easy)
      fill.opacity.add_keyframe(12, 100, easy)
      fill.opacity.add_keyframe(18, 100, easy)
      fill.opacity.add_keyframe(22, 0, easy)
      stroke = text_layer.add_shape(objects.Stroke(Color(1, 1, 1), 5))
      
      stroke.opacity.add_keyframe(0, 0, easy)
      stroke.opacity.add_keyframe(8, 0, easy)
      stroke.opacity.add_keyframe(12, 100, easy)
      stroke.opacity.add_keyframe(18, 100, easy)
      stroke.opacity.add_keyframe(22, 0, easy)

      text_layer = objects.ShapeLayer()
      an.add_layer(text_layer)
      style = FontStyle("animations/assets/fonts/FasterOne-Regular.ttf", 72, justify=TextJustify.Center)
      t = text_layer.add_shape(style.render("1")) 
      t.transform.position.value.y = 104 + t.line_height/2
      t.transform.position.value.x = 380
      
      fill = text_layer.add_shape(objects.Fill(clothesColor)) 
      
      fill.opacity.add_keyframe(0, 0, easy)
      fill.opacity.add_keyframe(18, 0, easy)
      fill.opacity.add_keyframe(22, 100, easy)
      fill.opacity.add_keyframe(28, 100, easy)
      fill.opacity.add_keyframe(32, 0, easy)
      stroke = text_layer.add_shape(objects.Stroke(Color(1, 1, 1), 5))
      
      stroke.opacity.add_keyframe(0, 0, easy)
      stroke.opacity.add_keyframe(18, 0, easy)
      stroke.opacity.add_keyframe(22, 100, easy)
      stroke.opacity.add_keyframe(28, 100, easy)
      stroke.opacity.add_keyframe(32, 0, easy)

      text_layer = objects.ShapeLayer()
      an.add_layer(text_layer)
      style = FontStyle("animations/assets/fonts/FasterOne-Regular.ttf", 66, justify=TextJustify.Center)
      t = text_layer.add_shape(style.render("JUST\nDO IT!")) 
      t.transform.position.value.y = 104
      t.transform.position.value.x = 380
      
      fill = text_layer.add_shape(objects.Fill(clothesColor)) 
      
      fill.opacity.add_keyframe(0, 0, easy)
      fill.opacity.add_keyframe(28, 0, easy)
      fill.opacity.add_keyframe(38, 100, easy)
      stroke = text_layer.add_shape(objects.Stroke(Color(1, 1, 1), 5))
      
      stroke.opacity.add_keyframe(0, 0, easy)
      stroke.opacity.add_keyframe(28, 0, easy)
      stroke.opacity.add_keyframe(38, 100, easy)