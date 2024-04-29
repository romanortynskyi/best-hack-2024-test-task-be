from typing import List
from flask import request

class AddSongRequestDto:
  def __init__(self, name, featured_artist_ids, file):
    self.name = name
    self.featured_artist_ids = featured_artist_ids
    self.file = file
