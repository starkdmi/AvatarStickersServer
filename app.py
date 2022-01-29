from fastapi import FastAPI, Header
from fastapi.responses import FileResponse, JSONResponse, PlainTextResponse, RedirectResponse, StreamingResponse
from pydantic import BaseModel
from typing import Optional
import random

import xml.etree.ElementTree as ET
from lottie import objects
from lottie.parsers.svg import parse_svg_etree
from lottie import Point
from lottie.objects import easing
import python_avatars as pa

# WhatsApp
import tempfile
from lottie.exporters import exporters
from lottie.utils.stripper import Strip
exporter = exporters.get_from_filename("temp.webp")
strip = Strip(3)
o_options = { 'lossless': False, 'quality': 30, 'method': 0, 'skip_frames': 3 }

from animations.animation_angry import Angry
from animations.animation_love import Love, Love2, Love3, LoveNamed
from animations.animation_amazing import Amazing
from animations.animation_crying import Crying
from animations.animation_excited import Excited
from animations.animation_sad import Sad
from animations.animation_laugh import Laugh
from animations.animation_wink import Wink, Wink2
from animations.animation_please import Please
from animations.animation_emotionless import Emotionless
from animations.animation_avatar import AnimateAvatar
from animations.animation_cookie import Cookie
from animations.body import Body

class Avatar(BaseModel):
   service: str = "telegram" # telegram, whatsapp
   emotion: str
   hair: Optional[str] = "no_hair"
   eyebrows: Optional[str] = "default"
   eyes: Optional[str] = "default"
   mouth: Optional[str] = "default"
   beard: Optional[str] = ""
   gender: Optional[str] = "male"
   accessory: Optional[str] = ""
   clothes: Optional[str] = "graphic_shirt"
   shirt_graphic: Optional[str] = "custom_text"
   shirt_text: Optional[str] = ""
   facialHair: Optional[str] = None
   hairStyle: Optional[str] = None
   clothesColor: Optional[str] = None
   beardColor: Optional[str] = None
   text_color: Optional[str] = None
   hairColorOriginal: Optional[str] = None
   hairColor: Optional[str] = None
   skinColorOriginal: Optional[str] = None
   hatColor: Optional[str] = None
   skinColor: Optional[str] = None
   clothesColorOriginal: Optional[str] = None

app = FastAPI()

"""
   python3.8 -m uvicorn app:app --host=macpro.home --port=5000 --reload

   curl -X POST \
   -H 'Accept: application/json' \
   -H 'Content-type: application/json' \
   -H 'Token: SERVER_TOKEN' \
   -d '{"hatColor": "#25557C", "hairColorOriginal": "#897A68", "Black_Hair": "0.5147464", "gender": "female", "text_color": "#EDF1F2", "hairStyle": "Straight_Hair", "shirt_graphic": "resist", "beardColor": "#B58143", "beard2": "0.116824806", "mouth": "smile", "facialHair": "", "mustache": "0.20124775", "hairColor": "#B58143", "skinColorOriginal": "#A97663", "skinColor": "#D08B5B", "accessory": "", "eyes": "happy", "clothesColorOriginal": "#7B5641", "clothesColor": "#25557C", "Straight_Hair": "0.39472002", "hair": "long_not_too_long", "shirt_text": "", "clothes": "hoodie", "beard": "", "emotion": "Football", "eyebrows": "default"}' 'http://macpro.home:5000/avatar'
"""

@app.post("/avatar")
def avatar(avatar: Avatar, token: Optional[str] = Header(None)):
   if (token == Header(None) or token != "SERVER_TOKEN"): 
      return JSONResponse(status_code=404, content={"message": "auth required"})

   print(avatar)

   if avatar.emotion == "Angry":
      avatar.eyes = "squint" # or default
   if (avatar.mouth == "scream_open") and ((avatar.emotion == "Love") or (avatar.emotion == "Amazing") or (avatar.emotion == "Excited")):
      avatar.mouth = random.choice(["smile", "tongue"])
   
   if avatar.hair in ['hat', 'hijab', 'turban', 'winter_hat_1', 'winter_hat_2', 'winter_hat_3', 'winter_hat_4']:
      avatar.hair = pa.HatType.fromString(avatar.hair)
   elif avatar.hair in [
      'no_hair', 'big_hair', 'bob', 'bun', 'caesar_side_part', 'caesar', 'curly', 'curvy',
      'dreads', 'frida', 'frizzle', 'fro_band', 'fro', 'long_not_too_long', 'mia_wallace', 'shaggy_mullet',
      'shaggy', 'shaved_sides', 'short_curly', 'short_dreads_1', 'short_dreads_2', 'short_flat',
      'short_round', 'short_waved', 'sides', 'straight_1', 'straight_2', 'straight_strand'
   ]: 
      avatar.hair = pa.HairType.fromString(avatar.hair)
   
   systemColors = ["#614335", "#A55728", "#FF488E", "#F59797", "#E8E1E1", None]
   if avatar.text_color in systemColors: 
      avatar.text_color = "#FFFFFF"
   if avatar.hatColor in systemColors: 
      avatar.hatColor = "#3C4F5C"
   if avatar.skinColor in systemColors: 
      avatar.skinColor = "#EDB98A"
   if avatar.clothesColor in systemColors: 
      avatar.clothesColor = "#3C4F5C"
   if avatar.hairColor in systemColors: 
      avatar.hairColor = "#FF488E"
   if avatar.beardColor in systemColors: 
      avatar.beardColor = "#FF488E"

   if avatar.eyebrows not in ['', 'angry_natural', 'default_natural', 'default', 'flat_natural', 
   'frown_natural', 'up_down', 'up_down_natural', 'raised_excited_natural', 'raised_excited', 
   'sad_concerned_natural', 'sad_concerned', 'unibrow_natural', 'angry']:
      avatar.eyebrows = "default"
   
   if avatar.eyes not in ['closed', 'cry', 'default', 'eye_roll', 'happy', 'heart', 'side',
   'surprised', 'wink_wacky', 'wink', 'x_dizzy', 'squint']:
      avatar.eyes = "default"
   
   if avatar.mouth not in ['concerned', 'default', 'disbelief', 'eating', 'grimace', 'sad', 'scream_open',
   'serious', 'smile', 'tongue', 'twinkle', 'vomit']:
      avatar.mouth = "default"

   if avatar.beard not in ['', 'beard_light', 'beard_magestic', 'beard_medium', 'moustache_fancy', 'moustache_magnum']:
      avatar.beard = ""

   if avatar.accessory not in ['', 'eyepatch', 'kurt', 'prescription_01', 'prescription_02', 'round', 'sunglasses', 'wayfarers']:
      avatar.accessory = ""

   if avatar.clothes not in ['', 'blazer_shirt', 'blazer_sweater', 'collar_sweater', 'graphic_shirt',
   'hoodie', 'overall', 'shirt_crew_neck', 'shirt_scoop_neck', 'shirt_v_neck']:
      avatar.clothes = "graphic_shirt"

   if avatar.shirt_graphic not in ['', 'bat', 'bear', 'cumbia', 'custom_text', 'deer', 'diamond', 'hola',
   'pizza', 'resist', 'selena', 'skull_outline', 'skull']:
      avatar.shirt_graphic = "custom_text"

   if avatar.shirt_text != None:
      lenght = len(avatar.shirt_text)
      if avatar.shirt_text != "" and (lenght < 3 or lenght > 6):
         avatar.shirt_text = ""
   else:
      avatar.shirt_text = ""

   style = {
      "skinColor": avatar.skinColor,
      "clothesColor": avatar.clothesColor,
      "hairColor": avatar.hairColor,
      "beardColor": avatar.beardColor
   }

   if avatar.emotion == "Love":
      if (random.random() <= 0.25):
         avatar.emotion = "Love"
      else:
         avatar.emotion = "LoveX"

    # Create global Animation object
   an = None
   layer = None
   root = None
   if avatar.emotion == "Smile": 
      an = objects.Animation(90)
   else: 
      an = objects.Animation(60)

   # Body
   avatarStyle = pa.AvatarStyle.TRANSPARENT
   # Male
   # "character-2218185-0", "character-2218190-0", "character-2218204-0", "character-2218229-0", 
   # "man-with-glass-2218163-0", "michael-jackson-2218161-0", "photographer-2218230-0"
   # Female
   # "artist-2218153-0", "lady-2218164-0", "lady-teacher-2218147-0", "student-2218150-0"
   # Unisex
   # "winner-2218184-0", "basketball-player-2218183-0", "character-2218144-0", "character-2218171-0", "professor-2218155-0"
   body = "" # "character-2218185-0"
   if body != "" or avatar.emotion in ["Basketball", "Football"]:
      avatarStyle = pa.AvatarStyle.HEAD_ROUND

   if avatar.emotion not in ["Smile", "LoveX"]:
      my_avatar = pa.Avatar(
         style=avatarStyle,
         top=avatar.hair,
         hat_color=avatar.hatColor,
         eyebrows=avatar.eyebrows, 
         eyes=avatar.eyes, 
         nose=pa.NoseType.DEFAULT,
         mouth=avatar.mouth, 
         facial_hair_color=pa.HairColor.SILVER_GRAY, # DO NOT CHANGE HERE
         facial_hair=avatar.beard,
         # skin_color="#00FFFF",
         skin_color=pa.SkinColor.BLACK, # DO NOT CHANGE HERE
         hair_color=pa.HairColor.PASTEL_PINK, # DO NOT CHANGE HERE
         accessory=avatar.accessory,
         clothing_color=pa.ClothingColor.PINK, # DO NOT CHANGE HERE
         clothing=pa.ClothingType.fromString(avatar.clothes), 
         shirt_graphic=pa.ClothingGraphic.fromString(avatar.shirt_graphic), 
         shirt_text=avatar.shirt_text, # 'Name', # 3-6, 5 is better
         text_color=avatar.text_color, 
      )
      # my_avatar = pa.Avatar.random()
      # my_avatar.render("avatar.svg") # Save to file
      svgCode = my_avatar.render() # Get SVG string

      root = ET.fromstring(svgCode)
      svgImage = parse_svg_etree(root, colors=style)
      # svgImage = parse_svg_file(os.path.join(
      #     os.path.dirname(os.path.abspath(__file__)),
      #     "avatar.svg" # Vectornator export with "Responsive" toggled off (!) 
      # ))

      # Get ShapeLayer
      # layer = svgImage.find("squareLayer") # get layer by name
      layer = svgImage.layers[0] # get layer by index

      # Append to global animation
      an.add_layer(layer)

   if avatar.emotion == "Angry":
      Angry.animate(an, layer)
   elif avatar.emotion == "Love":
      Love.animate(an, layer)
      # layer.in_point = 0
      # layer.out_point = 90
      # Love.animate(an, layer, frames=90)
      AnimateAvatar.love(layer)
   elif avatar.emotion == "LoveX":
      if avatar.shirt_text != "":
         LoveNamed.animate(an, name=avatar.shirt_text)
         # LoveNamed.animate(an, name=shirt_text, frames=90)
      else:
         rand = random.random()
         if (rand <= 0.3):
            Love2.animate(an)
            # Love2.animate(an, frames=90) # 120
         elif (rand <= 0.65):
            Love3.animate(an, "I love\nyou")
            # Love3.animate(an, text="I love\nyou", frames=90)
         else:
            Love3.animate(an, "MISS\nYOU")
            # Love3.animate(an, text="MISS\nYOU", frames=90)
   elif avatar.emotion == "Amazing":
      Amazing.animate(an, layer)
   elif avatar.emotion == "Crying":
      AnimateAvatar.crying(layer)
      Crying.animate(an, layer)
   elif avatar.emotion == "Excited":
      Excited.animate(an, layer)
   elif avatar.emotion == "Sad":
      Sad.animate(an, layer)
      AnimateAvatar.sad(layer)
   elif avatar.emotion == "Laugh":
      copy2 = parse_svg_etree(root, colors=style).layers[0]
      copy3 = parse_svg_etree(root, colors=style).layers[0]
      Laugh.animate(an, layer, copy2, copy3) 
   elif avatar.emotion == "Wink":
      if (random.random() <= 0.5):
         Wink.animate(an, layer)
      else:
         Wink2.animate(an, layer)
   elif avatar.emotion == "Please":
      Please.animate(an, layer)
   elif avatar.emotion == "Smile":
      Cookie.animate(an)
   elif avatar.emotion == "Emotionless":
      Emotionless.animate(an, layer)
   elif avatar.emotion == "Basketball":
      Body.basket_ball(an, layer, avatarStyle, style)
   elif avatar.emotion == "Football":
      Body.football(an, layer, avatarStyle, style)
   else:
      easy = easing.Linear() # easing.Jump(), easing.EaseOut(1 / 10), easing.EaseIn(1 / 3), easing.Sigmoid(1 / 2)
      layer.transform.position.add_keyframe(0, Point(-280, -280), easy)
      layer.transform.position.add_keyframe(30, Point(256, 256), easy)
      layer.transform.position.add_keyframe(60, Point(512+280, 512+280), easy)

   if avatar.service == "telegram":
      # Export Telegram
      an.tgs_sanitize()
      lottie_dict = an.to_dict()
      lottie_dict["tgs"] = 1
      return JSONResponse(status_code=200, content=lottie_dict)
   else:
      # Export WhatsApp
      # temp = tempfile.NamedTemporaryFile(delete=False)
      # strip(an)
      # exporter.process(an, temp.name, **o_options)
      # return FileResponse(temp.name, filename="temp.webp", media_type="image/webp")

      async def streamer():
         temp = tempfile.NamedTemporaryFile(delete=True)
         strip(an)
         yield b''
         if avatar.emotion == "Basketball": # decrease size to be under 500kb
            options = { 'lossless': False, 'quality': 24, 'method': 0, 'skip_frames': 4 }
            exporter.process(an, temp.name, **options)
         else:
            exporter.process(an, temp.name, **o_options)
         yield b''
         yield temp.read()
         temp.close()

      return StreamingResponse(streamer(), media_type="image/webp")

@app.get("/")
def main():
   return FileResponse('web/app.html')

@app.get("/privacy")
def privacy():
   return FileResponse('web/privacy_policy.html')

@app.get("/terms")
def terms():
   return FileResponse('web/terms.html')

@app.get("/support")
def support():
   return PlainTextResponse("Avatar Stickers Support Page")

@app.get('/marketing')
def marketing():
   return PlainTextResponse("Avatar Stickers Marketing Page")

@app.get('/icon')
def icon():
   return FileResponse('web/icon.png')

@app.get("/favicon.ico")
def favicon():
   return FileResponse('web/favicon.ico') # icon.png

@app.get("/robots.txt")
def robots():
   return FileResponse('web/robots.txt')

# app.html
@app.get("/styles/index.css")
def style():
   return FileResponse('web/styles/index.css')

@app.get("/scripts/bodymovin.js")
def scripts_bodymovin():
   return FileResponse('web/scripts/bodymovin.js')

@app.get("/scripts/index.js")
def scripts_index():
   return FileResponse('web/scripts/index.js')

@app.get("/Jane/Amazing.json")
def amazing():
   return FileResponse('web/Jane/Amazing.json')

@app.get("/Jane/Laugh.json")
def laugh():
   return FileResponse('web/Jane/Laugh.json')

@app.get("/Jane/Love.json")
def love():
   return FileResponse('web/Jane/Love.json')