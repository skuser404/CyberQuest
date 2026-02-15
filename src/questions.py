"""
Questions module for CyberQuest
Handles loading and managing quiz questions
"""

import json
import os
import random

QUESTIONS_FILE = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data', 'questions.json')


def load_questions():
    """Load all questions from JSON file"""
    try:
        with open(QUESTIONS_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"❌ Error: Questions file not found at {QUESTIONS_FILE}")
        return {"beginner": [], "intermediate": [], "advanced": []}
    except json.JSONDecodeError as e:
        print(f"❌ Error: Invalid JSON in questions file: {e}")
        return {"beginner": [], "intermediate": [], "advanced": []}


def get_questions_by_level(level):
    """
    Get questions for a specific difficulty level
    
    Args:
        level: 'beginner', 'intermediate', or 'advanced'
    
    Returns:
        list: Questions for the specified level
    """
    all_questions = load_questions()
    return all_questions.get(level, [])


def get_random_questions(level, count=5):
    """
    Get random questions from a level
    
    Args:
        level: Difficulty level
        count: Number of questions to return
    
    Returns:
        list: Random selection of questions
    """
    questions = get_questions_by_level(level)
    
    if len(questions) <= count:
        return questions
    
    return random.sample(questions, count)


def get_question_by_id(question_id):
    """
    Get a specific question by ID
    
    Args:
        question_id: The question ID to find
    
    Returns:
        dict: Question object or None if not found
    """
    all_questions = load_questions()
    
    for level_questions in all_questions.values():
        for question in level_questions:
            if question['id'] == question_id:
                return question
    
    return None


def validate_answer(question_id, answer):
    """
    Validate a user's answer
    
    Args:
        question_id: The question ID
        answer: The user's answer (option index)
    
    Returns:
        dict: Result with correct status, explanation, and points
    """
    question = get_question_by_id(question_id)
    
    if not question:
        return {
            'correct': False,
            'explanation': 'Question not found',
            'points': 0
        }
    
    is_correct = answer == question['correct']
    
    return {
        'correct': is_correct,
        'explanation': question.get('explanation', ''),
        'points': question.get('points', 10) if is_correct else 0,
        'correct_answer': question['correct']
    }


def get_all_categories():
    """Get list of all unique categories across all questions"""
    all_questions = load_questions()
    categories = set()
    
    for level_questions in all_questions.values():
        for question in level_questions:
            if 'category' in question:
                categories.add(question['category'])
    
    return sorted(list(categories))


def get_question_count_by_level():
    """Get count of questions for each level"""
    all_questions = load_questions()
    return {
        level: len(questions) 
        for level, questions in all_questions.items()
    }


if __name__ == '__main__':
    # Test the module
    print("Testing questions module...")
    
    counts = get_question_count_by_level()
    print(f"\n📊 Question counts: {counts}")
    
    categories = get_all_categories()
    print(f"\n📚 Categories: {categories}")
    
    print("\n🎮 Sample beginner question:")
    beginner_questions = get_questions_by_level('beginner')
    if beginner_questions:
        q = beginner_questions[0]
        print(f"  Q: {q['question']}")
        print(f"  Category: {q.get('category', 'N/A')}")
        print(f"  Points: {q.get('points', 10)}")
