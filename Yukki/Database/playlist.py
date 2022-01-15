from typing import Dict, List, Union

from Yukki import db

playlistdb_90ssong = db.playlist90sSong
playlistdb_hitSong = db.playlisthitSong
playlistdb_sadsong = db.playlistsadsong
playlistdb_newsong = db.playlistnewsong
playlistdb_arrsong = db.playlistarrsong
playlistdb_lovesong = db.playlistlovesong
playlistdb_melodysong = db.playlistmelodysong
playlistdb_otherssong = db.playlistothersong


async def _get_playlists(chat_id: int, type: str) -> Dict[str, int]:
    if type == "90sSong":
        xd = playlistdb_90ssong
    elif type == "HitSong":
        xd = playlistdb_hitSong
    elif type == "SadSong":
        xd = playlistdb_sadsong
    elif type == "NewSong":
        xd = playlistdb_newsong
    elif type == "ARRSong":
        xd = playlistdb_arrsong
    elif type == "LoveSong":
        xd = playlistdb_lovesong
    elif type == "MelodySong":
        xd = playlistdb_melodysong
    elif type == "OtherSong":
        xd = playlistdb_othersong
    _notes = await xd.find_one({"chat_id": chat_id})
    if not _notes:
        return {}
    return _notes["notes"]


async def get_playlist_names(chat_id: int, type: str) -> List[str]:
    _notes = []
    for note in await _get_playlists(chat_id, type):
        _notes.append(note)
    return _notes


async def get_playlist(
    chat_id: int, name: str, type: str
) -> Union[bool, dict]:
    name = name
    _notes = await _get_playlists(chat_id, type)
    if name in _notes:
        return _notes[name]
    else:
        return False


async def save_playlist(chat_id: int, name: str, note: dict, type: str):
    name = name
    _notes = await _get_playlists(chat_id, type)
    _notes[name] = note
    if type == "90sSong":
        xd = playlistdb_90ssong
    elif type == "HitSong":
        xd = playlistdb_hitSong
    elif type == "SadSong":
        xd = playlistdb_sadsong
    elif type == "NewSong":
        xd = playlistdb_newsong
    elif type == "ARRSong":
        xd = playlistdb_arrsong
    elif type == "LoveSong":
        xd = playlistdb_lovesong
    elif type == "MelodySong":
        xd = playlistdb_melodysong
    elif type == "OtherSong":
        xd = playlistdb_othersong
    await xd.update_one(
        {"chat_id": chat_id}, {"$set": {"notes": _notes}}, upsert=True
    )


async def delete_playlist(chat_id: int, name: str, type: str) -> bool:
    notesd = await _get_playlists(chat_id, type)
    name = name
    if type == "90sSong":
        xd = playlistdb_90ssong
    elif type == "HitSong":
        xd = playlistdb_hitSong
    elif type == "SadSong":
        xd = playlistdb_sadsong
    elif type == "NewSong":
        xd = playlistdb_newsong
    elif type == "ARRSong":
        xd = playlistdb_arrsong
    elif type == "LoveSong":
        xd = playlistdb_lovesong
    elif type == "MelodySong":
        xd = playlistdb_melodysong
    elif type == "OtherSong":
        xd = playlistdb_othersong
    if name in notesd:
        del notesd[name]
        await xd.update_one(
            {"chat_id": chat_id}, {"$set": {"notes": notesd}}, upsert=True
        )
        return True
    return False
