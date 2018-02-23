from flask import Flask, jsonify
from flask_prometheus import monitor
import random

app = Flask(__name__)

@app.route('/api/songs/random')
def songs_random():
    song_names = ['Beautiful Soup', 'The Queen Of Hearts', 'The Lion And The Unicorn',
    			  'Pig And Pepper', 'Terminal', 'Tis The Voice Of The Lobster', 'The Fish Riddle']
    song_name = random.choice(song_names)
    return jsonify(name=song_name, url='https://freepd.com/Simple/{}.mp3'.format(song_name))

monitor(app, port=8000)
app.run(host='0.0.0.0', port=5000)
