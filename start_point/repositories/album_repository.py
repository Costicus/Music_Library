from db.run_sql import run_sql
from models.artist import Artist
from models.album import Album
import repositories.album_repository as album_repository
import repositories.artist_repository as artist_repository


def save(album):
    sql = "INSERT INTO albums (title, artist_id) VALUES (%s, %s) RETURNING *"
    values = [album.title, album.artist.id]
    results = run_sql(sql, values)
    id = results[0]['id']
    album.id = id
    return album

def select_all():
    albums = []
    sql = "SELECT * FROM albums"
    results = run_sql(sql)

    for row in results:
        artist = artist_repository.select(row ['artist_id'])
        album = Album(row ['title'], artist, row ['id'])
        albums.append(album)
    return albums

def select(id):
    album = None
    sql = "SELECT * FROM albums WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)
    if results:
        result = results[0]
        artist = artist_repository.select(result['artist_id'])
        album = Album(result['title'], artist, result['id'])
    return album

def delete_all():
    sql = "DELETE FROM albums"
    run_sql(sql)
    