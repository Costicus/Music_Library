# Use this file to test your repository functions 

import pdb
from models.artist import Artist
from models.album import Album

import repositories.artist_repository as artist_repository
import repositories.album_repository as album_repository

artist_1 = Artist("RHCP")
artist_repository.save(artist_1)

album_1 = Album("Californication", artist_1)
album_repository.save(album_1)

result = artist_repository.select_all()
for artist in result:
    print (artist.__dict__)

result = album_repository.select_all()
for album in result:
    print (album.__dict__)
    print(album.__dict__["artist"].__dict__)

