# System Architecture

## Overview
CyberQuest follows a traditional **Client-Server MVC Architecture** optimized for educational gaming, with clear separation of concerns and modular design for maintainability and scalability.

## Architecture Diagram

```
┌─────────────────────────────────────────────────────────────┐
│                        CLIENT SIDE                           │
├─────────────────────────────────────────────────────────────┤
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐     │
│  │   HTML/CSS   │  │  JavaScript  │  │   Chart.js   │     │
│  │  Templates   │  │  Game Logic  │  │ Visualizations│     │
│  └──────────────┘  └──────────────┘  └──────────────┘     │
│         ▼                 ▼                  ▼              │
│  ┌────────────────────────────────────────────────────┐    │
│  │            Browser (Chrome, Firefox, etc.)          │    │
│  └────────────────────────────────────────────────────┘    │
└────────────────────────┬────────────────────────────────────┘
                         │ HTTP/HTTPS (JSON)
                         ▼
┌─────────────────────────────────────────────────────────────┐
│                       SERVER SIDE                            │
├─────────────────────────────────────────────────────────────┤
│  ┌────────────────────────────────────────────────────┐    │
│  │              Flask Application (app.py)             │    │
│  │  ┌──────────────────────────────────────────────┐  │    │
│  │  │           Routing & Controllers              │  │    │
│  │  │  - index() - start_game() - submit()        │  │    │
│  │  │  - show_results() - leaderboard()           │  │    │
│  │  └──────────────────────────────────────────────┘  │    │
│  └────────────────────────────────────────────────────┘    │
│                         │                                    │
│       ┌─────────────────┼─────────────────┐               │
│       ▼                 ▼                 ▼                │
│  ┌──────────┐    ┌───────────┐    ┌──────────┐          │
│  │questions │    │game_logic │    │ database │          │
│  │   .py    │    │    .py    │    │   .py    │          │
│  │          │    │           │    │          │          │
│  │- Load Q  │    │- Scoring  │    │- CRUD    │          │
│  │- Validate│    │- Risk     │    │- Players │          │
│  └──────────┘    │- Stats    │    │- Scores  │          │
│                  └───────────┘    └──────────┘          │
│                                          │                │
│                                          ▼                │
│  ┌────────────────────────────────────────────────────┐  │
│  │                SQLite Database                      │  │
│  │  ┌──────────┐  ┌──────────┐  ┌─────────────────┐  │  │
│  │  │ players  │  │  scores  │  │question_attempts│  │  │
│  │  └──────────┘  └──────────┘  └─────────────────┘  │  │
│  └────────────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────────────┘
                         │
                         ▼
┌─────────────────────────────────────────────────────────────┐
│                      DATA LAYER                              │
├─────────────────────────────────────────────────────────────┤
│  ┌────────────────────────────────────────────────────┐    │
│  │          questions.json (Question Bank)             │    │
│  │  - Beginner (5 questions)                          │    │
│  │  - Intermediate (5 questions)                      │    │
│  │  - Advanced (5 questions)                          │    │
│  └────────────────────────────────────────────────────┘    │
└─────────────────────────────────────────────────────────────┘
```

## Component Breakdown

### 1. Frontend Layer

#### A. HTML Templates (`templates/`)
**Purpose**: User interface presentation

| Template | Purpose | Key Features |
|----------|---------|--------------|
| `index.html` | Landing page | Level selection, username input, stats |
| `level.html` | Game play | Question display, navigation, timer |
| `result.html` | Results page | Score breakdown, charts, feedback |
| `leaderboard.html` | Rankings | Top players, achievements |

**Technologies**:
- Jinja2 templating (Flask's built-in)
- Semantic HTML5
- Responsive design (mobile-first)

#### B. CSS (`static/styles.css`)
**Purpose**: Visual styling and user experience

**Design System**:
- Color palette: Primary (blue), Success (green), Danger (red)
- Typography: Inter font family
- Spacing: 8px grid system
- Components: Cards, buttons, badges, progress bars

**Responsive Breakpoints**:
- Desktop: 1200px+
- Tablet: 768px - 1199px
- Mobile: < 768px

#### C. JavaScript (`static/`)

**game.js**
- Question navigation
- Answer validation
- Progress tracking
- Local storage (auto-save)
- Keyboard shortcuts
- Form submission

**charts.js**
- Chart.js integration
- Category performance visualization
- Score distribution charts
- Radar charts for skill assessment

### 2. Backend Layer

#### A. Flask Application (`src/app.py`)
**Purpose**: Web server and request handling

**Key Routes**:
```python
GET  /                  # Home page
POST /start             # Initialize game session
GET  /play/<level>      # Game play page
POST /submit            # Submit answers, calculate score
GET  /results           # Display results
GET  /leaderboard       # Show top scores
GET  /reset             # Clear session
```

**Session Management**:
- Server-side sessions using Flask's secure cookies
- Stores: player_id, username, level, last_result
- Lifetime: 2 hours

#### B. Game Logic Module (`src/game_logic.py`)
**Purpose**: Business logic for scoring and assessment

**Core Functions**:
1. `calculate_risk_level(score, max_score)` → Risk assessment
2. `get_level_metadata()` → Difficulty level info
3. `calculate_category_stats(questions, answers)` → Performance by topic
4. `generate_feedback(questions, answers)` → Detailed explanations
5. `get_improvement_suggestions(stats)` → Personalized recommendations

**Risk Level Algorithm**:
```python
if percentage >= 90: "Cyber Defender"
elif percentage >= 75: "Security Aware"
elif percentage >= 60: "Safe User"
elif percentage >= 40: "At Risk"
else: "High Risk"
```

#### C. Questions Module (`src/questions.py`)
**Purpose**: Question bank management

**Functions**:
- Load questions from JSON
- Filter by difficulty level
- Validate answers
- Get random question subsets

**Question Structure**:
```json
{
  "id": 1,
  "type": "phishing",
  "question": "Question text...",
  "options": ["A", "B", "C", "D"],
  "correct": 1,
  "explanation": "Educational explanation...",
  "points": 10,
  "category": "Phishing Detection"
}
```

#### D. Database Module (`src/database.py`)
**Purpose**: Data persistence and retrieval

**Database Schema**:

**players**
- id (PRIMARY KEY)
- username (UNIQUE)
- created_at (TIMESTAMP)

**scores**
- id (PRIMARY KEY)
- player_id (FOREIGN KEY)
- level (TEXT)
- score (INTEGER)
- max_score (INTEGER)
- percentage (REAL)
- risk_level (TEXT)
- played_at (TIMESTAMP)

**question_attempts**
- id (PRIMARY KEY)
- player_id (FOREIGN KEY)
- question_id (INTEGER)
- level (TEXT)
- correct (BOOLEAN)
- attempted_at (TIMESTAMP)

**Key Operations**:
- CRUD for players and scores
- Leaderboard queries (top 10)
- Player statistics aggregation
- Category performance analytics

#### E. Utilities Module (`src/utils.py`)
**Purpose**: Helper functions and validation

**Functions**:
- Username validation (security checks)
- Input sanitization (XSS prevention)
- Date/time formatting
- Percentage calculations
- Color coding by performance

### 3. Data Layer

#### A. SQLite Database (`data/cyberquest.db`)
**Why SQLite?**
- ✅ Zero configuration
- ✅ Serverless (no separate process)
- ✅ Perfect for educational projects
- ✅ Fast for < 1000 concurrent users
- ✅ ACID compliant

**Limitations**:
- ❌ Not suitable for massive scale (10,000+ concurrent)
- ❌ Limited concurrency (write locks)

**Future Migration Path**: PostgreSQL or MySQL for production

#### B. Question Bank (`data/questions.json`)
**Why JSON?**
- ✅ Human-readable and editable
- ✅ Easy to version control
- ✅ Simple structure for Q&A format
- ✅ No complex queries needed

**Structure**: Three difficulty levels, 5 questions each

## Data Flow

### Game Play Flow
```
1. User enters username + selects level
   ↓
2. POST /start → Create/get player_id → Store in session
   ↓
3. GET /play/<level> → Load questions → Render game
   ↓
4. User answers questions (client-side)
   ↓
5. POST /submit → Validate → Calculate score → Save to DB
   ↓
6. Store results in session
   ↓
7. GET /results → Retrieve session data → Render charts
```

### Leaderboard Flow
```
1. GET /leaderboard
   ↓
2. Query top 10 scores (ORDER BY score DESC)
   ↓
3. Join with players table
   ↓
4. Format and render
```

## Security Considerations

### Input Validation
- Username: Regex validation, SQL injection prevention
- Answers: Integer validation, bounds checking
- Level: Whitelist validation

### Session Security
- Secure cookies (httponly, secure flags)
- CSRF protection (Flask-WTF recommended for production)
- Session timeout (2 hours)

### XSS Prevention
- Jinja2 auto-escaping enabled
- Additional sanitization in utils.py
- Content Security Policy headers (recommended)

### SQL Injection Prevention
- Parameterized queries (no string concatenation)
- Context managers for connection handling
- Input validation before database operations

## Performance Optimization

### Frontend
- Minified CSS/JS (production build)
- CDN for Chart.js
- Lazy loading for charts
- Browser caching headers

### Backend
- Database connection pooling
- Index on frequently queried columns
- Query optimization (JOIN vs multiple queries)
- Session storage optimization

### Database
```sql
CREATE INDEX idx_scores_player_id ON scores(player_id);
CREATE INDEX idx_scores_score ON scores(score DESC);
CREATE INDEX idx_attempts_player ON question_attempts(player_id);
```

## Scalability Path

### Current Capacity
- **Users**: 100-500 concurrent users
- **Database**: 100,000 score records
- **Response Time**: < 200ms average

### Scale to 10,000 Users
1. **Database**: Migrate to PostgreSQL
2. **Caching**: Add Redis for sessions
3. **Load Balancing**: Multiple Flask instances + Nginx
4. **CDN**: Static assets via CloudFlare
5. **Async**: Convert to async Flask (Quart)

### Scale to 100,000 Users
1. **Microservices**: Separate game logic, leaderboard, auth
2. **Message Queue**: Celery for async score processing
3. **Database Sharding**: By user_id hash
4. **Global Distribution**: Multi-region deployment
5. **Monitoring**: Prometheus + Grafana

## Technology Stack Summary

| Layer | Technology | Purpose |
|-------|-----------|---------|
| **Frontend** | HTML5, CSS3 | Structure & Styling |
| **UI Framework** | Custom CSS | Responsive design |
| **Visualization** | Chart.js | Data charts |
| **Backend Framework** | Flask 3.0 | Web server |
| **Database** | SQLite 3 | Data persistence |
| **Session** | Flask-Session | User state |
| **Language** | Python 3.8+ | Backend logic |
| **Web Server** | Werkzeug | Development server |
| **Production Server** | Gunicorn (recommended) | Production WSGI |

## Deployment Architecture

### Development
```
Flask development server
├── Host: 0.0.0.0
├── Port: 5000
├── Debug: True
└── Auto-reload: Enabled
```

### Production (Recommended)
```
Nginx (Reverse Proxy)
  ↓
Gunicorn (WSGI Server)
  ↓
Flask Application
  ↓
PostgreSQL / SQLite
```

## Conclusion
CyberQuest's architecture is designed for:
- **Simplicity**: Easy to understand and modify
- **Maintainability**: Modular, well-documented code
- **Security**: Input validation, secure sessions
- **Performance**: Optimized queries, efficient rendering
- **Scalability**: Clear path to handle growth
