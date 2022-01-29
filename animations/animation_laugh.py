from lottie import Point
from lottie.utils.animation import spring_pull

class Laugh:
   def animate(an, layer, layer2, layer3):
      layer.transform.position.value = Point(116, 28)

      layer2.transform.position.value = Point(-240, 100)
      layer2.transform.scale.value = Point(60, 60)
      an.add_layer(layer2)

      layer3.transform.position.value = Point(600, 100)
      layer3.transform.scale.value = Point(60, 60)
      an.add_layer(layer3)

      falloff = 15
      spring_pull(layer.transform.position, Point(116, 128), 0, 60, falloff, 7)
      spring_pull(layer2.transform.position, Point(40, 100), 0, 60, falloff, 7)
      spring_pull(layer3.transform.position, Point(300, 100), 0, 60, falloff, 7)




     
