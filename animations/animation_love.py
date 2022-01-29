import os
from lottie import Point, Color
from lottie.objects.text import TextJustify
from lottie.parsers.svg.importer import parse_svg_file 
from lottie.utils.animation import follow_path
from lottie.utils.font import FontStyle
from lottie import objects
from lottie.utils import color

class Love:
   def animate(an, layer, frames=60):
      layer.transform.position.value = Point(88, 128)
      layer.transform.scale.value = Point(120, 120)

      layer = objects.ShapeLayer()
      an.insert_layer(0, layer)
      
      heart = objects.Bezier()
      heart.add_point(Point(50, 20), Point(50, -20), Point(-50, -20))
      heart.add_smooth_point(Point(0, 50), Point(-5, -10))
      heart.add_smooth_point(Point(50, 100), Point(-10, 0))
      heart.add_smooth_point(Point(100, 50), Point(-5, 10))
      heart.closed = True
      antiheart = (
         objects.Bezier()
         .add_smooth_point(Point(50, 0), Point(10, 0))
         .add_smooth_point(Point(0, 50), Point(0, -20))
         .add_point(Point(50, 80), Point(-50, 20), Point(50, 20))
         .add_smooth_point(Point(100, 50), Point(0, 20))
         .close()
      )

      g2 = layer.add_shape(objects.Group())
      g2.transform.position.value = Point(72, 232)
      animated = g2.add_shape(objects.Path())
      animated.shape.add_keyframe(0, heart)
      animated.shape.add_keyframe(frames/2, antiheart)
      animated.shape.add_keyframe(frames-1, heart)
      g2.transform.scale.value = Point(75, 75)
      fill = g2.add_shape(objects.Fill(color.from_uint8(255, 83, 83)))
      g2.transform.anchor_point.value = Point(50, 50)
      g2.transform.rotation.value = -45

      g2 = layer.add_shape(objects.Group())
      g2.transform.position.value = Point(360, 74)
      animated = g2.add_shape(objects.Path())
      animated.shape.add_keyframe(0, antiheart)
      animated.shape.add_keyframe(frames/2, heart)
      animated.shape.add_keyframe(frames-1, antiheart)
      g2.transform.scale.value = Point(75, 75)
      fill = g2.add_shape(objects.Fill(color.from_uint8(255, 83, 83)))
      g2.transform.anchor_point.value = Point(50, 50)
      g2.transform.rotation.value = -150

      g2 = layer.add_shape(objects.Group())
      g2.transform.position.value = Point(420, 340)
      animated = g2.add_shape(objects.Path())
      animated.shape.add_keyframe(0, heart)
      animated.shape.add_keyframe(frames/2, antiheart)
      animated.shape.add_keyframe(frames-1, heart)
      g2.transform.scale.value = Point(75, 75)
      fill = g2.add_shape(objects.Fill(color.from_uint8(255, 83, 83)))
      g2.transform.anchor_point.value = Point(50, 50)
      g2.transform.rotation.value = 120

class Love2:
   def animate(an, frames=60):
      frame_rate = int(frames*11/12)

      layer = an.add_layer(objects.ShapeLayer())

      heart = objects.Bezier()
      heart.add_point(Point(50, 20), Point(50, -20), Point(-50, -20))
      heart.add_smooth_point(Point(0, 50), Point(-5, -10))
      heart.add_smooth_point(Point(50, 100), Point(-10, 0))
      heart.add_smooth_point(Point(100, 50), Point(-5, 10))
      heart.add_smooth_point(Point(50, 20), Point(50, -20))
      
      path = layer.add_shape(objects.Path())
      layer.transform.scale.value = Point(120, 120) 
      layer.transform.position.value = Point(256-60, 324)
      path.shape.value = heart
      fill = layer.add_shape(objects.Fill(color.from_uint8(255, 83, 83)))
      fill.opacity.add_keyframe(0, 0)
      fill.opacity.add_keyframe(frame_rate*0.75, 0)
      fill.opacity.add_keyframe(frame_rate*0.915, 100)
      stroke = layer.add_shape(objects.Stroke(Color(1, 1, 1), 20))
      stroke.opacity.add_keyframe(0, 0)
      stroke.opacity.add_keyframe(frame_rate*0.75, 0)
      stroke.opacity.add_keyframe(frame_rate*0.835, 100)

      marker = parse_svg_file(os.path.join(
          os.path.dirname(os.path.abspath(__file__)),
          "assets/images/marker.svg"
      )).layers[0]
      marker.in_point = 0
      marker.out_point = frames
      an.insert_layer(0, marker)

      marker.transform.scale.value = Point(80, 80)
      marker.transform.opacity.add_keyframe(0, 0)
      marker.transform.opacity.add_keyframe(frame_rate*0.65, 0) 
      marker.transform.opacity.add_keyframe(frame_rate*0.66, 100) 
      marker.transform.opacity.add_keyframe(frame_rate*0.915, 0) 
      for fill in marker.find_all((objects.Fill)):
         fill.color.value = color.from_uint8(255, 83, 83)

      follow_path(marker.transform.position, heart, frame_rate*0.66, frame_rate*0.915, frame_rate, False, Point(256-57, 334-38))

      text_frame_rate = frame_rate * 2/3
      text_layer = an.add_layer(objects.ShapeLayer())
      style = FontStyle("animations/assets/fonts/Pacifico-Regular.ttf", 78, justify=TextJustify.Center)
      t = text_layer.add_shape(style.render("I love\nyou!")) 
      t.transform.position.value.y = 158 
      t.transform.position.value.x = 256
      fill = text_layer.add_shape(objects.Fill(color.from_uint8(255, 83, 83))) 
      fill.opacity.add_keyframe(0, 0)
      fill.opacity.add_keyframe(frame_rate*0.5, 0)
      fill.opacity.add_keyframe(frame_rate*0.75, 100)
      stroke = text_layer.add_shape(objects.Stroke(Color(1, 1, 1), 20))
      stroke.opacity.add_keyframe(0, 0)
      stroke.opacity.add_keyframe(frame_rate*0.415, 0)
      stroke.opacity.add_keyframe(frame_rate*0.75, 100)

      marker = parse_svg_file(os.path.join(
          os.path.dirname(os.path.abspath(__file__)),
          "assets/images/marker.svg"
      )).layers[0]
      marker.in_point = 0
      marker.out_point = 180
      an.insert_layer(0, marker)
      marker.transform.scale.value = Point(80, 80)
      marker.transform.opacity.add_keyframe(0, 100)
      marker.transform.opacity.add_keyframe(frame_rate*0.65, 100)
      marker.transform.opacity.add_keyframe(frame_rate*0.66, 0)
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
         duration = int(lenght/count*text_frame_rate)
         end_time = frame_rate

         transform.opacity.add_keyframe(0, 0)
         transform.opacity.add_keyframe(start_time, 0)
         transform.opacity.add_keyframe(start_time + duration, 100)
         transform.opacity.add_keyframe(frame_rate, 100)

         fill = group.add_shape(objects.Fill(color.from_uint8(255, 83, 83)))

         if start_time == 0:
            fill.opacity.add_keyframe(0, 0)
            fill.opacity.add_keyframe(start_time, 0)
            fill.opacity.add_keyframe(start_time + duration, 100)
            fill.opacity.add_keyframe(frame_rate, 100)

         start_time += duration

   
      index = 0
      for (path, position) in paths:
         start_time = int(index/count*text_frame_rate)
         end_time = int(index/count*text_frame_rate+text_frame_rate/count)

         follow_path(marker.transform.position, path.shape.value, start_time, end_time, frame_rate, False, Point(position.x + 256, position.y + (512 - t.line_height)/2 - 46-34))
                  
         index += 1

class LoveNamed:
   def animate(an, name="me", frames=60):
      frame_rate = int(frames*11/12)

      layer = an.add_layer(objects.ShapeLayer())

      heart = objects.Bezier()
      heart.add_point(Point(50, 20), Point(50, -20), Point(-50, -20))
      heart.add_smooth_point(Point(0, 50), Point(-5, -10))
      heart.add_smooth_point(Point(50, 100), Point(-10, 0))
      heart.add_smooth_point(Point(100, 50), Point(-5, 10))
      heart.add_smooth_point(Point(50, 20), Point(50, -20))
      
      path = layer.add_shape(objects.Path())
      layer.transform.scale.value = Point(120, 120) 
      layer.transform.position.value = Point(332, 64) 
      path.shape.value = heart
      fill = layer.add_shape(objects.Fill(color.from_uint8(255, 83, 83)))
      fill.opacity.add_keyframe(0, 0)
      fill.opacity.add_keyframe(frame_rate*0.175, 0)
      fill.opacity.add_keyframe(frame_rate*0.375, 100)
      stroke = layer.add_shape(objects.Stroke(Color(1, 1, 1), 20))
      stroke.opacity.add_keyframe(0, 0)
      stroke.opacity.add_keyframe(frame_rate*0.415, 0)
      stroke.opacity.add_keyframe(frame_rate*0.75, 100)

      text_frame_rate = frame_rate * 2/3
      text_layer = an.add_layer(objects.ShapeLayer())
      style = FontStyle("animations/assets/fonts/Pacifico-Regular.ttf", 82, justify=TextJustify.Center)
      t = text_layer.add_shape(style.render("With       \nfrom\n" + name))
      t.transform.position.value.y = 164 
      t.transform.position.value.x = 256
      fill = text_layer.add_shape(objects.Fill(color.from_uint8(255, 83, 83)))
      fill.opacity.add_keyframe(0, 0)
      fill.opacity.add_keyframe(frame_rate*0.5, 0)
      fill.opacity.add_keyframe(frame_rate*0.75, 100)
      stroke = text_layer.add_shape(objects.Stroke(Color(1, 1, 1), 20))
      stroke.opacity.add_keyframe(0, 0)
      stroke.opacity.add_keyframe(frame_rate*0.415, 0)
      stroke.opacity.add_keyframe(frame_rate*0.75, 100)

      marker = parse_svg_file(os.path.join(
          os.path.dirname(os.path.abspath(__file__)),
          "assets/images/marker.svg"
      )).layers[0]
      marker.in_point = 0
      marker.out_point = frames
      an.insert_layer(0, marker)
      marker.transform.scale.value = Point(80, 80)
      marker.transform.opacity.add_keyframe(0, 100)
      marker.transform.opacity.add_keyframe(frame_rate*0.65, 100)
      marker.transform.opacity.add_keyframe(frame_rate*0.66, 0)
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
         duration = int(lenght/count*text_frame_rate)
         end_time = frame_rate

         transform.opacity.add_keyframe(0, 0)
         transform.opacity.add_keyframe(start_time, 0)
         transform.opacity.add_keyframe(start_time + duration, 100)
         transform.opacity.add_keyframe(frame_rate, 100)

         fill = group.add_shape(objects.Fill(color.from_uint8(255, 83, 83))) 

         if start_time == 0:
            fill.opacity.add_keyframe(0, 0)
            fill.opacity.add_keyframe(start_time, 0)
            fill.opacity.add_keyframe(start_time + duration, 100)
            fill.opacity.add_keyframe(frame_rate, 100)

         start_time += duration

   
      index = 0
      for (path, position) in paths:
         start_time = int(index/count*text_frame_rate)
         end_time = int(index/count*text_frame_rate+text_frame_rate/count)

         follow_path(marker.transform.position, path.shape.value, start_time, end_time, frame_rate, False, Point(position.x + 256, position.y + (512 - t.line_height)/2 - 46-34+6))
                  
         index += 1

class Love3:
   def animate(an, text="I love\nyou", frames=60):
      frame_rate = int(frames*11/12)

      layer = an.add_layer(objects.ShapeLayer())
      
      heart = objects.Bezier()
      heart.add_point(Point(220, 88), Point(220, -88), Point(-220, -88))
      heart.add_smooth_point(Point(0, 220), Point(-22, -44))
      heart.add_smooth_point(Point(220, 440), Point(-44, 0))
      heart.add_smooth_point(Point(440, 220), Point(-22, 44))
      heart.add_smooth_point(Point(220, 88), Point(220, -88))
      
      path = layer.add_shape(objects.Path())
      layer.transform.scale.value = Point(100, 100) 
      layer.transform.position.value = Point(36, 0)

      path.shape.value = heart
      fill = layer.add_shape(objects.Fill(color.from_uint8(255, 83, 83)))
      fill.opacity.add_keyframe(0, 0)
      fill.opacity.add_keyframe(frame_rate*0.75, 0)
      fill.opacity.add_keyframe(frame_rate*0.915, 100)

      marker = parse_svg_file(os.path.join(
          os.path.dirname(os.path.abspath(__file__)),
          "assets/images/marker.svg"
      )).layers[0]
      marker.in_point = 0
      marker.out_point = frames 
      an.insert_layer(0, marker)

      marker.transform.scale.value = Point(80, 80)
      marker.transform.opacity.add_keyframe(0, 0)
      marker.transform.opacity.add_keyframe(frame_rate*0.65, 0) 
      marker.transform.opacity.add_keyframe(frame_rate*0.66, 100) 
      marker.transform.opacity.add_keyframe(frame_rate*0.915, 100)
      marker.transform.opacity.add_keyframe(frame_rate, 0) 
      for fill in marker.find_all((objects.Fill)):
         fill.color.value = color.from_uint8(255, 83, 83)

      follow_path(marker.transform.position, heart, frame_rate*0.66, frame_rate*0.915, frame_rate, False, Point(36, -38)) 

      text_frame_rate = frame_rate * 2/3
      text_layer = an.insert_layer(0, objects.ShapeLayer())
      style = FontStyle("animations/assets/fonts/Pacifico-Regular.ttf", 74, justify=TextJustify.Center)
      t = text_layer.add_shape(style.render(text)) 
      t.transform.position.value.y = 212 
      t.transform.position.value.x = 256
      fill = text_layer.add_shape(objects.Fill(color.from_uint8(255, 83, 83)))
      fill.opacity.add_keyframe(0, 0)
      fill.opacity.add_keyframe(frame_rate*0.5, 0)
      fill.opacity.add_keyframe(frame_rate*0.75, 100)
      stroke = text_layer.add_shape(objects.Stroke(Color(1, 1, 1), 20))
      stroke.opacity.add_keyframe(0, 0)
      stroke.opacity.add_keyframe(frame_rate*0.5, 0)
      stroke.opacity.add_keyframe(frame_rate*0.75, 100)

      marker = parse_svg_file(os.path.join(
          os.path.dirname(os.path.abspath(__file__)),
          "assets/images/marker.svg"
      )).layers[0]
      marker.in_point = 0
      marker.out_point = frames
      an.insert_layer(0, marker)
      marker.transform.scale.value = Point(80, 80)
      marker.transform.opacity.add_keyframe(0, 100)
      marker.transform.opacity.add_keyframe(frame_rate*0.65, 100)
      marker.transform.opacity.add_keyframe(frame_rate*0.66, 0)
      for fill in marker.find_all((objects.Fill)):
         fill.color.value = color.from_uint8(255, 83, 83)

      transforms = []
      paths = []
      line = 0
      for shape in text_layer.shapes[0].shapes:
         if str(shape) != "Group": 
            continue

         transform = shape.shapes[-1] # TransformShape

         count = 0
         for path in shape.find_all((objects.Path)):
            count += 1
            paths.append((path, transform.position.value))

         transforms.append((shape, transform, count))
         line += 1


      count = len(paths)
      start_time = 0
      for (group, transform, lenght) in transforms:
         duration = int(lenght/count*text_frame_rate)

         transform.opacity.add_keyframe(0, 0)
         transform.opacity.add_keyframe(start_time, 0)
         transform.opacity.add_keyframe(start_time + duration, 100)
         transform.opacity.add_keyframe(frame_rate, 100)

         fill = group.add_shape(objects.Fill(color.from_uint8(255, 83, 83))) # Color(147/255, 120/255, 1)
         
         if start_time == 0:
            fill.opacity.add_keyframe(0, 0)
            fill.opacity.add_keyframe(start_time, 0)
            fill.opacity.add_keyframe(start_time + duration, 100)
            fill.opacity.add_keyframe(frame_rate, 100)

         start_time += duration

   
      index = 0
      for (path, position) in paths:
         start_time = int(index/count*text_frame_rate)
         end_time = int(index/count*text_frame_rate+text_frame_rate/count)

         follow_path(marker.transform.position, path.shape.value, start_time, end_time, frame_rate, False, Point(position.x + 256, position.y + (512 - t.line_height)/2 - 46-34+66-12))
                  
         index += 1