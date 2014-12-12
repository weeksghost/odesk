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
    sid = obj['name'] + '_' + obj['artist']['name']
    sid = re.sub(r'[^\x00-\x7F]+', '', sid)
    sid = re.sub(r'/\s+/', '_', sid)
    sid = re.sub(r'\W+', '', sid).lower()
    starget['source'] = "with_or_without_you_u2"
    starget['target'] = sid
    tracks['match'] = obj['match']
    tracks['name'] = obj['name']
    tracks['artist'] = obj['artist']['name']
    tracks['playcount'] = obj['playcount']
    tracks['id'] = sid
    nodes.append(tracks)
    links.append(starget)
    all_songs = json.dumps({'nodes': nodes, 'links': links}, indent=2)
  return all_songs

print(get_tracks())
