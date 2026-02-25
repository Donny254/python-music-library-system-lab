class Song:
    
    count = 0
    genres = []
    artists = []
    genre_count = {}
    artists_count = {}
    
    def __init__(self,name,artist,genre):
        self.name = name
        self.artist = artist
        self.genre = genre
        
        
        
        # Each class method is triggered upon a new song being created
        Song.add_song_to_count()
        Song.add_to_genres(genre)
        Song.add_to_artists(artist)
        Song.add_to_genre_count(genre)
        Song.add_to_artist_count(artist)


    @classmethod
    def add_song_to_count(cls):
        """Increments the total song count by 1."""
        cls.count += 1

    # @classmethod
    def add_to_genres(cls, genre):
        """Adds a genre to the genres list only if it doesn't already exist (no duplicates)."""
        if genre not in cls.genres:
            cls.genres.append(genre)

    # @classmethod
    def add_to_artists(cls, artist):
        """Adds an artist to the artists list only if they don't already exist (no duplicates)."""
        if artist not in cls.artists:
            cls.artists.append(artist)

    # @classmethod
    def add_to_genre_count(cls, genre):
        """
        Updates genre_count dictionary:
        - If the genre already exists, increment its count by 1.
        - If the genre doesn't exist yet, add it and set its count to 1.
        """
        if genre in cls.genre_count:
            cls.genre_count[genre] += 1
        else:
            cls.genre_count[genre] = 1

    # @classmethod
    def add_to_artist_count(cls, artist):
        """
        Updates artist_count dictionary:
        - If the artist already exists, increment their count by 1.
        - If the artist doesn't exist yet, add them and set their count to 1.
        """
        if artist in cls.artist_count:
            cls.artist_count[artist] += 1
        else:
            cls.artist_count[artist] = 1

    
