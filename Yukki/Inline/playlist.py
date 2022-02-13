from pyrogram.types import (CallbackQuery, InlineKeyboardButton,
                            InlineKeyboardMarkup, InputMediaPhoto, Message)


def check_markup(user_name, user_id, videoid):
    return [
        [
            InlineKeyboardButton(
                text="Group's Playlist",
                callback_data=f"playlist_check {user_id}|Group|{videoid}",
            ),
            InlineKeyboardButton(
                text=f"{user_name[:8]}'s Playlist",
                callback_data=f"playlist_check {user_id}|Personal|{videoid}",
            ),
        ],
        [InlineKeyboardButton(text="🗑 Close Menu", callback_data="close")],
    ]


def playlist_markup(user_name, user_id, videoid):
    return [
        [
            InlineKeyboardButton(
                text="Group's Playlist",
                callback_data=f"show_genre {user_id}|Group|{videoid}",
            ),
            InlineKeyboardButton(
                text=f"{user_name[:8]}'s Playlist",
                callback_data=f"show_genre {user_id}|Personal|{videoid}",
            ),
        ],
        [InlineKeyboardButton(text="🗑 Close Menu", callback_data="close")],
    ]


def play_genre_playlist(user_id, type, videoid):
    return [
        [
            InlineKeyboardButton(
                text='ARRSong',
                callback_data=f"play_playlist {user_id}|{type}|ARRSong",
            ),
            InlineKeyboardButton(
                text='LoveSong',
                callback_data=f"play_playlist {user_id}|{type}|LoveSong",
            ),
        ],
        [
            InlineKeyboardButton(
                text='NewSong',
                callback_data=f"play_playlist {user_id}|{type}|NewSong",
            ),
            InlineKeyboardButton(
                text='90sSong',
                callback_data=f"play_playlist {user_id}|{type}|90sSong",
            ),
        ],
        [
            InlineKeyboardButton(
                text='SadSong',
                callback_data=f"play_playlist {user_id}|{type}|SadSong",
            ),
            InlineKeyboardButton(
                text='HitSong',
                callback_data=f"play_playlist {user_id}|{type}|HitSong",
            ),
        ],
        [
            InlineKeyboardButton(
                text='MelodySong',
                callback_data=f"play_playlist {user_id}|{type}|MelodySong",
            ),
            InlineKeyboardButton(
                text='OtherSong',
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


def add_genre_markup(user_id, type, videoid):
    return [
        [
            InlineKeyboardButton(
                text='✚ HitSong',
                callback_data=f"add_playlist {videoid}|{type}|HitSong",
            ),
            InlineKeyboardButton(
                text='✚ SadSong',
                callback_data=f"add_playlist {videoid}|{type}|SadSong",
            ),
        ],
        [
            InlineKeyboardButton(
                text='✚ NewSong',
                callback_data=f"add_playlist {videoid}|{type}|NewSong",
            ),
            InlineKeyboardButton(
                text='✚ 90sSong',
                callback_data=f"add_playlist {videoid}|{type}|90sSong",
            ),
        ],
        [
            InlineKeyboardButton(
                text='✚ ARRSong',
                callback_data=f"add_playlist {videoid}|{type}|ARRSong",
            ),
            InlineKeyboardButton(
                text='✚ LoveSong',
                callback_data=f"add_playlist {videoid}|{type}|LoveSong",
            ),
        ],
        [
            InlineKeyboardButton(
                text='✚ MelodySong',
                callback_data=f"add_playlist {videoid}|{type}|MelodySong",
            ),
            InlineKeyboardButton(
                text='✚ OtherSong',
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


def check_genre_markup(type, videoid, user_id):
    return [
        [
            InlineKeyboardButton(
                text='HitSong', callback_data=f"check_playlist {type}|HitSong"
            ),
            InlineKeyboardButton(
                text='SadSong', callback_data=f"check_playlist {type}|SadSong"
            ),
        ],
        [
            InlineKeyboardButton(
                text='NewSong', callback_data=f"check_playlist {type}|NewSong"
            ),
            InlineKeyboardButton(
                text='90sSong', callback_data=f"check_playlist {type}|90sSong"
            ),
        ],
        [
            InlineKeyboardButton(
                text='ARRSong', callback_data=f"check_playlist {type}|ARRSong"
            ),
            InlineKeyboardButton(
                text='LoveSong',
                callback_data=f"check_playlist {type}|LoveSong",
            ),
        ],
        [
            InlineKeyboardButton(
                text='MelodySong',
                callback_data=f"check_playlist {type}|MelodySong",
            ),
            InlineKeyboardButton(
                text='OtherSong',
                callback_data=f"check_playlist {type}|OtherSong",
            ),
        ],
        [InlineKeyboardButton(text="🗑 Close Menu", callback_data="close")],
    ]


def third_playlist_markup(user_name, user_id, third_name, userid, videoid):
    return [
        [
            InlineKeyboardButton(
                text="Group's Playlist",
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


def paste_queue_markup(url):
    return [
        [
            InlineKeyboardButton(text="▶️", callback_data='resumecb'),
            InlineKeyboardButton(text="⏸️", callback_data='pausecb'),
            InlineKeyboardButton(text="⏭️", callback_data='skipcb'),
            InlineKeyboardButton(text="⏹️", callback_data='stopcb'),
        ],
        [InlineKeyboardButton(text="Checkout Queued Playlist", url=f"{url}")],
        [InlineKeyboardButton(text="🗑 Close Menu", callback_data='close')],
    ]


def fetch_playlist(user_name, type, genre, user_id, url):
    return [
        [
            InlineKeyboardButton(
                text=f"Play {user_name[:10]}'s {genre} Playlist",
                callback_data=f"play_playlist {user_id}|{type}|{genre}",
            ),
        ],
        [InlineKeyboardButton(text="Checkout Playlist", url=f"{url}")],
        [InlineKeyboardButton(text="🗑 Close Menu", callback_data='close')],
    ]


def delete_playlist_markuup(type, genre):
    return [
        [
            InlineKeyboardButton(
                text='Yes! Delete',
                callback_data=f"delete_playlist {type}|{genre}",
            ),
            InlineKeyboardButton(text="No!", callback_data='close'),
        ]
    ]
