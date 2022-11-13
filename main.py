from flask import Flask, render_template, jsonify, request
import json
import random

app = Flask(__name__)

@app.route('/fetch')
def fetch():
  data = {
  "one": [
    "Bitch, ",
    "Fact: ",
    "Everybody says ",
    "Dang... ",
    "Check it: ",
    "Just saying... ",
    "Superstar ",
    "Tiger ",
    "Self, ",
    "Know this: ",
    "News alert: ",
    "Girl, ",
    "Boy, ",
    "Motherfucker, ",
    "Hold the fuck up: ",
    "Experts agree: ",
    "In my opinion, ",
    "Hear ye, hear ye ",
    "Okay, listen the fuck up: "
  ],
  "two": [
    "the mere idea of you ",
    "your soul ",
    "your hair today ",
    "everything you do ",
    "your personal style ",
    "every thought you have ",
    "that sparkle in your eye ",
    "your prescence here ",
    "what you got going on ",
    "the essential you ",
    "your life's journey ",
    "that saucy personality ",
    "your DNA ",
    "that brain of yours ",
    "your choice of attire ",
    "the way you roll ",
    "whatever your secret is ",
    "your ass "
  ],
  "three": [
    "has serious game. ",
    "rains magic. ",
    "deserves the nobel prize. ",
    "raises the roof. ",
    "breeds miracles. ",
    "is paying off big time. ",
    "shows mad skills. ",
    "just shimmers. ",
    "is a national treasure. ",
    "gets the party hopping. ",
    "is the next big thing. ",
    "roars like a lion. ",
    "is a rainbow factory. ",
    "is made of diamonds. ",
    "makes birds sing. ",
    "should be taught in school. ",
    "makes my world go round. ",
    "is 100% legit. "
  ],
  "four": [
    "24/7",
    "can I get an amen?",
    "and that's a fact",
    "so treat yourself",
    "you feel me?",
    "that's just science",
    "would I lie?",
    "for reals",
    "mic drop",
    "you hidden gem",
    "snuggle bear",
    "period",
    "can I get an amen",
    "now let's dance",
    "high five",
    "say it again!",
    "according to InfoWars",
    "according to Fox News",
    "so get used to it",
    f"Unfortunately, {request.environ['HTTP_X_FORWARDED_FOR']}"
  ]
}
  return jsonify(
    one = random.choice(data["one"]),
    two = random.choice(data["two"]),
    three = random.choice(data["three"]),
    four = random.choice(data["four"]),
  )

@app.route('/')
def index():
    return render_template('index.html')


app.run(host='0.0.0.0', port=81)
