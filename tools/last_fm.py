#!/usr/bin/env python

import re
import json
import urllib


def get_tracks():
  url = 'http://ws.audioscrobbler.com/2.0/?method=track.getsimilar&artist=u2&track=With+or+Without+You&api_key=6b1730aec724adfbf0e21befc7385e6c&format=json'

  j = json.loads(urllib.urlopen(url).read())
  results = j['similartracks']['track']

  starget = {}
  tracks = {}
  for obj in results:
    song = re.sub(r'\W+', '_', obj['name']).lower()
    player = re.sub(r'\W+', '_', obj['artist']['name']).lower()
    song_id = "_".join([song, player])
    starget['source'] = song_id

    tracks['match'] = obj['match']
    tracks['name'] = obj['name']
    tracks['artist'] = obj['artist']['name']
    tracks['playcount'] = obj['playcount']
    tracks['id'] = song_id
    #nodes.append(tracks)

    data = json.dumps(tracks, indent=2, sort_keys=True)

    #sources = json.dumps(starget, indent=2)
    #data = json.dumps([tracks for tracks in nodes], indent=2)


    yield data
    #yield sources

track_generator = get_tracks()

nodes = []
for items in track_generator:
  nodes.append(items)
  print nodes
