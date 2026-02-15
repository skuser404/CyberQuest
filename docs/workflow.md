# Development & Deployment Workflow

## Development Environment Setup

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)
- Git (version control)
- Text editor (VS Code, PyCharm, Sublime, etc.)
- Web browser (Chrome, Firefox for testing)

### Initial Setup

```bash
# 1. Clone the repository
git clone https://github.com/skuser404/CyberQuest.git
cd CyberQuest

# 2. Create virtual environment
python3 -m venv venv

# 3. Activate virtual environment
# On Linux/Mac:
source venv/bin/activate
# On Windows:
venv\Scripts\activate

# 4. Install dependencies
pip install -r requirements.txt

# 5. Initialize database
python src/database.py

# 6. Run the application
python src/app.py

# 7. Open browser
# Navigate to http://localhost:5000
```

## Project Structure Workflow

### Directory Organization

```
CyberQuest/
├── src/                  # Backend Python code
│   ├── app.py           # Main Flask application
│   ├── database.py      # Database operations
│   ├── game_logic.py    # Scoring & risk assessment
│   ├── questions.py     # Question management
│   └── utils.py         # Helper functions
│
├── templates/           # HTML templates (Jinja2)
│   ├── index.html      # Home page
│   ├── level.html      # Game play page
│   ├── result.html     # Results page
│   └── leaderboard.html # Leaderboard page
│
├── static/             # Frontend assets
│   ├── styles.css      # All CSS styles
│   ├── game.js         # Game logic JavaScript
│   └── charts.js       # Chart.js visualizations
│
├── data/               # Data files
│   ├── questions.json  # Question bank
│   └── cyberquest.db   # SQLite database (auto-created)
│
├── docs/               # Documentation
│   ├── problem_statement.md
│   ├── system_architecture.md
│   ├── learning_objectives.md
│   ├── game_design.md
│   └── workflow.md
│
├── requirements.txt    # Python dependencies
├── .gitignore         # Git ignore rules
├── LICENSE            # MIT License
└── README.md          # Project documentation
```

## Development Workflow

### 1. Feature Development Process

```mermaid
Feature Request → Create Branch → Develop → Test → Code Review → Merge → Deploy
```

#### Step-by-Step

**A. Create Feature Branch**
```bash
git checkout -b feature/add-new-questions
```

**B. Develop Feature**
```bash
# Make changes to files
# For example: Add questions to data/questions.json

# Test locally
python src/app.py
# Verify in browser
```

**C. Test Changes**
```bash
# Manual testing checklist:
# ✅ Game loads without errors
# ✅ Questions display correctly
# ✅ Answers submit successfully
# ✅ Results calculate accurately
# ✅ Leaderboard updates
# ✅ All links work
# ✅ Responsive design works on mobile
```

**D. Commit Changes**
```bash
git add .
git commit -m "feat: add 5 new phishing detection questions"
```

**E. Push & Create Pull Request**
```bash
git push origin feature/add-new-questions
# Create pull request on GitHub
```

**F. Code Review**
```bash
# Team member reviews code
# Address feedback
# Get approval
```

**G. Merge to Main**
```bash
git checkout main
git merge feature/add-new-questions
git push origin main
```

### 2. Adding New Questions

**Location**: `data/questions.json`

**Process**:
1. Identify gap in question coverage
2. Research real-world scenarios
3. Write question following template:

```json
{
  "id": 16,
  "type": "category_name",
  "question": "Scenario-based question using real context...",
  "options": [
    "Plausible but incorrect option",
    "Correct answer with clear reasoning",
    "Common misconception",
    "Another plausible wrong answer"
  ],
  "correct": 1,
  "explanation": "Clear explanation of why answer is correct, including statistics or tips. Make it educational!",
  "points": 10,
  "category": "Category Name"
}
```

4. Test question in game
5. Verify explanation clarity
6. Commit with descriptive message

### 3. Modifying Game Logic

**Location**: `src/game_logic.py`

**Common Modifications**:

**A. Adjust Risk Level Thresholds**
```python
def calculate_risk_level(score, max_score):
    percentage = (score / max_score) * 100
    
    # Modify these thresholds
    if percentage >= 90:  # Change to 95 for stricter
        return "Cyber Defender"
    elif percentage >= 75:  # Change to 80
        return "Security Aware"
    # etc.
```

**B. Change Point Values**
Edit `data/questions.json`:
```json
{
  "points": 15  # Change from 10 to 15
}
```

**C. Add New Categories**
1. Add questions with new category name
2. Add category emoji in `src/utils.py`:
```python
emoji_map = {
    "New Category": "🆕",
    # ...existing categories
}
```

### 4. Styling Changes

**Location**: `static/styles.css`

**Common Changes**:

**A. Color Scheme**
```css
:root {
    --primary-color: #3b82f6;  /* Change to your brand color */
    --secondary-color: #8b5cf6;
    /* etc. */
}
```

**B. Font**
```css
body {
    font-family: 'Roboto', sans-serif;  /* Change font */
}
```

**C. Responsive Breakpoints**
```css
@media (max-width: 768px) {
    /* Adjust mobile styles */
}
```

### 5. Database Schema Changes

**Location**: `src/database.py`

**Process**:
1. Modify table schema in `init_database()`
2. Drop existing database: `rm data/cyberquest.db`
3. Reinitialize: `python src/database.py`
4. Test all database operations

**Example**: Add email column to players
```python
cursor.execute('''
    CREATE TABLE IF NOT EXISTS players (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL UNIQUE,
        email TEXT,  # NEW COLUMN
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
''')
```

## Testing Workflow

### Manual Testing Checklist

#### Homepage Testing
- [ ] Page loads without errors
- [ ] Username input accepts valid names
- [ ] Username validation rejects invalid names
- [ ] All level cards display correctly
- [ ] Start buttons work for all levels
- [ ] Leaderboard link works
- [ ] Statistics display correctly

#### Game Play Testing
- [ ] Questions load for each difficulty
- [ ] Radio buttons select correctly
- [ ] Navigation (Next/Previous) works
- [ ] Progress bar updates
- [ ] Score counter displays
- [ ] Submit button appears on last question
- [ ] Answer summary shows correctly
- [ ] Confirmation works before final submit

#### Results Page Testing
- [ ] Score calculates correctly
- [ ] Risk level assigns correctly
- [ ] Category chart displays data
- [ ] Feedback shows for each question
- [ ] Correct/incorrect answers marked clearly
- [ ] Explanations display fully
- [ ] Suggestions generate based on performance
- [ ] Learning resources display
- [ ] Action buttons work (Play Again, Leaderboard)

#### Leaderboard Testing
- [ ] Top scores display in order
- [ ] Player names show correctly
- [ ] Scores and percentages accurate
- [ ] Medals appear for top 3
- [ ] Current player highlighted
- [ ] Dates display correctly
- [ ] Empty state shows when no scores

#### Cross-Browser Testing
Test on:
- [ ] Chrome (Windows/Mac)
- [ ] Firefox (Windows/Mac)
- [ ] Safari (Mac)
- [ ] Edge (Windows)
- [ ] Mobile Safari (iOS)
- [ ] Mobile Chrome (Android)

#### Responsive Design Testing
Test at widths:
- [ ] 1920px (Desktop)
- [ ] 1366px (Laptop)
- [ ] 768px (Tablet)
- [ ] 375px (Mobile)

### Automated Testing (Future)

```python
# Unit tests for game logic
import unittest
from src.game_logic import calculate_risk_level

class TestGameLogic(unittest.TestCase):
    def test_cyber_defender(self):
        risk_level, _, _, _ = calculate_risk_level(95, 100)
        self.assertEqual(risk_level, "Cyber Defender 🛡️")
    
    def test_high_risk(self):
        risk_level, _, _, _ = calculate_risk_level(25, 100)
        self.assertEqual(risk_level, "High Risk 🚨")

if __name__ == '__main__':
    unittest.main()
```

## Deployment Workflow

### Local Development
```bash
# Run Flask development server
python src/app.py

# Server runs on http://localhost:5000
# Debug mode enabled (auto-reload on changes)
```

### Production Deployment Options

#### Option 1: Heroku (Recommended for Beginners)

```bash
# 1. Install Heroku CLI
# 2. Login
heroku login

# 3. Create Heroku app
heroku create cyberquest-app

# 4. Add Procfile
echo "web: gunicorn src.app:app" > Procfile

# 5. Add gunicorn to requirements.txt
echo "gunicorn==21.2.0" >> requirements.txt

# 6. Deploy
git add .
git commit -m "deploy: configure for Heroku"
git push heroku main

# 7. Open app
heroku open
```

#### Option 2: PythonAnywhere

```bash
# 1. Sign up at pythonanywhere.com
# 2. Upload code via Git
# 3. Create virtual environment
# 4. Configure WSGI file
# 5. Set working directory
# 6. Reload web app
```

#### Option 3: DigitalOcean / AWS / VPS

```bash
# 1. Set up Ubuntu server
# 2. Install Python, nginx, gunicorn
sudo apt update
sudo apt install python3-pip python3-venv nginx

# 3. Clone repo
git clone https://github.com/skuser404/CyberQuest.git

# 4. Set up virtual environment
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# 5. Configure gunicorn
gunicorn --bind 0.0.0.0:8000 src.app:app

# 6. Configure nginx reverse proxy
# 7. Set up systemd service for auto-start
# 8. Configure SSL with Let's Encrypt
```

### Environment Configuration

**Development** (`src/app.py`):
```python
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
```

**Production** (use gunicorn):
```bash
gunicorn --workers 4 --bind 0.0.0.0:8000 src.app:app
```

### Database Migration

**Development to Production**:
```bash
# Export development database
sqlite3 data/cyberquest.db .dump > backup.sql

# On production server
# Create database from backup
sqlite3 data/cyberquest.db < backup.sql
```

**PostgreSQL Migration** (for scale):
```bash
# Install PostgreSQL adapter
pip install psycopg2-binary

# Modify database.py to use PostgreSQL
# Update connection string
# Migrate schema
```

## Git Workflow

### Branch Strategy

```
main (production-ready code)
  └── develop (integration branch)
       ├── feature/add-questions
       ├── feature/new-game-mode
       └── bugfix/leaderboard-sorting
```

### Commit Message Convention

```
type(scope): brief description

[optional body]

[optional footer]
```

**Types**:
- `feat`: New feature
- `fix`: Bug fix
- `docs`: Documentation changes
- `style`: Formatting, no code change
- `refactor`: Code restructuring
- `test`: Adding tests
- `chore`: Maintenance tasks

**Examples**:
```bash
git commit -m "feat: add ransomware awareness questions"
git commit -m "fix: leaderboard sorting by score descending"
git commit -m "docs: update installation instructions in README"
git commit -m "style: improve mobile responsive design"
```

### Release Process

```bash
# 1. Test thoroughly on develop branch
git checkout develop
# ... test everything

# 2. Create release branch
git checkout -b release/v1.1.0

# 3. Update version numbers
# Edit __init__.py, README.md, etc.

# 4. Final testing

# 5. Merge to main
git checkout main
git merge release/v1.1.0

# 6. Tag release
git tag -a v1.1.0 -m "Release version 1.1.0"
git push origin main --tags

# 7. Merge back to develop
git checkout develop
git merge main

# 8. Deploy to production
```

## Monitoring & Maintenance

### Health Checks
```bash
# Check if app is running
curl http://localhost:5000

# Check database integrity
sqlite3 data/cyberquest.db "PRAGMA integrity_check;"

# Monitor logs
tail -f logs/app.log  # If logging configured
```

### Backup Strategy

**Daily Backups**:
```bash
#!/bin/bash
# backup.sh
DATE=$(date +%Y-%m-%d)
sqlite3 data/cyberquest.db .dump > backups/cyberquest_$DATE.sql
```

**Weekly Full Backups**:
```bash
tar -czf backups/CyberQuest_full_$DATE.tar.gz .
```

### Performance Monitoring

**Key Metrics**:
- Response time (<200ms target)
- Database query time (<50ms target)
- Error rate (<0.1% target)
- User completion rate (>70% target)

**Tools** (production):
- New Relic (APM)
- Sentry (error tracking)
- Google Analytics (user behavior)

## Security Workflow

### Security Checklist

- [ ] Input validation on all user inputs
- [ ] SQL injection prevention (parameterized queries)
- [ ] XSS prevention (Jinja2 auto-escaping)
- [ ] CSRF protection (Flask-WTF in production)
- [ ] Secure session cookies (httponly, secure flags)
- [ ] HTTPS in production
- [ ] Security headers (CSP, X-Frame-Options)
- [ ] Dependency updates (Dependabot)
- [ ] Regular security audits

### Dependency Updates

```bash
# Check for outdated packages
pip list --outdated

# Update specific package
pip install --upgrade Flask

# Update requirements.txt
pip freeze > requirements.txt

# Test after updates
python src/app.py
# Run full test suite
```

### Security Incident Response

1. **Detect**: Monitor error logs
2. **Assess**: Determine severity
3. **Contain**: Take affected systems offline if needed
4. **Eradicate**: Patch vulnerability
5. **Recover**: Restore service
6. **Learn**: Document and prevent recurrence

## Contribution Workflow

### For Contributors

```bash
# 1. Fork repository on GitHub

# 2. Clone your fork
git clone https://github.com/YOUR_USERNAME/CyberQuest.git

# 3. Create feature branch
git checkout -b feature/my-contribution

# 4. Make changes

# 5. Commit with clear messages
git commit -m "feat: add accessibility improvements"

# 6. Push to your fork
git push origin feature/my-contribution

# 7. Create Pull Request on original repo
# 8. Wait for review
# 9. Address feedback
# 10. Get merged!
```

### Code Review Checklist

- [ ] Code follows project style
- [ ] Tests pass (if applicable)
- [ ] Documentation updated
- [ ] No security vulnerabilities
- [ ] Performance not degraded
- [ ] Accessibility maintained
- [ ] Mobile responsive
- [ ] Browser compatible

## Troubleshooting Common Issues

### Issue: "Module not found" errors
**Solution**:
```bash
source venv/bin/activate  # Activate virtual environment
pip install -r requirements.txt
```

### Issue: Database locked error
**Solution**:
```bash
# Close all connections to database
fuser -k data/cyberquest.db  # Linux
# Or restart application
```

### Issue: Port 5000 already in use
**Solution**:
```bash
# Find process using port
lsof -i :5000
# Kill process
kill -9 <PID>
# Or change port in app.py
```

### Issue: Static files not loading
**Solution**:
```python
# Check Flask static folder configuration
app = Flask(__name__, static_folder='static', template_folder='templates')
```

### Issue: Questions not loading
**Solution**:
```bash
# Verify JSON syntax
python -m json.tool data/questions.json
# Check file path in questions.py
```

## Conclusion

This workflow document provides a complete guide for:
- Setting up development environment
- Developing new features
- Testing changes
- Deploying to production
- Maintaining the application
- Contributing to the project

Follow these workflows to ensure **consistent, quality, and secure** development of CyberQuest!
