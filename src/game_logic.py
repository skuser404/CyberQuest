"""
Game logic module for CyberQuest
Handles scoring, risk assessment, and game flow
"""

def calculate_risk_level(score, max_score):
    """
    Calculate risk level based on score percentage
    
    Returns:
        tuple: (risk_level, risk_description, risk_emoji)
    """
    percentage = (score / max_score) * 100 if max_score > 0 else 0
    
    if percentage >= 90:
        return (
            "Cyber Defender 🛡️",
            "Outstanding! You're a cybersecurity champion! You understand security fundamentals and can protect yourself and others online.",
            "🛡️",
            "#10b981"  # Green
        )
    elif percentage >= 75:
        return (
            "Security Aware 🔐",
            "Great job! You have strong cybersecurity awareness. Keep learning and stay vigilant!",
            "🔐",
            "#3b82f6"  # Blue
        )
    elif percentage >= 60:
        return (
            "Safe User 🔒",
            "Good foundation! You understand basic security concepts but should continue learning to improve your defenses.",
            "🔒",
            "#f59e0b"  # Yellow
        )
    elif percentage >= 40:
        return (
            "At Risk ⚠️",
            "You're vulnerable to many common attacks. Take time to learn cybersecurity basics to protect yourself online!",
            "⚠️",
            "#f97316"  # Orange
        )
    else:
        return (
            "High Risk 🚨",
            "Critical! Your cybersecurity knowledge needs immediate improvement. You're highly vulnerable to attacks. Please study the educational materials!",
            "🚨",
            "#ef4444"  # Red
        )


def get_level_metadata():
    """Get metadata for each difficulty level"""
    return {
        "beginner": {
            "name": "Beginner",
            "description": "Learn fundamental cybersecurity concepts",
            "icon": "🌱",
            "color": "#10b981",
            "question_count": 5
        },
        "intermediate": {
            "name": "Intermediate",
            "description": "Test your security knowledge with real-world scenarios",
            "icon": "🔥",
            "color": "#3b82f6",
            "question_count": 5
        },
        "advanced": {
            "name": "Advanced",
            "description": "Master advanced security concepts and incident response",
            "icon": "🚀",
            "color": "#8b5cf6",
            "question_count": 5
        }
    }


def calculate_category_stats(questions, answers):
    """
    Calculate performance statistics by category
    
    Args:
        questions: List of question objects
        answers: Dictionary of user answers {question_id: selected_option}
    
    Returns:
        dict: Category performance statistics
    """
    categories = {}
    
    for question in questions:
        category = question.get('category', 'General')
        
        if category not in categories:
            categories[category] = {
                'total': 0,
                'correct': 0,
                'percentage': 0
            }
        
        categories[category]['total'] += 1
        
        # Check if answer is correct
        question_id = question['id']
        user_answer = answers.get(str(question_id))
        
        if user_answer is not None and user_answer == question['correct']:
            categories[category]['correct'] += 1
    
    # Calculate percentages
    for category in categories:
        total = categories[category]['total']
        correct = categories[category]['correct']
        categories[category]['percentage'] = round((correct / total) * 100, 1) if total > 0 else 0
    
    return categories


def generate_feedback(questions, answers):
    """
    Generate detailed feedback for each question
    
    Args:
        questions: List of question objects
        answers: Dictionary of user answers
    
    Returns:
        list: Feedback objects with question details and explanations
    """
    feedback = []
    
    for question in questions:
        question_id = str(question['id'])
        user_answer = answers.get(question_id)
        correct_answer = question['correct']
        is_correct = user_answer == correct_answer
        
        feedback.append({
            'question': question['question'],
            'category': question.get('category', 'General'),
            'user_answer': question['options'][user_answer] if user_answer is not None else "Not answered",
            'correct_answer': question['options'][correct_answer],
            'is_correct': is_correct,
            'explanation': question.get('explanation', ''),
            'points_earned': question.get('points', 10) if is_correct else 0,
            'points_possible': question.get('points', 10)
        })
    
    return feedback


def get_learning_resources():
    """Get recommended learning resources based on common weak areas"""
    return {
        "Phishing Detection": {
            "tips": [
                "Always check sender email addresses carefully",
                "Hover over links before clicking to see the actual URL",
                "Be suspicious of urgent or threatening language",
                "Verify requests through official channels"
            ],
            "resources": [
                "https://www.phishing.org/phishing-examples",
                "https://www.consumer.ftc.gov/articles/how-recognize-and-avoid-phishing-scams"
            ]
        },
        "Password Security": {
            "tips": [
                "Use 12+ character passwords with mixed case, numbers, and symbols",
                "Never reuse passwords across sites",
                "Use a password manager like Bitwarden or 1Password",
                "Enable two-factor authentication everywhere possible"
            ],
            "resources": [
                "https://www.security.org/how-secure-is-my-password/",
                "https://haveibeenpwned.com/"
            ]
        },
        "Social Engineering": {
            "tips": [
                "Verify identities through independent channels",
                "Be skeptical of unsolicited requests for information",
                "Never share credentials or sensitive data over phone/email",
                "Question urgent or unusual requests"
            ],
            "resources": [
                "https://www.social-engineer.org/",
                "https://www.cisa.gov/social-engineering"
            ]
        },
        "Malware Awareness": {
            "tips": [
                "Keep software and operating systems updated",
                "Use reputable antivirus/anti-malware software",
                "Don't download software from untrusted sources",
                "Be cautious with email attachments"
            ],
            "resources": [
                "https://www.malwarebytes.com/what-is-malware",
                "https://www.cisa.gov/sites/default/files/publications/Malware_WhitePaper.pdf"
            ]
        },
        "Safe Browsing": {
            "tips": [
                "Look for HTTPS and the padlock icon",
                "Avoid clicking on suspicious pop-ups or ads",
                "Use browser extensions like uBlock Origin",
                "Keep your browser updated"
            ],
            "resources": [
                "https://safebrowsing.google.com/",
                "https://www.eff.org/https-everywhere"
            ]
        }
    }


def get_improvement_suggestions(category_stats):
    """
    Generate personalized improvement suggestions based on performance
    
    Args:
        category_stats: Dictionary of category performance statistics
    
    Returns:
        list: Prioritized improvement suggestions
    """
    suggestions = []
    
    # Sort categories by performance (worst first)
    sorted_categories = sorted(
        category_stats.items(),
        key=lambda x: x[1]['percentage']
    )
    
    for category, stats in sorted_categories[:3]:  # Top 3 weak areas
        if stats['percentage'] < 70:
            suggestions.append({
                'category': category,
                'performance': f"{stats['correct']}/{stats['total']} correct ({stats['percentage']}%)",
                'priority': 'high' if stats['percentage'] < 50 else 'medium',
                'recommendation': f"Focus on improving your {category} knowledge. Review the educational tips and resources provided."
            })
    
    return suggestions
