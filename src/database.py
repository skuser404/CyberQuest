"""
Database module for CyberQuest
Handles SQLite database operations for user scores and leaderboard
"""

import sqlite3
import os
from datetime import datetime
from contextlib import contextmanager

# Database file path
DB_PATH = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data', 'cyberquest.db')


@contextmanager
def get_db_connection():
    """Context manager for database connections"""
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    try:
        yield conn
        conn.commit()
    except Exception as e:
        conn.rollback()
        raise e
    finally:
        conn.close()


def init_database():
    """Initialize the database with required tables"""
    with get_db_connection() as conn:
        cursor = conn.cursor()
        
        # Create players table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS players (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT NOT NULL UNIQUE,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        
        # Create scores table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS scores (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                player_id INTEGER NOT NULL,
                level TEXT NOT NULL,
                score INTEGER NOT NULL,
                max_score INTEGER NOT NULL,
                percentage REAL NOT NULL,
                risk_level TEXT NOT NULL,
                played_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (player_id) REFERENCES players (id)
            )
        ''')
        
        # Create question_attempts table for detailed analytics
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS question_attempts (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                player_id INTEGER NOT NULL,
                question_id INTEGER NOT NULL,
                level TEXT NOT NULL,
                correct BOOLEAN NOT NULL,
                attempted_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (player_id) REFERENCES players (id)
            )
        ''')
        
        print("✅ Database initialized successfully!")


def create_or_get_player(username):
    """Create a new player or get existing player ID"""
    if not username or len(username.strip()) == 0:
        raise ValueError("Username cannot be empty")
    
    username = username.strip()[:50]  # Limit username length
    
    with get_db_connection() as conn:
        cursor = conn.cursor()
        
        # Try to get existing player
        cursor.execute('SELECT id FROM players WHERE username = ?', (username,))
        player = cursor.fetchone()
        
        if player:
            return player['id']
        
        # Create new player
        cursor.execute('INSERT INTO players (username) VALUES (?)', (username,))
        return cursor.lastrowid


def save_score(player_id, level, score, max_score, percentage, risk_level):
    """Save a game score to the database"""
    with get_db_connection() as conn:
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO scores (player_id, level, score, max_score, percentage, risk_level)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', (player_id, level, score, max_score, percentage, risk_level))
        return cursor.lastrowid


def save_question_attempt(player_id, question_id, level, correct):
    """Save individual question attempt for analytics"""
    with get_db_connection() as conn:
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO question_attempts (player_id, question_id, level, correct)
            VALUES (?, ?, ?, ?)
        ''', (player_id, question_id, level, correct))


def get_leaderboard(limit=10):
    """Get top players by their best scores"""
    with get_db_connection() as conn:
        cursor = conn.cursor()
        cursor.execute('''
            SELECT 
                p.username,
                s.level,
                s.score,
                s.max_score,
                s.percentage,
                s.risk_level,
                s.played_at
            FROM scores s
            JOIN players p ON s.player_id = p.id
            ORDER BY s.score DESC, s.played_at DESC
            LIMIT ?
        ''', (limit,))
        
        results = cursor.fetchall()
        return [dict(row) for row in results]


def get_player_stats(player_id):
    """Get statistics for a specific player"""
    with get_db_connection() as conn:
        cursor = conn.cursor()
        
        # Get total games played
        cursor.execute('SELECT COUNT(*) as total_games FROM scores WHERE player_id = ?', (player_id,))
        total_games = cursor.fetchone()['total_games']
        
        # Get best score
        cursor.execute('''
            SELECT score, max_score, percentage, level, risk_level 
            FROM scores 
            WHERE player_id = ? 
            ORDER BY score DESC 
            LIMIT 1
        ''', (player_id,))
        best_score = cursor.fetchone()
        
        # Get average score
        cursor.execute('SELECT AVG(percentage) as avg_percentage FROM scores WHERE player_id = ?', (player_id,))
        avg_percentage = cursor.fetchone()['avg_percentage']
        
        return {
            'total_games': total_games,
            'best_score': dict(best_score) if best_score else None,
            'avg_percentage': round(avg_percentage, 2) if avg_percentage else 0
        }


def get_category_performance(player_id):
    """Get performance breakdown by category"""
    with get_db_connection() as conn:
        cursor = conn.cursor()
        cursor.execute('''
            SELECT 
                level,
                COUNT(*) as total_attempts,
                SUM(CASE WHEN correct = 1 THEN 1 ELSE 0 END) as correct_answers
            FROM question_attempts
            WHERE player_id = ?
            GROUP BY level
        ''', (player_id,))
        
        results = cursor.fetchall()
        return [dict(row) for row in results]


# Initialize database when module is imported
if __name__ == '__main__':
    init_database()
    print("Database setup complete!")
