#!/usr/bin/env python

import re
import json
import urllib
import random

def get_tracks():
  url = 'http://ws.audioscrobbler.com/2.0/?method=track.getsimilar&artist=u2&track=With+or+Without+You&api_key=6b1730aec724adfbf0e21befc7385e6c&format=json'

  j = json.loads(urllib.urlopen(url).read())
  results = j['similartracks']['track']

  nodes = []
  links = []
  for obj in results:
    tracks = {}
    starget = {}
    song = re.sub(r'\W+', '_', obj['name']).lower()
    player = re.sub(r'\W+', '_', obj['artist']['name']).lower()
    song_id = "_".join([song, player])
    starget['source'] = "with_or_without_you_u2"
    starget['target'] = song_id
    tracks['match'] = obj['match']
    tracks['name'] = obj['name']
    tracks['artist'] = obj['artist']['name']
    tracks['playcount'] = obj['playcount']
    tracks['id'] = song_id
    nodes.append(tracks)
    links.append(starget)
    all_songs = json.dumps({'nodes': nodes, 'links': links}, indent=2)
  return all_songs

print(get_tracks())
