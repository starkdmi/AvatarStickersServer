//["Amazing", "Angry", "Crying", "Emotionless", "Excited", "Laugh", "Love", "Please", "Sad", "Smile", "Wink"]
["Amazing", "Laugh", "Love"].forEach(function (emotion, index) {
   bodymovin.loadAnimation({
      container: document.getElementById(emotion),
      renderer: 'svg',
      loop: true,
      autoplay: true,
      path: 'Jane/' + emotion + '.json'
   })
});
