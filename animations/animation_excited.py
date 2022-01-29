from lottie import Point, Color
from lottie import objects
from lottie.objects import easing

class Excited:
   def animate(an, layer):
      layer.transform.position.value = Point(88, 128)
      layer.transform.scale.value = Point(120, 120)

      easy = easing.EaseOut(1 / 4)
      easy2 = easing.EaseOut(1 / 8)
      yellow = Color(255/255, 237/255, 41/255)

      star_layer = objects.ShapeLayer()
      an.insert_layer(0, star_layer)
      
      group = star_layer.add_shape(objects.Group())

      star = group.add_shape(objects.Star())
      star.inner_radius.value = 10
      star.outer_radius.value = 30
      star.position.value = Point(160, 80)

      fill = group.add_shape(objects.Fill(yellow)) 

      group.transform.anchor_point.value = Point(160, 80)
      group.transform.position.value = Point(160, 80)
      group.transform.rotation.add_keyframe(0, 0, easy)
      group.transform.rotation.add_keyframe(20, 180, easy)
      group.transform.rotation.add_keyframe(60, 360, easy)


      star_layer = objects.ShapeLayer()
      an.insert_layer(0, star_layer)
      
      group = star_layer.add_shape(objects.Group())

      star = group.add_shape(objects.Star())
      star.inner_radius.value = 10
      star.outer_radius.value = 30
      star.position.value = Point(80, 240)
      
      fill = group.add_shape(objects.Fill(yellow)) 

      group.transform.anchor_point.value = Point(80, 240)
      group.transform.position.value = Point(80, 240)
      group.transform.rotation.add_keyframe(0, 0, easy2)
      group.transform.rotation.add_keyframe(30, 180, easy2)
      group.transform.rotation.add_keyframe(60, 360, easy2)


      star_layer = objects.ShapeLayer()
      an.insert_layer(0, star_layer)
      
      group = star_layer.add_shape(objects.Group())

      star = group.add_shape(objects.Star())
      star.inner_radius.value = 10
      star.outer_radius.value = 30
      star.position.value = Point(400, 120)
      
      fill = group.add_shape(objects.Fill(yellow)) 

      group.transform.anchor_point.value = Point(400, 120)
      group.transform.position.value = Point(400, 120)
      group.transform.rotation.add_keyframe(0, 0, easy)
      group.transform.rotation.add_keyframe(20, 180, easy)
      group.transform.rotation.add_keyframe(60, 360, easy)


      star_layer = objects.ShapeLayer()
      an.insert_layer(0, star_layer)
      
      group = star_layer.add_shape(objects.Group())

      star = group.add_shape(objects.Star())
      star.inner_radius.value = 10
      star.outer_radius.value = 30
      star.position.value = Point(430, 300)
      
      fill = group.add_shape(objects.Fill(yellow)) 

      group.transform.anchor_point.value = Point(430, 300)
      group.transform.position.value = Point(430, 300)
      group.transform.rotation.add_keyframe(0, 0, easy2)
      group.transform.rotation.add_keyframe(30, 180, easy2)
      group.transform.rotation.add_keyframe(60, 360, easy2)


      
