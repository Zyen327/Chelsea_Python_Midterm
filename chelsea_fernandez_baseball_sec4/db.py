import sqlite3
import os

DB_NAME = os.path.join(os.path.dirname(__file__), "baseball.db")

def get_connection():
    return sqlite3.connect(DB_NAME)

def get_player(player_id):
    with get_connection() as conn:
        cur = conn.cursor()
        cur.execute("SELECT * FROM Player WHERE playerID = ?", (player_id,))
        return cur.fetchone()


def update_player(player_id, first, last, pos, at_bats, hits):
    with get_connection() as conn:
        cur = conn.cursor()
        cur.execute("""
            UPDATE Player
            SET firstName = ?, lastName = ?, position = ?, atBats = ?, hits = ?
            WHERE playerID = ?
        """, (first, last, pos, at_bats, hits, player_id))
        conn.commit()