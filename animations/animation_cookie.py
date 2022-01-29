import json
import os
import random
import textwrap
from lottie import Point, Color
from lottie.objects.properties import OffsetKeyframe
from lottie.objects.text import TextJustify
from lottie.parsers.svg.importer import parse_svg_file
from lottie.utils import color 
from lottie.objects import easing
from lottie.utils.font import FontStyle
from lottie import objects

cookies = [
   "The fortune you seek is in another cookie.",
   "Your reality check about to bounce.",
   "A closed mouth gathers no feet.",
   "A cynic is only a frustrated optimist.",
   "Learning by doing",
   "Nothing is impossible to a willing heart.",
   "Don’t pursue happiness – create it.",
   "Stop eating now. Food poisoning no fun.",
   "Drive like hell, you will get there.",
   "You think it’s a secret, but they know.",
   "Don’t eat the paper.",
   "You will die alone and poorly dressed.",
   "Nothing is so much to be feared as fear.",
   "The real kindness comes from within you.",
   "The older you get, the better you were.",
   "Age is high price to pay for maturity.",
   "A fool and his money are soon partying.",
   # "Do not mistake temptation for opportunity.",
   "Flattery will go far tonight.",
   "He who laughs last is laughing at you.",
   "He who throws dirt is losing ground.",
   "Someone will invite you to a Karaoke party.",
   "That wasn’t chicken.",
   "You love Chinese food.",
   "I am worth a fortune.",
   # "The usefulness of a cup is in its emptiness.",
   "He who throws mud loses ground.",
   "He who dies with most toys, still dies.",
   "Practice safe eating. Always use condiments.",
   "Atheism no fun. No holidays.",
   # "You have kleptomania. Take something for it.",
   "The greatest danger could be your stupidity.",
   "You will be hungry again in one hour.",
   "Don’t behave with cold manners.",
   "Don’t forget you are always on our minds.",
   "Fortune not found? Abort, Retry, Ignore.",
   "It’s about time I got out of that cookie.",
   "Big journeys begin with a single step.",
   "You have a secret admirer.",
   "Love, because it is the only true adventure.",
   "An old love will come back to you.",
   "Follow what calls you.",
   "Follow what you love and see what turns up.",
   "Be passionate and totally worth the chaos.",
   "Enter unknown territory.",
   "You should def go for it.",
   "Everything that is was first a dream.",
   "Make self care a non-negotiable.",
   "Love yourself hard.",
   # "Set yourself up to experience what you love.",
   "Focus on the magic of things; yourself.",
   "Self acceptance > self improvement",
   "To be found, stop hiding.",
   "A faithful friend is a strong defense.",
   "A fresh start will put you on your way.",
   "A friend is a present you give yourself.",
   "A good time to finish up old tasks.",
   "A lifetime friend shall soon be made.",
   "A lifetime of happiness lies ahead of you.",
   "A person is never to (sic) old to learn.",
   "A pleasant surprise is waiting for you.",
   "A smile is your personal welcome mat.",
   "A smooth long journey! Great expectations.",
   "A soft voice may be awfully persuasive.",
   "Adventure can be real happiness.",
   "Advice, when most needed, is least heeded.",
   "All will go well with your new project.",
   "All your hard work will soon pay off.",
   "Allow compassion to guide your decisions.",
   "An important person will offer you support.",
   "An inch of time is an inch of gold.",
   "Beauty in its various forms appeals to you.",
   "Believe in yourself and others will too.",
   "Believe it can be done.",
   "Better ask twice than lose yourself once.",
   "Bide your time, for success is near.",
   "Competence like yours is underrated.",
   "Congratulations! You are on your way.",
   "Could I get some directions to your heart?",
   "Courtesy begins in the home.",
   "Courtesy is contagious.",
   "Determination is what you need now.",
   "Disbelief destroys the magic.",
   "Distance yourself from the vain.",
   "Do not make extra work for yourself.",
   "Don’t confuse recklessness with confidence.",
   "Don’t just spend time. Invest it.",
   "Don’t just think, act!",
   "Embrace this love relationship you have!",
   "Emulate what you admire in your parents.",
   "Emulate what you respect in your friends.",
   "Every flower blooms in its own sweet time.",
   "Everyday in your life is a special occasion.",
   "Failure is the path of lease persistence.",
   "Fortune Not Found: Abort, Retry, Ignore?",
   "Go take a rest; you deserve it.",
   "Good news will be brought to you by mail.",
   "Good news will come to you by mail.",
   "Good to begin well, better to end well.",
   "Happiness will bring you good luck.",
   "Happy life is just in front of you.",
   "Have a beautiful day.",
   "He who knows he has enough is rich.",
   "How you look depends on where you go.",
   "I learn by going where I have to go.",
   "Imagination rules the world.",
   "In order to take, one must first give.",
   "In the end all things will be known.",
   "It is worth reviewing some old lessons.",
   "It takes courage to admit fault.",
   "Listen not to vain words of empty tongue.",
   "Long life is in store for you.",
   "Love is a warm fire to keep the soul warm.",
   "Love lights up the world.",
   "Love truth, but pardon error.",
   "Many will travel to hear you speak.",
   "Meditation with an old enemy is advised.",
   "Miles are covered one step at a time.",
   "New ideas could be profitable.",
   # "No one can walk backwards into the future.",
   "Now is a good time to buy stock.",
   "Now is the time to try something new",
   "Now is the time to try something new.",
   "Observe all men, but most of all yourself.",
   "Others can help you now.",
   "Place special emphasis on old friendship.",
   "Please visit us at www.wontonfood.com",
   "Practice makes perfect.",
   "Remember the birthday but never the age.",
   "Romance moves you in a new direction.",
   "Savor your freedom – it is precious.",
   "Self-knowledge is a life long process.",
   "Someone you care about seeks reconciliation.",
   "Soon life will become more interesting.",
   "Stand tall. Don’t look down upon yourself.",
   "Strong reasons make strong actions.",
   "Success is a journey, not a destination.",
   "Success is failure turned inside out.",
   "Swimming is easy. Stay floating is hard.",
   "Take the high road.",
   "The best prediction of future is the past.",
   "The harder you work, the luckier you get.",
   "The night life is for you.",
   "The weather is wonderful.",
   "There is no wisdom greater than kindness.",
   "There’s no such thing as an ordinary cat.",
   "Things don’t just happen; they happen just.",
   "Those who care will make the effort.",
   "To know oneself, one should assert oneself.",
   "Tonight you will be blinded by passion.",
   "Welcome change.",
   "“Welcome” is a powerful word.",
   "Well done is better than well said.",
   "What’s hidden in an empty box?",
   # "When your heart is pure, your mind is clear.",
   "Wish you happiness.",
   "With age comes wisdom.",
   "You always bring others happiness.",
   "You are a person of another time.",
   "You are a talented storyteller.",
   "You are almost there.",
   "You are busy, but you are happy.",
   "You are going to have some new clothes.",
   "You are in good hands this evening.",
   "You are modest and courteous.",
   "You are solid and dependable.",
   "You are talented in many ways.",
   "You are the master of every situation.",
   "You are working hard.",
   "You can keep a secret.",
   "You can see a lot just by looking.",
   "You desire recognition and you will find it.",
   "You have a yearning for perfection.",
   "You have exceeded what was expected.",
   "You have had a good start. Work harder!",
   "You have yearning for perfection.",
   "You look pretty.",
   "You love challenge.",
   "You love chinese food.",
   "You never know who you touch.",
   "You only treasure what you lost.",
   "You should pay for this check. Be generous.",
   "You will be blessed with longevity.",
   "You will be pleasantly surprised tonight.",
   "You will be successful in your work.",
   "You will become more and more wealthy.",
   "You will enjoy good health.",
   "You will have gold pieces by the bushel.",
   "You will inherit a large sum of money.",
   "You will make change for the better.",
   "Your abilities are unparalleled.",
   "Your ability is appreciated.",
   "Your biggest virtue is your modesty.",
   # "Your difficulties will strengthen you.",
   "Your energy returns and you get things done.",
   "Your family is young, gifted and attractive.",
   # "Your first love has never forgotten you.",
   "Your goal will be reached very soon.",
   "Your hard work will payoff today.",
   "Your home is the center of great love.",
   "Your ideals are well within your reach.",
   "Your life will be happy and peaceful.",
   "Your life will get more and more exciting.",
   "Your love life will be happy and harmonious.",
   "Your mind is creative, original and alert.",
   "Your mind is your greatest asset.",
   "Your moods signal a period of change.",
   "Your reputation is your wealth.",
   "Your success will astonish everyone.",
   "Plan for many pleasures ahead.",
   # "The joyfulness of a man prolongeth his days.",
   "Something you lost will soon turn up.",
   "A pleasant surprise is in store for you.",
   "May life throw you a pleasant curve.",
   "As the purse is emptied the heart is filled.",
   # "Be mischievous and you will not be lonesome.",
   "Don’t forget, you are always on our minds.",
   "Good luck is the result of good planning.",
   "Good things are being said about you.",
   "Someone is speaking well of you.",
   "The time is right to make new friends.",
   "Your life will be happy and peaceful.",
   "A friend is a present you give yourself.",
   "Happy news is on its way to you.",
   "The beginning of wisdom is to desire it.",
   "You will have a very pleasant experience.",
   "You will live a long, happy life.",
   "You will step on the soil of many countries.",
   "You will witness a special ceremony.",
   "You will be invited to an exciting event.",
   "Nothing is impossible to a willing heart.",
   "Don’t pursue happiness – create it.",
   "Nothing is so much to be feared as fear.",
   "The real kindness comes from within you.",
   # "The usefulness of a cup is in its emptiness.",
   "He who throws mud loses ground.",
   "Big journeys begin with a single step.",
   "Don't wait for success to come - go find it!",
   "Your smile lights up someone else's day.",
   "If you have an idea, make it into reality.",
   "Everyone agrees you are the best.",
   "Don't worry what others think of you.",
   "Free your mind, and the rest will follow.",
   "Everyone agrees you are the best.",
   "To achieve wisdom, you must first desire it.",
   "To be idle is to be foolish.",
   "Worry does not beget change.",
   "Work with what you have.",
   "Pursue your dreams with vigor.",
   "Everyone agrees you are the best.",
   "You excel at pleasing others.",
   "If you have an idea, make it into reality.",
   "Get ready for a life-changing event!",
   "Stop letting other people stand in your way.",
   "Work with what you have.",
   "Work first, but make sure to play later.",
   "Your smile lights up someone else's day.",
   "Face the truth with dignity.",
   "To achieve wisdom, you must first desire it.",
   "Somebody appreciates the unique you.",
   "Stop letting other people stand in your way.",
   "If you have an idea, make it into reality.",
   "Do your job to the best of your ability.",
   "Learn how to do something new today.",
   "Fall for someone who's not your type.",
   "If you can dream it, you can become it!",
   "A gathering of friends will bring you luck",
   "Get ready for a life-changing event!",
   "Happiness may be right under your nose.",
   "A healthy body will benefit you for life.",
   "Worry does not beget change.",
   "Do your job to the best of your ability?",
   "An exciting adventure awaits you.",
   "Anxiety won't help your problems.",
   "Be at peace with yourself.",
   "Free your mind, and the rest will follow.",
   "Trust your friends, but keep your eyes open.",
   "Somebody appreciates the unique you.",
   "Fame and fortune lie ahead.",
   "Free your mind, and the rest will follow.",
   "A healthy body will benefit you for life.",
   "You have good reason to be self-confident.",
   "Go with your gut feeling.",
   "A healthy body will benefit you for life.",
   "Work first, but make sure to play later.",
   "If we are all worms, try to be a glow worm",
   "Ignore previous cookie",
   "Why you always think about it?",
   "Enjoy yourself while you can",
   "True happiness makes us wise.",
   "Work first, but make sure to play later.",
   "Fame and fortune lie ahead.",
]

class Cookie:
   def animate(an):
      easy = easing.EaseOut(1 / 4)

      cookie_left = parse_svg_file(os.path.join(
         os.path.dirname(os.path.abspath(__file__)),
         "assets/images/fortune-cookie-left.svg"
      )).layers[0]
      an.add_layer(cookie_left)
      cookie_left.transform.scale.value = Point(20, 20)
      
      for stroke in cookie_left.find_all((objects.Stroke)):
         if stroke.color.value == Color(0.9372549019607843, 0.21568627450980393, 0.023529411764705882, 1):
            stroke.color.value = color.from_uint8(255, 83, 83) 
      for fill in cookie_left.find_all((objects.Fill)):
         if fill.color.value == Color(0.9372549019607843, 0.21568627450980393, 0.023529411764705882, 1):
            fill.color.value = color.from_uint8(255, 83, 83) 

      cookie_left.transform.anchor_point.value = Point(512, 512)
      cookie_left.transform.rotation.add_keyframe(0, 0, easy)
      cookie_left.transform.rotation.add_keyframe(10, -45, easy)
      cookie_left.transform.rotation.add_keyframe(60, -60, easy)

      cookie_left.transform.position.value = Point(142, 230)
      cookie_left.transform.position.add_keyframe(0, Point(142, 230), easy)
      cookie_left.transform.position.add_keyframe(40, Point(-64, 596), easy)

      cookie_left.transform.opacity.add_keyframe(0, 100, easy)
      cookie_left.transform.opacity.add_keyframe(30, 80, easy)
      cookie_left.transform.opacity.add_keyframe(50, 40, easy)
      cookie_left.transform.opacity.add_keyframe(60, 0, easy)

      cookie_right = parse_svg_file(os.path.join(
         os.path.dirname(os.path.abspath(__file__)),
         "assets/images/fortune-cookie-right.svg"
      )).layers[0]
      an.add_layer(cookie_right)
      cookie_right.transform.scale.value = Point(20, 20)

      for stroke in cookie_right.find_all((objects.Stroke)):
         if stroke.color.value == Color(0.9372549019607843, 0.21568627450980393, 0.023529411764705882, 1):
            stroke.color.value = color.from_uint8(255, 83, 83) 
      for fill in cookie_right.find_all((objects.Fill)):
         if fill.color.value == Color(0.9372549019607843, 0.21568627450980393, 0.023529411764705882, 1):
            fill.color.value = color.from_uint8(255, 83, 83) 


      cookie_right.transform.anchor_point.value = Point(512, 512)
      cookie_right.transform.rotation.add_keyframe(0, 0, easy)
      cookie_right.transform.rotation.add_keyframe(10, 20, easy)
      cookie_right.transform.rotation.add_keyframe(60, 30, easy)

      cookie_right.transform.position.value = Point(126.5, 230.5)
      cookie_right.transform.position.add_keyframe(0, Point(126.5, 230.5), easy)
      cookie_right.transform.position.add_keyframe(10, Point(256, 256), easy)
      cookie_right.transform.position.add_keyframe(20, Point(316, 356), easy)
      cookie_right.transform.position.add_keyframe(40, Point(384, 444), easy)
      cookie_right.transform.position.add_keyframe(60, Point(546, 564), easy)

      cookie_right.transform.opacity.add_keyframe(0, 100, easy)
      cookie_right.transform.opacity.add_keyframe(30, 80, easy)
      cookie_right.transform.opacity.add_keyframe(50, 40, easy)
      cookie_right.transform.opacity.add_keyframe(60, 0, easy)
      
      text_layer = objects.ShapeLayer()
      an.add_layer(text_layer)
      style = FontStyle("animations/assets/fonts/Pacifico-Regular.ttf", 64, justify=TextJustify.Center) 
      text = random.choice(cookies) 
      lines = textwrap.fill(text, 13, max_lines=4)
      
      t = text_layer.add_shape(style.render(lines))
      line_count = len(lines.split('\n'))
      if line_count == 1:
         t.transform.position.value.y = 272
      elif line_count == 2:
         t.transform.position.value.y = 236
      elif line_count == 3:
         t.transform.position.value.y = 196
      elif line_count == 4:
         t.transform.position.value.y = 136
      t.transform.position.value.x = 256

      fill = text_layer.add_shape(objects.Fill(Color(240/255, 91/255, 67/255))) # Color(147/255, 120/255, 1)
      fill.opacity.add_keyframe(0, 0)
      fill.opacity.add_keyframe(20, 0)
      fill.opacity.add_keyframe(40, 100)
      stroke = text_layer.add_shape(objects.Stroke(Color(1, 1, 1), 20))
      stroke.opacity.add_keyframe(0, 0, easy)
      stroke.opacity.add_keyframe(30, 0, easy)
      stroke.opacity.add_keyframe(40, 100, easy)

      with open("animations/assets/lottie/confetti.json") as file:
         data = json.load(file)
         
         an2 = objects.Animation.load(data)
         an2.width = 512
         an2.height = 512
         an2.frame_rate = 30
         an2.in_point = 0
         an2.out_point = 60
      
         for layer in an2.layers:
            layer.transform.scale.value = [75, 75, 0]

            layer.in_point = 0
            layer.out_point = 60
            for keyframe in layer.find_all((OffsetKeyframe)):
               keyframe.time *= 1.3

            an.add_layer(layer)