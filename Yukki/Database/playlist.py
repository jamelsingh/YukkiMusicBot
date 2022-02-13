from typing import Dict, List, Union

from Yukki import db

playlistdb_lofi = db.playlistlofi
playlistdb_rock = db.playlistrock
playlistdb_sad = db.playlistsad
playlistdb_party = db.playlistparty
playlistdb_bollywood = db.playlistbollywood
playlistdb_hollywood = db.playlisthollywood
playlistdb_punjabi = db.playlistpunjabi
playlistdb_others = db.playlistothers


async def _get_playlists(chat_id: int, type: str) -> Dict[str, int]:
    if type == "90sSong":
        xd = playlistdb_lofi
    elif type == "HitSong":
        xd = playlistdb_rock
    elif type == "SadSong":
        xd = playlistdb_sad
    elif type == "NewSong":
        xd = playlistdb_party
    elif type == "ARRSong":
        xd = playlistdb_bollywood
    elif type == "LoveSong":
        xd = playlistdb_hollywood
    elif type == "MelodySong":
        xd = playlistdb_punjabi
    elif type == "OtherSong":
        xd = playlistdb_others
    _notes = await xd.find_one({"chat_id": chat_id})
    if not _notes:
        return {}
    return _notes["notes"]


async def get_playlist_names(chat_id: int, type: str) -> List[str]:
    _notes = []
    _notes.extend(iter(await _get_playlists(chat_id, type)))
    return _notes


async def get_playlist(
    chat_id: int, name: str, type: str
) -> Union[bool, dict]:
    name = name
    _notes = await _get_playlists(chat_id, type)
    return _notes[name] if name in _notes else False


async def save_playlist(chat_id: int, name: str, note: dict, type: str):
    name = name
    _notes = await _get_playlists(chat_id, type)
    _notes[name] = note
    if type == "90sSong":
        xd = playlistdb_lofi
    elif type == "HitSong":
        xd = playlistdb_rock
    elif type == "SadSong":
        xd = playlistdb_sad
    elif type == "NewSong":
        xd = playlistdb_party
    elif type == "ARRSong":
        xd = playlistdb_bollywood
    elif type == "LoveSong":
        xd = playlistdb_hollywood
    elif type == "MelodySong":
        xd = playlistdb_punjabi
    elif type == "OtherSong":
        xd = playlistdb_others
    await xd.update_one(
        {"chat_id": chat_id}, {"$set": {"notes": _notes}}, upsert=True
    )


async def delete_playlist(chat_id: int, name: str, type: str) -> bool:
    notesd = await _get_playlists(chat_id, type)
    name = name
    if type == "90sSong":
        xd = playlistdb_lofi
    elif type == "HitSong":
        xd = playlistdb_rock
    elif type == "SadSong":
        xd = playlistdb_sad
    elif type == "NewSong":
        xd = playlistdb_party
    elif type == "ARRSong":
        xd = playlistdb_hollywood
    elif type == "LoveSong":
        xd = playlistdb_lovesong
    elif type == "MelodySong":
        xd = playlistdb_punjabi
    elif type == "OtherSong":
        xd = playlistdb_others
    if name in notesd:
        del notesd[name]
        await xd.update_one(
            {"chat_id": chat_id}, {"$set": {"notes": notesd}}, upsert=True
        )
        return True
    return False
