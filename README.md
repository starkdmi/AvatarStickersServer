## About
Python Server for [Avatar Stickers](https://apps.apple.com/us/app/avatar-stickers/id1574023061) iOS Application. Source code of iOS application available [here](https://github.com/starkdmi/AvatarStickers). The application was created while participating in the [contest](https://contest.com/sticker-app). Server generates animations in [TGS](https://core.telegram.org/animated_stickers) and WebP formats using [Lottie](https://airbnb.io/lottie).

## Ready to use
You can deploy server on Heroku in a minute

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/starkdmi/AvatarStickersServer)

Demo server is available at [facemotion.herokuapp.com](https://facemotion.herokuapp.com). It automatically deployed from **main** branch on changes. 

Demo server isn't used in production and uses free dyno plan. 

## Build locally
### Requirements
- Python 3.8 (or newer)

### Build
``` Bash
# Clone
git clone 'https://github.com/starkdmi/AvatarStickersServer'
cd AvatarStickersServer

# Install requirements
pip install -r requirements.txt

# Run
python -m uvicorn app:app --host=macpro.home --port=5000 --reload
```
Use local network hostname to easily access the server from mobile device while testing.

## Usage
### Fields
| Field | Description | Type | Default | Values | Required |
| --- | --- | --- | --- | --- | --- |
| service | Messenger name | String | telegram | telegram, whatsapp | YES |
| emotion | Name of animation | String | | Amazing, Excited, Laugh, Please, Love, Sad, Angry, Crying, Emotionless, Smile, Wink, Football, Basketball | YES |
| hair | Hair style or Hat type | String | no_hair | **Hair Styles:** no_hair, big_hair, bob, bun, caesar_side_part, caesar, curly, curvy, dreads, frida, 'rizzle, fro_band, fro, long_not_too_long, mia_wallace, shaggy_mullet, shaggy, shaved_sides, short_curly, short_dreads_1, short_dreads_2, short_flat, short_round, short_waved, sides, straight_1, straight_2, straight_strand </br></br> **Hats:** hat, hijab, turban, winter_hat_1, winter_hat_2, winter_hat_3, winter_hat_4 | NO |
| eyebrows | Eyebrows type | String | default | closed, cry, default, eye_roll, happy, heart, side, surprised, wink_wacky, wink, x_dizzy, squint | NO |
| eyes | Eyes type | String | default | '', angry_natural, default_natural, default, flat_natural, frown_natural, up_down, up_down_natural, raised_excited_natural, raised_excited, sad_concerned_natural, sad_concerned, unibrow_natural, angry | NO |
| mouth | Mouth emotion | String | default | concerned, default, disbelief, eating, grimace, sad, scream_open, serious, smile, tongue, twinkle, vomit | NO |
| beard | Facial hair style | String | '' | '', beard_light, beard_magestic, beard_medium, moustache_fancy, moustache_magnum | NO |
| gender | Sex | String | male | male, female | NO |
| accessory | Accessories type | String | '' | '', eyepatch, kurt, prescription_01, prescription_02, round, sunglasses, wayfarers | NO |
| clothes | Clothes | String | graphic_shirt | '', blazer_shirt, blazer_sweater, collar_sweater, graphic_shirt, hoodie, overall, shirt_crew_neck, shirt_scoop_neck, shirt_v_neck | NO |
| shirt_graphic | Draw an icon on clothes. Field **clothes** should be set to **graphic_shirt**. | String | custom_text | '', bat, bear, cumbia, custom_text, deer, diamond, hola, pizza, resist, selena, skull_outline, skull | NO |
| shirt_text | Text written on clothes. Field **shirt_graphic** should be set to **custom_text**. | String | '' | Some text | NO |
| clothesColor | Clothes color | String | | HEX String - #FFFFFF | NO |
| beardColor | Facial hair color | String | | HEX String - #FFFFFF | NO |
| hairColor | Hair color | String | | HEX String - #FFFFFF | NO |
| hatColor | Hat color | String | | HEX String - #FFFFFF | NO |
| skinColor | Skin tone color | String | | HEX String - #FFFFFF | NO |
| text_color | Text color | String | | HEX String - #FFFFFF | NO |

### Example
```
curl -X POST \
      -H 'Accept: application/json' \
      -H 'Content-type: application/json' \
      -H 'Token: SERVER_TOKEN' \
      -d '{"hatColor": "#25557C", "gender": "female", "text_color": "#EDF1F2", "shirt_graphic": "resist", "beardColor": "#B58143", "mouth": "smile", "hairColor": "#B58143", "skinColor": "#D08B5B", "accessory": "", "eyes": "happy", "clothesColor": "#25557C", "hair": "long_not_too_long", "shirt_text": "", "clothes": "hoodie", "beard": "", "emotion": "Football", "eyebrows": "default"}' 'http://macpro.home:5000/avatar' >> animation.json
```

## Licenses • Attribution
- [python_avatars](https://github.com/ibonn/python_avatars) - MIT
- [python-lottie](https://gitlab.com/mattbas/python-lottie) - GNU AGPLv3
- [lottie-web](https://github.com/airbnb/lottie-web) - MIT
- [twemoji](https://github.com/twitter/twemoj) - MIT
- [Pacifico](https://fonts.google.com/specimen/Pacifico?query=Pacifico#about) - Open Font License
- [Faster One](https://fonts.google.com/specimen/Faster+One?query=Faster+One#about) - Open Font License
- [Gee-me](https://iconscout.com/illustrations/gee-me) - CC 4.0
