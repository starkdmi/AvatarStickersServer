from lottie import Point
from lottie.objects import easing

class AnimateAvatar:
   def sad(layer):
      try: 
         face = layer.find("transparent_Face")
         eyes = face.find("transparent_Eyes").shapes[0]
         drop = eyes.find("cry_Drop")

         drop2 = drop.clone()

         drop.transform.position.add_keyframe(0, Point(0, 0))
         drop.transform.position.add_keyframe(30, Point(0, 20))
         drop.transform.opacity.add_keyframe(0, 100)
         drop.transform.opacity.add_keyframe(20, 100)
         drop.transform.opacity.add_keyframe(25, 80)
         drop.transform.opacity.add_keyframe(30, 0)

         drop2 = eyes.add_shape(drop2)
         drop2.transform.position.add_keyframe(30, Point(62, 0))
         drop2.transform.position.add_keyframe(60, Point(62, 20))
         drop2.transform.opacity.add_keyframe(30, 0)
         drop2.transform.opacity.add_keyframe(40, 100)
         drop2.transform.opacity.add_keyframe(50, 80)
         drop2.transform.opacity.add_keyframe(60, 0)
      except:
         pass

   def love(layer):
      try:
         face = layer.find("transparent_Face")
         mouth = face.find("transparent_Mouth").shapes[0]
         AnimateAvatar.__tongue(mouth)
      except:
         pass

   def crying(layer):
      try:
         face = layer.find("transparent_Face")
         eyes = face.find("transparent_Eyes").shapes[0]
         AnimateAvatar.__remove_eye_drop(eyes)
      except:
         pass

   def __tongue(mouth):
      tongue = mouth.find("tongue_Tongue")
      easy = easing.EaseOut(1/4)
      tongue.transform.skew.add_keyframe(0, 0, easy)
      tongue.transform.skew.add_keyframe(20, 10, easy)
      tongue.transform.skew.add_keyframe(40, -10, easy)
      tongue.transform.skew.add_keyframe(60, 0, easy)

   def __remove_eye_drop(eyes):
      drop = eyes.find("cry_Drop")
      drop.hidden = True
      drop.transform.opacity.value = 0
