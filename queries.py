"""
queries.py
CIS 3120 MP02 SQL and Database
Author 2 query module

This is the query module from my team project contribution. My original
contribution is documented in PR #29 in the course repository.
"""

import sqlite3


def get_playlist_tracks(conn, playlist_name):
    """Return tracks on a named playlist in playlist order."""
    query = """
        SELECT t.title, a.name AS artist_name, t.duration_seconds, pt.position
        FROM PlaylistTrack pt
        JOIN Track t ON pt.track_id = t.track_id
        JOIN Artist a ON t.artist_id = a.artist_id
        JOIN Playlist p ON pt.playlist_id = p.playlist_id
        WHERE p.playlist_name = ?
        ORDER BY pt.position ASC
    """
    return conn.execute(query, (playlist_name,)).fetchall()


def get_tracks_on_no_playlist(conn):
    """Return tracks that are not assigned to any playlist."""
    query = """
        SELECT t.track_id, t.title, a.name AS artist_name
        FROM Track t
        JOIN Artist a ON t.artist_id = a.artist_id
        LEFT JOIN PlaylistTrack pt ON t.track_id = pt.track_id
        WHERE pt.track_id IS NULL
    """
    return conn.execute(query).fetchall()


def get_most_added_track(conn):
    """Return the track that appears on the greatest number of playlists."""
    query = """
        SELECT t.title, a.name AS artist_name, COUNT(*) AS playlist_count
        FROM PlaylistTrack pt
        JOIN Track t ON pt.track_id = t.track_id
        JOIN Artist a ON t.artist_id = a.artist_id
        GROUP BY pt.track_id, t.title, a.name
        ORDER BY playlist_count DESC
        LIMIT 1
    """
    return conn.execute(query).fetchone()


def get_playlist_durations(conn):
    """Return each playlist and its total duration in minutes, longest first."""
    query = """
        SELECT p.playlist_name, SUM(t.duration_seconds) / 60.0 AS total_minutes
        FROM Playlist p
        JOIN PlaylistTrack pt ON p.playlist_id = pt.playlist_id
        JOIN Track t ON pt.track_id = t.track_id
        GROUP BY p.playlist_id, p.playlist_name
        ORDER BY total_minutes DESC
    """
    return conn.execute(query).fetchall()


if __name__ == "__main__":
    # Standalone smoke test used to verify the four functions independently.
    conn = sqlite3.connect(":memory:")
    conn.execute("PRAGMA foreign_keys = ON;")

    conn.executescript("""
        CREATE TABLE Artist (
            artist_id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            genre TEXT NOT NULL,
            origin_city TEXT
        );
        CREATE TABLE Track (
            track_id INTEGER PRIMARY KEY,
            title TEXT NOT NULL,
            duration_seconds INTEGER NOT NULL,
            artist_id INTEGER NOT NULL REFERENCES Artist(artist_id)
        );
        CREATE TABLE Playlist (
            playlist_id INTEGER PRIMARY KEY,
            playlist_name TEXT NOT NULL,
            owner_name TEXT NOT NULL
        );
        CREATE TABLE PlaylistTrack (
            playlist_id INTEGER NOT NULL REFERENCES Playlist(playlist_id),
            track_id INTEGER NOT NULL REFERENCES Track(track_id),
            position INTEGER NOT NULL,
            PRIMARY KEY (playlist_id, track_id)
        );
    """)

    conn.executemany("INSERT INTO Artist VALUES (?,?,?,?)", [
        (1, "Sample Artist A", "Hip-Hop", "New York"),
        (2, "Sample Artist B", "R&B", "Atlanta"),
    ])
    conn.executemany("INSERT INTO Track VALUES (?,?,?,?)", [
        (1, "Track One", 210, 1),
        (2, "Track Two", 185, 1),
        (3, "Track Three", 240, 2),
        (4, "Track Four", 195, 2),
        (5, "Orphan Track", 170, 1),
    ])
    conn.executemany("INSERT INTO Playlist VALUES (?,?,?)", [
        (1, "Morning Commute", "Student A"),
        (2, "Study Session", "Student B"),
    ])
    conn.executemany("INSERT INTO PlaylistTrack VALUES (?,?,?)", [
        (1, 1, 1), (1, 2, 2), (1, 3, 3),
        (2, 1, 1), (2, 4, 2),
    ])
    conn.commit()

    print(get_playlist_tracks(conn, "Morning Commute"))
    print(get_tracks_on_no_playlist(conn))
    print(get_most_added_track(conn))
    print(get_playlist_durations(conn))
    conn.close()
