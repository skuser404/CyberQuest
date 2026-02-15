# 🛡️ CyberQuest: Cybersecurity Awareness Game for Beginners

[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue)](https://www.python.org/)
[![Flask Version](https://img.shields.io/badge/flask-3.0.0-green)](https://flask.palletsprojects.com/)
[![License](https://img.shields.io/badge/license-MIT-purple)](LICENSE)
[![Status](https://img.shields.io/badge/status-active-success)]()

> An interactive educational game that teaches fundamental cybersecurity concepts through engaging, scenario-based challenges. Learn to protect yourself from phishing, malware, social engineering, and other cyber threats!

## 🌟 Project Overview

CyberQuest is a **free, web-based cybersecurity training game** designed to make security education accessible, engaging, and effective for everyone. Through realistic scenarios and immediate feedback, players learn to identify threats and develop secure habits.

### 🎯 Why Cyber Awareness Matters

- **💰 $10.5 Trillion**: Annual cost of cybercrime by 2025
- **📧 3.4 Billion**: Phishing emails sent daily worldwide
- **⏱️ Every 11 Seconds**: A business falls victim to ransomware
- **🎯 95% of Breaches**: Caused by human error

**The problem is urgent. Traditional training isn't working. CyberQuest is the solution.**

## ✨ Features

### 🎮 Interactive Learning
- **Scenario-Based Questions**: Learn from real-world situations, not theory
- **Immediate Feedback**: Understand WHY answers are correct or incorrect
- **Safe Environment**: Make mistakes without real-world consequences

### 📊 Progress Tracking
- **Risk Assessment**: Get rated from "High Risk 🚨" to "Cyber Defender 🛡️"
- **Category Performance**: Visualize strengths and weaknesses with Chart.js
- **Personalized Suggestions**: Receive targeted improvement recommendations

### 🏆 Gamification
- **Three Difficulty Levels**: Beginner 🌱, Intermediate 🔥, Advanced 🚀
- **Points System**: Earn 10-20 points per correct answer
- **Leaderboard**: Compete with other players globally
- **Achievement Badges**: Earn recognition for your cybersecurity expertise

### 📚 Educational Content
- **7 Core Topics**:
  - 🎣 Phishing Detection
  - 🔑 Password Security
  - 🎭 Social Engineering
  - 🌐 Safe Browsing
  - 🦠 Malware Awareness
  - 🔐 Two-Factor Authentication
  - 🔒 Basic Encryption
- **Detailed Explanations**: Every question includes educational insights
- **Curated Resources**: Links to trusted cybersecurity organizations

## 🏗️ Game Architecture

### Technology Stack

```
┌─────────────────────────────────────────────┐
│             FRONTEND                        │
│  HTML5 | CSS3 | JavaScript | Chart.js       │
└─────────────────────┬───────────────────────┘
                      │ HTTP/JSON
┌─────────────────────▼────────────────────────┐
│             BACKEND                          │
│  Python 3.8+ | Flask 3.0 | Jinja2            │
│                                              │
│  Modules:                                    │
│  • app.py (routes & controllers)             │
│  • game_logic.py (scoring & assessment)      │
│  • questions.py (question management)        │
│  • database.py (data persistence)            │
│  • utils.py (helpers & validation)           │
└─────────────────────┬────────────────────────┘
                      │
┌─────────────────────▼───────────────────────┐
│            DATABASE                         │
│  SQLite 3 (players, scores, attempts)       │
│  JSON (question bank)                       │
└─────────────────────────────────────────────┘
```

### Project Structure

```
CyberQuest/
├── src/                    # Backend Python modules
│   ├── app.py             # Main Flask application
│   ├── database.py        # Database operations
│   ├── game_logic.py      # Scoring & risk assessment
│   ├── questions.py       # Question management
│   └── utils.py           # Helper functions
│
├── templates/             # HTML templates (Jinja2)
│   ├── index.html        # Home page
│   ├── level.html        # Game play page
│   ├── result.html       # Results & feedback page
│   └── leaderboard.html  # Leaderboard page
│
├── static/               # Frontend assets
│   ├── styles.css       # All styling
│   ├── game.js          # Game logic
│   └── charts.js        # Visualizations
│
├── data/                # Data files
│   ├── questions.json   # Question bank (15 questions)
│   └── cyberquest.db    # SQLite database (auto-created)
│
├── docs/                # Comprehensive documentation
│   ├── problem_statement.md
│   ├── system_architecture.md
│   ├── learning_objectives.md
│   ├── game_design.md
│   └── workflow.md
│
├── requirements.txt     # Python dependencies
├── .gitignore          # Git ignore rules
├── LICENSE             # MIT License
└── README.md           # This file
```

## 🚀 Installation Guide

### Prerequisites
- **Python 3.8+** ([Download](https://www.python.org/downloads/))
- **pip** (included with Python)
- **Git** ([Download](https://git-scm.com/downloads))
- **Web Browser** (Chrome, Firefox, Safari, or Edge)

### Step-by-Step Setup

#### 1. Clone the Repository
```bash
git clone https://github.com/skuser404/CyberQuest.git
cd CyberQuest
```

#### 2. Create Virtual Environment
```bash
# On Linux/Mac:
python3 -m venv venv
source venv/bin/activate

# On Windows:
python -m venv venv
venv\Scripts\activate
```

#### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

#### 4. Initialize Database
```bash
python src/database.py
```

#### 5. Run the Application
```bash
python src/app.py
```

#### 6. Open in Browser
Navigate to: **http://localhost:5000**

You should see the CyberQuest home page! 🎉

### Quick Test
```bash
# In another terminal, test the application
curl http://localhost:5000
# Should return HTML content
```

## 🎯 How to Play

### Step 1: Enter Username
Choose a unique username (3-50 characters, alphanumeric + `_` and `-`)

### Step 2: Select Difficulty

| Level | Icon | Description | Questions | Points |
|-------|------|-------------|-----------|--------|
| **Beginner** | 🌱 | Learn fundamental concepts | 5 | 10 each |
| **Intermediate** | 🔥 | Test with real-world scenarios | 5 | 15 each |
| **Advanced** | 🚀 | Master advanced security concepts | 5 | 20 each |

### Step 3: Answer Questions
- Read each scenario carefully
- Select the BEST answer
- Use Previous/Next to navigate
- Review your answers before submitting

### Step 4: Get Results
- See your total score and percentage
- Receive risk level assessment (🚨 High Risk → 🛡️ Cyber Defender)
- Review detailed feedback for each question
- View performance by category with charts
- Get personalized improvement suggestions

### Step 5: Check Leaderboard
- See top 10 players
- Compare your performance
- Challenge yourself to improve!

## 📈 Learning Outcomes

By completing CyberQuest, you will:

✅ **Identify phishing attempts** in emails and websites  
✅ **Create strong, unique passwords** using best practices  
✅ **Recognize social engineering tactics** and respond appropriately  
✅ **Verify website security** before entering sensitive information  
✅ **Detect malware threats** and avoid infection  
✅ **Implement two-factor authentication** for account protection  
✅ **Understand basic encryption** and its importance  
✅ **Respond to security incidents** properly  
✅ **Develop security-conscious habits** for daily digital life  

## 🎓 Educational Impact

### Target Audience
- **Beginners**: No prior cybersecurity knowledge required
- **Students**: High school to college level digital citizenship
- **Employees**: Non-IT staff needing security awareness
- **General Public**: Anyone who uses the internet

### Learning Approach
- **Constructivist**: Learn by doing, not passive reading
- **Immediate Feedback**: Understand mistakes instantly
- **Scaffolded**: Progress from basic to advanced concepts
- **Real-World**: Scenarios based on actual security incidents

### Bloom's Taxonomy Coverage
1. **Remember**: Recall security concepts and definitions
2. **Understand**: Explain why threats work and how to prevent them
3. **Apply**: Use security knowledge in realistic scenarios
4. **Analyze**: Evaluate security risks and compare options
5. **Evaluate**: Judge security practices and prioritize actions
6. **Create**: Develop personal security protocols

## 🔒 Ethical Use Statement

CyberQuest is designed for **educational purposes only**. 

### Permitted Uses ✅
- Learning cybersecurity concepts
- Teaching security awareness in schools/organizations
- Self-assessment of security knowledge
- Training employees on cyber threats
- Promoting cybersecurity best practices

### Prohibited Uses ❌
- Testing security on systems you don't own
- Actual phishing or social engineering attacks
- Distributing malware or harmful code
- Exploiting vulnerabilities for malicious purposes
- Any illegal or unethical hacking activities

**By using CyberQuest, you agree to use the knowledge gained responsibly and ethically to PROTECT, not harm.**

## 🔧 Configuration & Customization

### Adding Questions
Edit `data/questions.json`:
```json
{
  "beginner": [
    {
      "id": 16,
      "type": "phishing",
      "question": "Your scenario here...",
      "options": ["A", "B", "C", "D"],
      "correct": 1,
      "explanation": "Educational explanation...",
      "points": 10,
      "category": "Phishing Detection"
    }
  ]
}
```

### Modifying Risk Levels
Edit `src/game_logic.py`:
```python
def calculate_risk_level(score, max_score):
    percentage = (score / max_score) * 100
    
    if percentage >= 90:  # Adjust thresholds
        return ("Cyber Defender 🛡️", "description", "🛡️", "#10b981")
    # ... etc
```

### Changing Styling
Edit `static/styles.css`:
```css
:root {
    --primary-color: #3b82f6;  /* Your brand color */
    --secondary-color: #8b5cf6;
    /* ... */
}
```

## 🐛 Troubleshooting

### Common Issues & Solutions

**Issue**: `ModuleNotFoundError: No module named 'flask'`  
**Solution**: Activate virtual environment and install dependencies
```bash
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -r requirements.txt
```

**Issue**: `sqlite3.OperationalError: unable to open database file`  
**Solution**: Create data directory and initialize database
```bash
mkdir -p data
python src/database.py
```

**Issue**: `Address already in use` (port 5000)  
**Solution**: Kill existing process or change port
```bash
# Find and kill process
lsof -i :5000  # On Linux/Mac
kill -9 <PID>

# Or change port in app.py
app.run(host='0.0.0.0', port=8080, debug=True)
```

**Issue**: Questions not displaying  
**Solution**: Verify JSON syntax
```bash
python -m json.tool data/questions.json
```

## 📊 Current Status

### Completed Features ✅
- ✅ Full Flask backend with session management
- ✅ SQLite database with 3 tables
- ✅ 15 scenario-based questions across 3 difficulty levels
- ✅ Responsive HTML/CSS frontend
- ✅ Interactive game play with navigation
- ✅ Real-time scoring and feedback
- ✅ Risk level assessment algorithm
- ✅ Chart.js visualizations for results
- ✅ Category performance breakdown
- ✅ Leaderboard with top 10 players
- ✅ Personalized improvement suggestions
- ✅ Learning resources and educational tips
- ✅ Input validation and security measures
- ✅ Comprehensive documentation (5 docs)

### Current Limitations
- Questions: 15 total (5 per level) - limited variety
- Single-player only (no multiplayer mode)
- No user accounts (session-based only)
- No achievement badges system
- No certificate generation
- English language only

## 🚀 Future Enhancements

### Phase 2 (Short-Term)
- [ ] Expand question bank to 50+ questions
- [ ] Add achievement badges system
- [ ] Implement daily challenge mode
- [ ] Create personal progress dashboard
- [ ] Add social sharing features

### Phase 3 (Medium-Term)
- [ ] Multi-language support (Spanish, French, Hindi)
- [ ] Mobile app (React Native)
- [ ] User accounts with login
- [ ] Certificate of completion (PDF)
- [ ] Community discussion forum

### Phase 4 (Long-Term)
- [ ] AI-powered adaptive difficulty
- [ ] VR/AR immersive scenarios
- [ ] Enterprise version with custom content
- [ ] Integration with LMS platforms (Canvas, Moodle)
- [ ] Advanced analytics dashboard for educators

## 🤝 Contributing

We welcome contributions! Here's how you can help:

### Ways to Contribute
1. **Add Questions**: Submit new scenario-based questions
2. **Fix Bugs**: Report or fix issues you find
3. **Improve Documentation**: Clarify or expand docs
4. **Translate**: Help make CyberQuest multilingual
5. **Spread the Word**: Share with friends, colleagues, students

### Contribution Process
```bash
# 1. Fork the repository
# 2. Create a feature branch
git checkout -b feature/your-feature-name

# 3. Make your changes
# 4. Test thoroughly
# 5. Commit with clear messages
git commit -m "feat: add new phishing scenarios"

# 6. Push and create Pull Request
git push origin feature/your-feature-name
```

## 📜 License

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.

**TL;DR**: You can use, modify, and distribute this software freely for personal or commercial purposes, as long as you include the original license.

## 👨‍💻 Author Details

**Project**: CyberQuest - Cybersecurity Awareness Game  
**Created By**: Dr. Research Scholar  
**Occupation**: Machine Learning Research Scientist (NLP & Sentiment Analysis)  
**GitHub**: [@skuser404](https://github.com/skuser404)  
**Purpose**: Educational cybersecurity training through gamification  
**Year**: 2024  

### About the Author
Accomplished research scientist with expertise in machine learning, natural language processing, and sentiment analysis. Specializes in developing innovative solutions for social media analytics and interactive educational systems. Passionate about bridging the gap between academic research and practical applications in cybersecurity education.

## 🌐 Deployment

### Local Development
```bash
python src/app.py
# Visit: http://localhost:5000
```

### Production Deployment Options

#### Heroku (Easy)
```bash
heroku create cyberquest-app
git push heroku main
```

#### PythonAnywhere (Free)
1. Upload code via Git
2. Configure WSGI
3. Set working directory
4. Done!

#### VPS (DigitalOcean, AWS, etc.)
```bash
# Install dependencies
sudo apt install python3-pip nginx gunicorn

# Configure nginx + gunicorn
# Set up SSL with Let's Encrypt
```

## 📞 Support & Contact

### Get Help
- **Issues**: [GitHub Issues](https://github.com/skuser404/CyberQuest/issues)
- **Discussions**: [GitHub Discussions](https://github.com/skuser404/CyberQuest/discussions)
- **Email**: Create an issue for contact

### Reporting Security Vulnerabilities
If you discover a security vulnerability, please email the project maintainers privately. Do NOT open a public issue.

## 🙏 Acknowledgments

### Resources & Inspiration
- **OWASP**: Web security education resources
- **SANS Institute**: Cybersecurity training methodologies
- **CISA**: Government cybersecurity awareness campaigns
- **Khan Academy**: Gamified learning approach
- **Duolingo**: Bite-sized, engaging education model

### Technologies Used
- **Flask**: Lightweight Python web framework
- **Chart.js**: Beautiful, responsive charts
- **SQLite**: Simple, serverless database
- **Font Awesome**: Icon library
- **Google Fonts**: Inter typography

## 📊 Project Statistics

- **Lines of Code**: ~5,000
- **Files**: 20+
- **Documentation**: 5 comprehensive guides
- **Questions**: 15 scenarios (expandable)
- **Topics Covered**: 7 core cybersecurity areas
- **Difficulty Levels**: 3 (Beginner → Advanced)
- **Development Time**: Educational project

## 🎉 Thank You!

Thank you for using **CyberQuest**! Together, we can make the internet safer by educating users about cybersecurity threats and best practices.

**Remember**: Security is everyone's responsibility. Stay vigilant, stay informed, stay safe! 🛡️

---

**⭐ If you find this project helpful, please give it a star on GitHub! ⭐**

**📢 Share CyberQuest with your friends, family, and colleagues to spread cybersecurity awareness! 📢**

---

*Built with ❤️ for a safer digital world*
