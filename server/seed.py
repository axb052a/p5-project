#!/usr/bin/env python3
import bcrypt
from models import User
# Standard library imports
from random import choice as rc

# Remote library imports
from faker import Faker

# Local imports
from app import app
from models import *

if __name__ == '__main__':
    fake = Faker()
    with app.app_context():
    
        db.drop_all()
        db.create_all()
        
     # Seed for Users
        
        user_list = [
            {"username": "Jane", "email": "janedoe@example.com", "password": "password1"},
            {"username": "Joe", "email": "joecena@example.com", "password": "password2"},
            {"username": "Alice", "email": "alice@example.com", "password": "password3"},
            {"username": "Bob", "email": "bobsmith@example.com", "password": "password4"},
            {"username": "Charlie", "email": "charliebrown@example.com", "password": "password5"},
            {"username": "David", "email": "davidmiller@example.com", "password": "password6"},
            {"username": "Eva", "email": "evaanderson@example.com", "password": "password7"},
        ]

        for user_data in user_list:
            user = User(username=user_data["username"], email=user_data["email"])

            # Hash the password using bcrypt
            password = user_data["password"].encode("utf-8")
            password_hash = bcrypt.generate_password_hash(password).decode('utf-8')

            user._password_hash = password_hash
            db.session.add(user)

        # Commit the changes
        db.session.commit()
        print("Users seeded successfully.")
    
        # Seed for Musics

        music_list = [
            {"title": "About You", "artist": "The 1975", "image": "https://razzmag.files.wordpress.com/2022/12/e3ee1ee6-fec2-42e4-860d-159d428aa108.jpeg?w=992&h=558&crop=1"},
            {"title": "Days", "artist": "The Drums", "image": "https://i.scdn.co/image/ab67616d0000b2734c27d14a19e67dac23661031"},
            {"title": "Anti-Hero", "artist": "Taylor Swift", "image": "https://i.scdn.co/image/ab67616d0000b273bb54dde68cd23e2a268ae0f5"},
            {"title": "Dreaming", "artist": "Smallpools", "image": "https://i.scdn.co/image/ab67616d0000b27324c80190d731ccaa74415049"},
            {"title": "Electric Feel", "artist": "MGMT", "image": "https://i.scdn.co/image/ab67616d0000b27360c4c3d695931aeb83bce500"},
            {"title": "Heartbeat", "artist": "Childish Gambino", "image": "https://i.scdn.co/image/ab67616d0000b273ddd59d8bd5982e6d250d9a22"},
            {"title": "Under the Bridge", "artist": "Red Hot Chili Peppers", "image": "https://i.scdn.co/image/ab67616d0000b273153d79816d853f2694b2cc70"},
            {"title": "Midnight City", "artist": "M83", "image": "https://i.scdn.co/image/ab67616d0000b273fff2cb485c36a6d8f639bdba"},
            {"title": "Dog Days Are Over", "artist": "Florence + The Machine", "image": "https://i.scdn.co/image/ab67616d0000b2730672b0f8756ae2af86e8a5ce"},
            {"title": "Sweater Weather", "artist": "The Neighbourhood", "image": "https://i.scdn.co/image/ab67616d0000b2738265a736a1eb838ad5a0b921"},
            {"title": "Take a Walk", "artist": "Passion Pit", "image": "https://i.scdn.co/image/ab67616d0000b273f860547bc8ba0c59df4fe2c3"},
            {"title": "Shut Up and Dance", "artist": "WALK THE MOON", "image": "https://i.scdn.co/image/ab67616d0000b27343294cfa2688055c9d821bf3"},
            {"title": "Ho Hey", "artist": "The Lumineers", "image": "https://i.scdn.co/image/ab67616d0000b273b23ded2daf5be916f9759077"},
            {"title": "Walking on a Dream", "artist": "Empire of the Sun", "image": "https://i.scdn.co/image/ab67616d0000b273cba2ced72e7bca015df64dcc"},
            {"title": "I Will Wait", "artist": "Mumford & Sons", "image": "https://i.scdn.co/image/ab67616d0000b27383f859512262378f2aa50a22"},
            {"title": "Ocean Eyes", "artist": "Billie Eilish", "image": "https://i.scdn.co/image/ab67616d0000b273a9f6c04ba168640b48aa5795"},
            {"title": "Some Nights", "artist": "fun.", "image": "https://i.scdn.co/image/ab67616d0000b273e89e0d90d786d37fb6d5d84f"},
            {"title": "Stressed Out", "artist": "Twenty One Pilots", "image": "https://i.scdn.co/image/ab67616d0000b273de03bfc2991fd5bcfde65ba3"},
        ]

        musics = [Music(
            title=music["title"],
            artist=music["artist"],
            image=music["image"])
          for music in music_list]
        db.session.add_all(musics)
        db.session.commit()
        print("Musics seeded successfully.")

        # Seed for Genres

        genre_list = [
            {"name": "R&B", "musics": [6], "image": "https://i.pinimg.com/originals/b7/54/6b/b7546bca6cbf4fe7f474d213bb9c6a28.jpg"},
            {"name": "Indie Rock", "musics": [2, 4, 5, 7, 13, 14, 15, 17], "image": "https://i.pinimg.com/564x/70/bf/ec/70bfec9fc7ccc14d2412b0f99dbbbd53.jpg"},
            {"name": "Mainstream Pop", "musics": [1, 3, 12, 16, 17], "image": "https://i.pinimg.com/736x/5b/e7/3d/5be73dafdf15eb39a98eabb12eaf6c79.jpg"},
            {"name": "Electronic", "musics": [3, 5, 14], "image": "https://edm.com/.image/ar_1:1%2Cc_fill%2Ccs_srgb%2Cfl_progressive%2Cq_auto:good%2Cw_1200/MTUzMTcwODc2NzA2MDcxNTU5/festival-image.jpg"},
            {"name": "Hip Hop", "musics": [6], "image": "https://img.freepik.com/premium-vector/hip-hop-tag-graffiti-style-label-lettering_204219-49.jpg?w=2000"},
            {"name": "Alternative", "musics": [5, 8, 9, 10, 11, 18], "image": "https://cdn.pnghd.pics/data/667/indie-tumblr-24.png"},
            {"name": "Country", "musics": [15], "image": "https://i.pinimg.com/736x/3a/52/42/3a524276efcbd286f289ec2f8034b355.jpg"},
            {"name": "Jazz", "musics": [8], "image": "https://media.istockphoto.com/id/607972154/vector/jazz-instruments.jpg?s=612x612&w=0&k=20&c=s8G_EkJqjU-rRn--GXSicTUj3n9nzZuPNv9MtM1u4kc="},
        ]
        
        for genre_data in genre_list:
            genre = Genre(
                name=genre_data["name"],
                image=genre_data["image"]
            )

            # Add musics to the genre
            music_ids = genre_data.get("musics", [])
            genre_musics = Music.query.filter(Music.id.in_(music_ids)).all()

            genre.musics = genre_musics

            db.session.add(genre)
            db.session.commit()

        print("Genres seeded successfully.")
        
        # Seed for Playlists

        playlist_list = [
            {"name": "Nostalgia", "musics": [1, 2, 3], "image": "https://i.pinimg.com/originals/6b/77/6d/6b776d376dcf508ac7249c8309c02999.jpg"}, 
            {"name": "In My Feels", "musics": [4, 5, 6], "image": "https://pm1.aminoapps.com/6696/592909d0be489390a30e8e2544ca86d53dbc7753_hq.jpg"},
            {"name": "Road Trip", "musics": [7, 8, 9], "image": "https://i.ytimg.com/vi/O4N4MMIfnW0/maxresdefault.jpg"},
            {"name": "Chill Vibes", "musics": [10, 11, 12], "image": "https://i.pinimg.com/564x/f5/31/be/f531be33d92a1431d5b274e65eae3a52.jpg"},
            {"name": "Workout Beats", "musics": [13, 14, 15], "image": "https://i.pinimg.com/originals/e4/a7/20/e4a7206b019cc7b43b1522f39afded6a.png"},
            {"name": "Study Session", "musics": [16, 17, 18], "image": "https://i.pinimg.com/564x/c9/83/7a/c9837afb7fed53871e45422d4266492e.jpg"},  
        ]

        for playlist_data in playlist_list:
            playlist = Playlist(
                name=playlist_data["name"],
                image=playlist_data['image'])  

            # Add musics to the playlist
            music_ids = playlist_data.get("musics", [])
            playlist_musics = Music.query.filter(Music.id.in_(music_ids)).all()

            playlist.musics = playlist_musics

            db.session.add(playlist)  # Add the playlist to the session
            db.session.commit()
            print("Playlist seeded successfully.")




