import os
import json
import tempfile

path = '/Users/starkdmi/Projects/TGStickersImport/MockupAnimations/'
path2 = '/Users/starkdmi/Projects/TGStickersImport/MockupAnimations/Avatar3/'
emotions = ["Amazing", "Angry", "Crying", "Emotionless", "Excited", "Laugh", "Love", "Please", "Sad", "Smile", "Wink"]

for emotion in emotions:
   with open(path + 'avatar_3/' + emotion + '_' + '3.json') as json_file:
      data = json.load(json_file)

      with open(path2 + emotion + '.json', 'w') as outfile:
         outfile.write(data)