from pyrogram.types import (CallbackQuery, InlineKeyboardButton,
                            InlineKeyboardMarkup, InputMediaPhoto, Message)


def check_markup(user_name, user_id, videoid):
    buttons = [
        [
            InlineKeyboardButton(
                text=f"Group's Playlist",
                callback_data=f"playlist_check {user_id}|Group|{videoid}",
            ),
            InlineKeyboardButton(
                text=f"{user_name[:8]}'s Playlist",
                callback_data=f"playlist_check {user_id}|Personal|{videoid}",
            ),
        ],
        [InlineKeyboardButton(text="🗑 Close Menu", callback_data="close")],
    ]
    return buttons


def playlist_markup(user_name, user_id, videoid):
    buttons = [
        [
            InlineKeyboardButton(
                text=f"Group's Playlist",
                callback_data=f"show_genre {user_id}|Group|{videoid}",
            ),
            InlineKeyboardButton(
                text=f"{user_name[:8]}'s Playlist",
                callback_data=f"show_genre {user_id}|Personal|{videoid}",
            ),
        ],
        [InlineKeyboardButton(text="🗑 Close Menu", callback_data="close")],
    ]
    return buttons


def play_genre_playlist(user_id, type, videoid):
    buttons = [
        [
            InlineKeyboardButton(
                text=f"ARRSong",
                callback_data=f"play_playlist {user_id}|{type}|ARRSong",
            ),
            InlineKeyboardButton(
                text=f"LoveSong",
                callback_data=f"play_playlist {user_id}|{type}|LoveSong",
            ),
        ],
        [
            InlineKeyboardButton(
                text=f"NewSong",
                callback_data=f"play_playlist {user_id}|{type}|NewSong",
            ),
            InlineKeyboardButton(
                text=f"90sSong",
                callback_data=f"play_playlist {user_id}|{type}|90sSong",
            ),
        ],
        [
            InlineKeyboardButton(
                text=f"SadSong",
                callback_data=f"play_playlist {user_id}|{type}|SadSong",
            ),
            InlineKeyboardButton(
                text=f"HitSong",
                callback_data=f"play_playlist {user_id}|{type}|HitSong",
            ),
        ],
        [
            InlineKeyboardButton(
                text=f"MelodySong",
                callback_data=f"play_playlist {user_id}|{type}|MelodySong",
            ),
            InlineKeyboardButton(
                text=f"OtherSong",
                callback_data=f"play_playlist {user_id}|{type}|OtherSong",
            ),
        ],
        [
            InlineKeyboardButton(
                text="⬅️ Go Back",
                callback_data=f"main_playlist {videoid}|{type}|{user_id}",
            ),
            InlineKeyboardButton(text="🗑 Close Menu", callback_data="close"),
        ],
    ]
    return buttons


def add_genre_markup(user_id, type, videoid):
    buttons = [
        [
            InlineKeyboardButton(
                text=f"✚ HitSong",
                callback_data=f"add_playlist {videoid}|{type}|HitSong",
            ),
            InlineKeyboardButton(
                text=f"✚ SadSong",
                callback_data=f"add_playlist {videoid}|{type}|SadSong",
            ),
        ],
        [
            InlineKeyboardButton(
                text=f"✚ NewSong",
                callback_data=f"add_playlist {videoid}|{type}|NewSong",
            ),
            InlineKeyboardButton(
                text=f"✚ 90sSong",
                callback_data=f"add_playlist {videoid}|{type}|90sSong",
            ),
        ],
        [
            InlineKeyboardButton(
                text=f"✚ ARRSong",
                callback_data=f"add_playlist {videoid}|{type}|ARRSong",
            ),
            InlineKeyboardButton(
                text=f"✚ LoveSong",
                callback_data=f"add_playlist {videoid}|{type}|LoveSong",
            ),
        ],
        [
            InlineKeyboardButton(
                text=f"✚ MelodySong",
                callback_data=f"add_playlist {videoid}|{type}|MelodySong",
            ),
            InlineKeyboardButton(
                text=f"✚ OtherSong",
                callback_data=f"add_playlist {videoid}|{type}|OtherSong",
            ),
        ],
        [
            InlineKeyboardButton(
                text="⬅️ Go Back", callback_data=f"goback {videoid}|{user_id}"
            ),
            InlineKeyboardButton(text="🗑 Close Menu", callback_data="close"),
        ],
    ]
    return buttons


def check_genre_markup(type, videoid, user_id):
    buttons = [
        [
            InlineKeyboardButton(
                text=f"HitSong", callback_data=f"check_playlist {type}|HitSong"
            ),
            InlineKeyboardButton(
                text=f"SadSong", callback_data=f"check_playlist {type}|SadSong"
            ),
        ],
        [
            InlineKeyboardButton(
                text=f"NewSong", callback_data=f"check_playlist {type}|NewSong"
            ),
            InlineKeyboardButton(
                text=f"90sSong", callback_data=f"check_playlist {type}|90sSong"
            ),
        ],
        [
            InlineKeyboardButton(
                text=f"ARRSong",
                callback_data=f"check_playlist {type}|ARRSong",
            ),
            InlineKeyboardButton(
                text=f"LoveSong",
                callback_data=f"check_playlist {type}|LoveSong",
            ),
        ],
        [
            InlineKeyboardButton(
                text=f"MelodySong",
                callback_data=f"check_playlist {type}|MelodySong",
            ),
            InlineKeyboardButton(
                text=f"OtherSong", callback_data=f"check_playlist {type}|OtherSong"
            ),
        ],
        [InlineKeyboardButton(text="🗑 Close Menu", callback_data="close")],
    ]
    return buttons


def third_playlist_markup(user_name, user_id, third_name, userid, videoid):
    buttons = [
        [
            InlineKeyboardButton(
                text=f"Group's Playlist",
                callback_data=f"show_genre {user_id}|Group|{videoid}",
            ),
            InlineKeyboardButton(
                text=f"{user_name[:8]}'s Playlist",
                callback_data=f"show_genre {user_id}|Personal|{videoid}",
            ),
        ],
        [
            InlineKeyboardButton(
                text=f"{third_name[:16]}'s Playlist",
                callback_data=f"show_genre {userid}|third|{videoid}",
            ),
        ],
        [InlineKeyboardButton(text="🗑 Close", callback_data="close")],
    ]
    return buttons


def paste_queue_markup(url):
    buttons = [
        [
            InlineKeyboardButton(text="▶️", callback_data=f"resumecb"),
            InlineKeyboardButton(text="⏸️", callback_data=f"pausecb"),
            InlineKeyboardButton(text="⏭️", callback_data=f"skipcb"),
            InlineKeyboardButton(text="⏹️", callback_data=f"stopcb"),
        ],
        [InlineKeyboardButton(text="Checkout Queued Playlist", url=f"{url}")],
        [InlineKeyboardButton(text="🗑 Close Menu", callback_data=f"close")],
    ]
    return buttons


def fetch_playlist(user_name, type, genre, user_id, url):
    buttons = [
        [
            InlineKeyboardButton(
                text=f"Play {user_name[:10]}'s {genre} Playlist",
                callback_data=f"play_playlist {user_id}|{type}|{genre}",
            ),
        ],
        [InlineKeyboardButton(text="Checkout Playlist", url=f"{url}")],
        [InlineKeyboardButton(text="🗑 Close Menu", callback_data=f"close")],
    ]
    return buttons


def delete_playlist_markuup(type, genre):
    buttons = [
        [
            InlineKeyboardButton(
                text=f"Yes! Delete",
                callback_data=f"delete_playlist {type}|{genre}",
            ),
            InlineKeyboardButton(text="No!", callback_data=f"close"),
        ],
    ]
    return buttons
