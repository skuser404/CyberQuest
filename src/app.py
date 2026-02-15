"""
CyberQuest: Cybersecurity Awareness Game for Beginners
Main Flask Application
"""

from flask import Flask, render_template, request, jsonify, session, redirect, url_for
import os
import json
from datetime import timedelta

# Import our modules
from database import init_database, create_or_get_player, save_score, save_question_attempt, get_leaderboard, get_player_stats
from questions import get_questions_by_level, get_question_count_by_level, get_all_categories
from game_logic import calculate_risk_level, get_level_metadata, calculate_category_stats, generate_feedback, get_learning_resources, get_improvement_suggestions
from utils import validate_username, sanitize_input, format_score_display, get_color_for_percentage, is_valid_level

# Initialize Flask app with correct paths
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
app = Flask(__name__, 
            template_folder=os.path.join(BASE_DIR, 'templates'),
            static_folder=os.path.join(BASE_DIR, 'static'))
app.secret_key = os.urandom(24)  # Generate random secret key for sessions
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(hours=2)

# Initialize database on startup
init_database()


@app.route('/')
def index():
    """Home page - game introduction and level selection"""
    level_metadata = get_level_metadata()
    question_counts = get_question_count_by_level()
    
    return render_template('index.html', 
                         levels=level_metadata,
                         question_counts=question_counts)


@app.route('/start', methods=['POST'])
def start_game():
    """Start a new game session"""
    data = request.get_json()
    
    # Validate username
    username = data.get('username', '').strip()
    is_valid, error_msg = validate_username(username)
    
    if not is_valid:
        return jsonify({'success': False, 'error': error_msg}), 400
    
    # Validate level
    level = data.get('level', '').lower()
    if not is_valid_level(level):
        return jsonify({'success': False, 'error': 'Invalid difficulty level'}), 400
    
    # Create or get player
    try:
        player_id = create_or_get_player(username)
        
        # Store in session
        session['player_id'] = player_id
        session['username'] = username
        session['level'] = level
        session.permanent = True
        
        return jsonify({
            'success': True,
            'redirect': url_for('play_game', level=level)
        })
    
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500


@app.route('/play/<level>')
def play_game(level):
    """Game play page for specified level"""
    # Check if user has started a game
    if 'player_id' not in session:
        return redirect(url_for('index'))
    
    if not is_valid_level(level):
        return redirect(url_for('index'))
    
    # Get questions for this level
    questions = get_questions_by_level(level)
    
    if not questions:
        return "No questions available for this level", 404
    
    level_metadata = get_level_metadata()
    
    return render_template('level.html',
                         level=level,
                         level_info=level_metadata[level],
                         questions=questions,
                         username=session.get('username'))


@app.route('/submit', methods=['POST'])
def submit_answers():
    """Submit answers and calculate results"""
    if 'player_id' not in session:
        return jsonify({'success': False, 'error': 'No active session'}), 401
    
    data = request.get_json()
    level = data.get('level')
    answers = data.get('answers', {})  # {question_id: selected_option}
    
    if not is_valid_level(level):
        return jsonify({'success': False, 'error': 'Invalid level'}), 400
    
    # Get questions for validation
    questions = get_questions_by_level(level)
    
    # Calculate score
    score = 0
    max_score = 0
    
    for question in questions:
        question_id = str(question['id'])
        max_score += question.get('points', 10)
        
        user_answer = answers.get(question_id)
        correct_answer = question['correct']
        is_correct = user_answer == correct_answer
        
        if is_correct:
            score += question.get('points', 10)
        
        # Save individual question attempt
        save_question_attempt(
            session['player_id'],
            question['id'],
            level,
            is_correct
        )
    
    # Calculate percentage and risk level
    percentage = round((score / max_score) * 100, 2) if max_score > 0 else 0
    risk_level, risk_description, risk_emoji, risk_color = calculate_risk_level(score, max_score)
    
    # Save score to database
    score_id = save_score(
        session['player_id'],
        level,
        score,
        max_score,
        percentage,
        risk_level
    )
    
    # Calculate category statistics
    category_stats = calculate_category_stats(questions, answers)
    
    # Generate detailed feedback
    feedback = generate_feedback(questions, answers)
    
    # Get improvement suggestions
    suggestions = get_improvement_suggestions(category_stats)
    
    # Store results in session for results page
    session['last_result'] = {
        'score_id': score_id,
        'level': level,
        'score': score,
        'max_score': max_score,
        'percentage': percentage,
        'risk_level': risk_level,
        'risk_description': risk_description,
        'risk_emoji': risk_emoji,
        'risk_color': risk_color,
        'category_stats': category_stats,
        'feedback': feedback,
        'suggestions': suggestions
    }
    
    return jsonify({
        'success': True,
        'redirect': url_for('show_results')
    })


@app.route('/results')
def show_results():
    """Display game results with detailed feedback"""
    if 'last_result' not in session:
        return redirect(url_for('index'))
    
    result = session['last_result']
    learning_resources = get_learning_resources()
    
    return render_template('result.html',
                         result=result,
                         username=session.get('username'),
                         learning_resources=learning_resources)


@app.route('/leaderboard')
def leaderboard():
    """Display top scores leaderboard"""
    top_scores = get_leaderboard(limit=10)
    
    return render_template('leaderboard.html',
                         scores=top_scores,
                         username=session.get('username'))


@app.route('/api/player/stats')
def player_stats():
    """API endpoint for player statistics"""
    if 'player_id' not in session:
        return jsonify({'error': 'Not authenticated'}), 401
    
    try:
        stats = get_player_stats(session['player_id'])
        return jsonify(stats)
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/api/categories')
def get_categories():
    """API endpoint for all question categories"""
    categories = get_all_categories()
    return jsonify(categories)


@app.route('/reset')
def reset_session():
    """Reset game session"""
    session.clear()
    return redirect(url_for('index'))


@app.errorhandler(404)
def not_found(e):
    """Custom 404 error page"""
    return render_template('index.html'), 404


@app.errorhandler(500)
def server_error(e):
    """Custom 500 error page"""
    return "Internal Server Error - Please try again later", 500


# Development server configuration
if __name__ == '__main__':
    print("🚀 Starting CyberQuest...")
    print("📚 Initializing database...")
    init_database()
    print("✅ Ready! Visit http://localhost:5000")
    
    # Run with debug mode for development
    app.run(host='0.0.0.0', port=5000, debug=True)
