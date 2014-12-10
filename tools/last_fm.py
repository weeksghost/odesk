#!/usr/bin/env python

import re
import json
import urllib


def get_tracks():
  url = 'http://ws.audioscrobbler.com/2.0/?method=track.getsimilar&artist=u2&track=With+or+Without+You&api_key=6b1730aec724adfbf0e21befc7385e6c&format=json'

  j = json.loads(urllib.urlopen(url).read())
  results = j['similartracks']['track']

  tracks = {}
  for obj in results:
    song = re.sub(r'\W+', '_', obj['name']).lower()
    player = re.sub(r'\W+', '_', obj['artist']['name']).lower()
    song_id = "_".join([song, player])
    tracks['match'] = obj['match']
    tracks['name'] = obj['name']
    tracks['artist'] = obj['artist']['name']
    tracks['playcount'] = obj['playcount']
    tracks['id'] = song_id
    data = json.dumps(tracks, indent=2, sort_keys=True)
    yield data

track_generator = get_tracks()

for items in track_generator:
  print items
