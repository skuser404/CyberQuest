"""
Utility functions for CyberQuest
Helper functions for validation, formatting, and security
"""

import re
from datetime import datetime
import hashlib


def validate_username(username):
    """
    Validate username according to security rules
    
    Args:
        username: String to validate
    
    Returns:
        tuple: (is_valid, error_message)
    """
    if not username or len(username.strip()) == 0:
        return False, "Username cannot be empty"
    
    username = username.strip()
    
    if len(username) < 3:
        return False, "Username must be at least 3 characters long"
    
    if len(username) > 50:
        return False, "Username must be less than 50 characters"
    
    # Allow alphanumeric, underscore, and hyphen
    if not re.match(r'^[a-zA-Z0-9_-]+$', username):
        return False, "Username can only contain letters, numbers, underscores, and hyphens"
    
    # Prevent SQL injection patterns (extra safety)
    dangerous_patterns = ['--', ';', 'DROP', 'SELECT', 'INSERT', 'DELETE', 'UPDATE']
    username_upper = username.upper()
    
    for pattern in dangerous_patterns:
        if pattern in username_upper:
            return False, "Username contains invalid characters"
    
    return True, ""


def sanitize_input(text, max_length=1000):
    """
    Sanitize user input to prevent XSS and injection attacks
    
    Args:
        text: Input text to sanitize
        max_length: Maximum allowed length
    
    Returns:
        str: Sanitized text
    """
    if not text:
        return ""
    
    # Convert to string and strip whitespace
    text = str(text).strip()
    
    # Limit length
    text = text[:max_length]
    
    # Remove dangerous characters for XSS prevention
    # Note: Flask's Jinja2 auto-escapes by default, but this is extra safety
    text = text.replace('<', '&lt;').replace('>', '&gt;')
    
    return text


def format_datetime(dt):
    """
    Format datetime for display
    
    Args:
        dt: datetime object or string
    
    Returns:
        str: Formatted datetime string
    """
    if isinstance(dt, str):
        try:
            dt = datetime.fromisoformat(dt.replace('Z', '+00:00'))
        except:
            return dt
    
    if isinstance(dt, datetime):
        return dt.strftime("%Y-%m-%d %H:%M:%S")
    
    return str(dt)


def calculate_percentage(score, max_score):
    """
    Calculate percentage score
    
    Args:
        score: Points earned
        max_score: Maximum possible points
    
    Returns:
        float: Percentage rounded to 2 decimal places
    """
    if max_score == 0:
        return 0.0
    
    return round((score / max_score) * 100, 2)


def generate_session_id(username):
    """
    Generate a unique session ID for a player
    
    Args:
        username: Player username
    
    Returns:
        str: Unique session identifier
    """
    timestamp = datetime.now().isoformat()
    data = f"{username}_{timestamp}"
    return hashlib.sha256(data.encode()).hexdigest()[:16]


def format_score_display(score, max_score):
    """
    Format score for display with percentage
    
    Args:
        score: Points earned
        max_score: Maximum possible points
    
    Returns:
        str: Formatted score string
    """
    percentage = calculate_percentage(score, max_score)
    return f"{score}/{max_score} ({percentage}%)"


def get_color_for_percentage(percentage):
    """
    Get color code based on performance percentage
    
    Args:
        percentage: Score percentage
    
    Returns:
        str: Hex color code
    """
    if percentage >= 90:
        return "#10b981"  # Green
    elif percentage >= 75:
        return "#3b82f6"  # Blue
    elif percentage >= 60:
        return "#f59e0b"  # Yellow
    elif percentage >= 40:
        return "#f97316"  # Orange
    else:
        return "#ef4444"  # Red


def get_emoji_for_category(category):
    """
    Get emoji representation for question category
    
    Args:
        category: Question category
    
    Returns:
        str: Emoji character
    """
    emoji_map = {
        "Phishing Detection": "🎣",
        "Password Security": "🔑",
        "Safe Browsing": "🌐",
        "Social Engineering": "🎭",
        "Malware Awareness": "🦠",
        "Two-Factor Authentication": "🔐",
        "Encryption Basics": "🔒",
        "Advanced Threats": "⚠️",
        "Data Privacy": "🛡️",
        "Incident Response": "🚨"
    }
    
    return emoji_map.get(category, "📝")


def is_valid_level(level):
    """
    Check if level is valid
    
    Args:
        level: Level string
    
    Returns:
        bool: True if valid level
    """
    valid_levels = ['beginner', 'intermediate', 'advanced']
    return level in valid_levels


def get_difficulty_emoji(level):
    """
    Get emoji for difficulty level
    
    Args:
        level: Difficulty level
    
    Returns:
        str: Emoji character
    """
    emoji_map = {
        'beginner': '🌱',
        'intermediate': '🔥',
        'advanced': '🚀'
    }
    return emoji_map.get(level, '❓')


if __name__ == '__main__':
    # Test utilities
    print("Testing utility functions...")
    
    # Test username validation
    test_usernames = ['john_doe', 'a', 'valid-user123', 'invalid@user', 'DROP TABLE']
    print("\n🔍 Username validation:")
    for username in test_usernames:
        valid, msg = validate_username(username)
        status = "✅" if valid else "❌"
        print(f"  {status} '{username}': {msg if not valid else 'Valid'}")
    
    # Test percentage calculation
    print("\n📊 Percentage calculation:")
    print(f"  50/100 = {calculate_percentage(50, 100)}%")
    print(f"  15/20 = {calculate_percentage(15, 20)}%")
    
    # Test color assignment
    print("\n🎨 Color for percentages:")
    for pct in [95, 80, 65, 45, 30]:
        print(f"  {pct}% → {get_color_for_percentage(pct)}")
