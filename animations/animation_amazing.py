from lottie import Point
from lottie.utils.animation import follow_path
from lottie.objects import easing
from lottie.parsers.svg import parse_svg_file
import os
     
class Amazing:
   def animate(an, layer):
      layer.transform.position.value = Point(88, 128)
      layer.transform.scale.value = Point(120, 120)
      easy = easing.EaseOut(1 / 4)

      telegram = parse_svg_file(os.path.join(
            os.path.dirname(os.path.abspath(__file__)),
            "assets/images/fly_left.svg" 
      )).layers[0]
      telegram.transform.scale.value = Point(8, 8)

      telegram2 = parse_svg_file(os.path.join(
            os.path.dirname(os.path.abspath(__file__)),
            "assets/images/fly_right.svg" 
      )).layers[0]
      telegram2.transform.scale.value = Point(8, 8)

      curves = parse_svg_file(os.path.join(
            os.path.dirname(os.path.abspath(__file__)),
            "assets/images/curves.svg"
      )).layers[0]
      an.insert_layer(0, curves)

      path1 = curves.find("FlyPath1").shapes[0].shapes[0]
      path2 = curves.find("FlyPath2").shapes[0].shapes[0]
      path3 = curves.find("FlyPath3").shapes[0].shapes[0]
      path4 = curves.find("FlyPath4").shapes[0].shapes[0]
      path5 = curves.find("FlyPath5").shapes[0].shapes[0]
      path6 = curves.find("FlyPath6").shapes[0].shapes[0]
      path7 = curves.find("FlyPath7").shapes[0].shapes[0]

      # 1 (RTL)
      telegramX = telegram2.clone()
      an.insert_layer(0, telegramX)
      telegramX.transform.rotation.add_keyframe(0, -30, easy)
      telegramX.transform.rotation.add_keyframe(24, -25, easy)
      telegramX.transform.rotation.add_keyframe(30, -35, easy)
      telegramX.transform.rotation.add_keyframe(40, -40, easy)
      telegramX.transform.opacity.add_keyframe(0, 100)
      telegramX.transform.opacity.add_keyframe(35, 100)
      telegramX.transform.opacity.add_keyframe(40, 0)
      follow_path(telegramX.transform.position, path1.shape.value, 0, 40, 60, False, Point(-64, -64))
      
      # 2
      telegramX = telegram.clone()
      an.insert_layer(0, telegramX)
      telegramX.transform.rotation.add_keyframe(0, 80, easy)
      telegramX.transform.rotation.add_keyframe(25, 60, easy)
      telegramX.transform.rotation.add_keyframe(45, -15, easy)
      telegramX.transform.rotation.add_keyframe(60, -20, easy)
      follow_path(telegramX.transform.position, path2.shape.value, 0, 60, 60, False, Point(64, -64))
      
      # 3
      telegramX = telegram.clone()
      an.insert_layer(0, telegramX)
      telegramX.transform.rotation.add_keyframe(0, 80, easy)
      telegramX.transform.rotation.add_keyframe(15, 60, easy)
      telegramX.transform.rotation.add_keyframe(35, 15, easy)
      telegramX.transform.rotation.add_keyframe(60, 25, easy)
      follow_path(telegramX.transform.position, path3.shape.value, 0, 60, 60, False, Point(64, -64))

      # 4
      telegramX = telegram.clone()
      an.insert_layer(0, telegramX)
      telegramX.transform.rotation.add_keyframe(10, 20, easy)
      telegramX.transform.rotation.add_keyframe(30, -10, easy)
      telegramX.transform.rotation.add_keyframe(35, 10, easy)
      telegramX.transform.rotation.add_keyframe(44, 55, easy)
      telegramX.transform.rotation.add_keyframe(50, 65, easy)

      telegramX.transform.opacity.add_keyframe(0, 0)
      telegramX.transform.opacity.add_keyframe(9, 0)
      telegramX.transform.opacity.add_keyframe(10, 100)
      telegramX.transform.opacity.add_keyframe(50, 100)
      telegramX.transform.opacity.add_keyframe(55, 0)

      follow_path(telegramX.transform.position, path4.shape.value, 10, 50, 60, False, Point(64, -324))

      # 5 (RTL)
      telegramX = telegram2.clone()
      an.insert_layer(0, telegramX)
      telegramX.transform.rotation.add_keyframe(0, -30, easy)
      telegramX.transform.rotation.add_keyframe(20, -10, easy)
      telegramX.transform.rotation.add_keyframe(35, 0, easy)
      telegramX.transform.rotation.add_keyframe(40, -20, easy)
      telegramX.transform.rotation.add_keyframe(60, -60, easy)
      follow_path(telegramX.transform.position, path5.shape.value, 0, 60, 60, False, Point(-64, -48))

      # 6 (RTL)
      telegramX = telegram2.clone()
      an.insert_layer(0, telegramX)

      telegramX.transform.rotation.add_keyframe(0, -35, easy) 
      telegramX.transform.rotation.add_keyframe(15, -20, easy) 
      telegramX.transform.rotation.add_keyframe(17, -15, easy) 
      telegramX.transform.rotation.add_keyframe(32, -30, easy) 
      telegramX.transform.rotation.add_keyframe(34, -35, easy) 
      telegramX.transform.rotation.add_keyframe(40, -40, easy) 

      telegramX.transform.opacity.add_keyframe(0, 100)
      telegramX.transform.opacity.add_keyframe(40, 100)
      telegramX.transform.opacity.add_keyframe(45, 0)

      follow_path(telegramX.transform.position, path6.shape.value, 0, 45, 60, False, Point(-64, -32))