# Game Design Document

## Game Overview

### Title
**CyberQuest: Cybersecurity Awareness Game for Beginners**

### Genre
Educational Quiz Game with Gamification Elements

### Target Audience
- Age: 13-65 years
- Technical Level: Beginner to Intermediate
- Context: Self-learners, students, employees
- Goal: Learn practical cybersecurity skills

### Core Loop
```
Select Level → Answer Questions → Get Feedback → See Results → Compete on Leaderboard → Play Again
```

## Game Mechanics

### 1. Difficulty Levels

#### Beginner 🌱
- **Audience**: Complete newcomers to cybersecurity
- **Questions**: 5 scenario-based questions
- **Points**: 10 points per question (50 total)
- **Topics**:
  - Basic phishing recognition
  - Simple password strength
  - HTTPS vs HTTP identification
  - Basic social engineering
  - Obvious malware warnings

**Example Question**:
> "You receive an email from 'accounts@paypa1-security.com' asking you to verify your account. What should you do?"

**Design Philosophy**: Build confidence with clear right/wrong answers

#### Intermediate 🔥
- **Audience**: Users with basic security knowledge
- **Questions**: 5 realistic scenario questions
- **Points**: 15 points per question (75 total)
- **Topics**:
  - Advanced phishing (correct branding)
  - 2FA method comparison
  - Public WiFi risks
  - Password breach response
  - Sophisticated social engineering

**Example Question**:
> "A LinkedIn 'recruiter' offers an amazing job but wants you to interview via an unknown video platform. Red flag?"

**Design Philosophy**: Challenge with nuanced scenarios that require critical thinking

#### Advanced 🚀
- **Audience**: Security-aware users wanting mastery
- **Questions**: 5 complex scenario questions
- **Points**: 20 points per question (100 total)
- **Topics**:
  - End-to-end encryption concepts
  - Ransomware incident response
  - Zero-day vulnerabilities
  - Mobile app over-permissioning
  - Breach reporting procedures

**Example Question**:
> "Your computer files are encrypted and a message demands $500 in Bitcoin. What's the BEST response?"

**Design Philosophy**: Test mastery and decision-making under pressure

### 2. Scoring System

#### Point Allocation
- **Beginner**: 10 points per question
- **Intermediate**: 15 points per question
- **Advanced**: 20 points per question

#### Scoring Formula
```
Total Score = Σ (Correct Answers × Question Points)
Percentage = (Total Score / Max Possible Score) × 100
```

#### Risk Level Assessment
Based on percentage score:

| Percentage | Risk Level | Badge | Description |
|-----------|-----------|-------|-------------|
| 90-100% | Cyber Defender 🛡️ | Gold | Security expert |
| 75-89% | Security Aware 🔐 | Blue | Strong knowledge |
| 60-74% | Safe User 🔒 | Yellow | Good foundation |
| 40-59% | At Risk ⚠️ | Orange | Needs improvement |
| 0-39% | High Risk 🚨 | Red | Critical gaps |

### 3. Question Structure

#### Question Components
```json
{
  "id": 1,
  "type": "phishing",
  "question": "Scenario-based question text",
  "options": [
    "Option A",
    "Option B",
    "Option C",
    "Option D"
  ],
  "correct": 1,
  "explanation": "Educational explanation with WHY",
  "points": 10,
  "category": "Phishing Detection"
}
```

#### Question Design Principles

**1. Scenario-Based**
❌ Bad: "What is phishing?"  
✅ Good: "You receive an email from 'CEO' asking for urgent password reset. What do you do?"

**2. Real-World Relevant**
- Use actual examples from recent breaches
- Reference well-known brands (carefully)
- Include current attack vectors

**3. Multiple Plausible Answers**
- All options should seem reasonable
- Avoid obviously wrong "joke" answers
- Test decision-making, not guessing

**4. Educational Feedback**
- Explain WHY correct answer is right
- Explain WHY other answers are wrong
- Provide actionable tips
- Include statistics when relevant

### 4. Progression System

#### Linear Progression (Current)
```
Beginner → Intermediate → Advanced
```

Users can choose any level, but natural progression is encouraged.

#### Achievement System (Future)
- 🥇 First Perfect Score
- 🔥 Streak Master (3 games in a row)
- 📚 All Levels Completed
- 🚀 Speed Demon (Complete in under 5 minutes)
- 🎓 Mentor (Share with 5 friends)

### 5. Feedback Mechanisms

#### Immediate Feedback (Per Question)
- ✅ Correct: Show checkmark, explanation, points earned
- ❌ Incorrect: Show X, correct answer, explanation, 0 points

#### Category Performance
Visual breakdown showing:
- Questions attempted per category
- Correct answers per category
- Percentage accuracy per category
- Color-coded by performance

**Chart**: Stacked bar chart (correct vs incorrect per category)

#### Overall Results
- Total score and percentage
- Risk level assessment
- Risk description and emoji
- Comparison with max possible score

**Chart**: Doughnut chart showing earned vs missed points

#### Personalized Suggestions
Based on weakest categories:
- "Focus on improving your Password Security knowledge"
- "Review educational tips for Social Engineering"
- Priority: High, Medium based on performance

### 6. Leaderboard

#### Ranking System
- **Primary Sort**: Total score (descending)
- **Secondary Sort**: Date (newest first)
- **Display**: Top 10 players

#### Displayed Information
- Rank (🥇🥈🥉 for top 3)
- Player username
- Difficulty level
- Score / Max Score
- Percentage
- Risk level badge
- Date played

#### Leaderboard Strategy
**Encourages**:
- Competition between players
- Replay to improve scores
- Trying higher difficulty levels
- Social sharing of achievements

**Prevents**:
- Usernames are moderated (profanity check in production)
- One account per player (IP tracking in production)
- Cheating detection (time-based analysis in production)

## User Experience Design

### 1. Visual Design

#### Color Palette
```css
Primary:   #3b82f6 (Blue) - Trust, Security
Secondary: #8b5cf6 (Purple) - Premium, Advanced
Success:   #10b981 (Green) - Correct, Safe
Danger:    #ef4444 (Red) - Wrong, Unsafe
Warning:   #f59e0b (Yellow) - Caution
```

#### Typography
- **Font**: Inter (clean, modern, readable)
- **Headings**: Bold, 2-3rem
- **Body**: Regular, 1rem
- **Code/Technical**: Monospace when needed

#### Spacing
- 8px grid system
- Generous padding for readability
- Clear visual hierarchy

### 2. User Flow

#### First-Time User Journey
```
1. Land on homepage
   ↓ See compelling stats about cybercrime
   
2. Read "Why Cyber Awareness Matters"
   ↓ Understand the problem
   
3. Enter username
   ↓ Create identity
   
4. Choose difficulty level
   ↓ See clear descriptions
   
5. Play game
   ↓ Engage with scenarios
   
6. Get immediate feedback
   ↓ Learn from explanations
   
7. See results with charts
   ↓ Visualize performance
   
8. Review detailed feedback
   ↓ Understand mistakes
   
9. Check leaderboard
   ↓ Compare with others
   
10. Play again or share
    ↓ Continuous engagement
```

#### Returning User Journey
```
1. Land on homepage
   ↓ Recognize game
   
2. Enter same username
   ↓ Automatic player recognition
   
3. Try different level
   ↓ Challenge self
   
4. Improve score
   ↓ Apply learned knowledge
   
5. Climb leaderboard
   ↓ Achieve goals
```

### 3. Interaction Design

#### Question Navigation
- **Progress Bar**: Visual indicator of completion
- **Question Counter**: "Question 3 of 5"
- **Navigation Buttons**: Previous / Next
- **Submit Button**: Only on last question
- **Keyboard Shortcuts**: Arrow keys to navigate

#### Answer Selection
- **Radio Buttons**: Single selection only
- **Hover Effect**: Highlight on mouseover
- **Selected State**: Bold border + background color
- **Visual Feedback**: Instant visual change on selection

#### Loading States
- **Starting Game**: "Starting..." on button
- **Submitting Answers**: Overlay with spinner
- **Loading Results**: "Calculating your results..."

### 4. Accessibility

#### Color Contrast
- WCAG AA compliance (4.5:1 minimum)
- Color-blind friendly palette
- Icons + text (not color alone)

#### Keyboard Navigation
- Tab through all interactive elements
- Enter to submit forms
- Arrow keys for question navigation

#### Screen Reader Support
- Semantic HTML (header, main, nav, section)
- ARIA labels for interactive elements
- Alt text for meaningful images

#### Responsive Design
- Mobile-first approach
- Breakpoints: 480px, 768px, 1200px
- Touch-friendly buttons (44px minimum)

## Gamification Elements

### 1. Points & Scores
**Purpose**: Measure performance and provide achievement satisfaction

**Implementation**:
- Visible score counter during gameplay
- Points earned per correct answer
- Total score displayed prominently in results

**Psychological Hook**: Achievement, mastery

### 2. Levels
**Purpose**: Provide structured progression and increasing challenge

**Implementation**:
- Three difficulty tiers
- Clear descriptions of each level
- Visual differentiation (colors, icons)

**Psychological Hook**: Progress, competence

### 3. Badges & Risk Levels
**Purpose**: Categorize players and provide identity/status

**Implementation**:
- 5 risk levels with unique names and emojis
- Visual badges displayed in results
- Leaderboard shows badges

**Psychological Hook**: Status, identity

### 4. Leaderboard
**Purpose**: Foster competition and social comparison

**Implementation**:
- Top 10 players displayed
- Medals for top 3
- Player's own rank highlighted

**Psychological Hook**: Competition, social recognition

### 5. Visual Feedback
**Purpose**: Reinforce correct behavior and maintain engagement

**Implementation**:
- ✅❌ icons for correct/incorrect
- Color-coded results (green = good, red = bad)
- Progress bar fills as game continues
- Animated charts reveal gradually

**Psychological Hook**: Instant gratification, satisfaction

### 6. Educational Rewards
**Purpose**: Make learning feel rewarding, not punishing

**Implementation**:
- Detailed explanations for ALL answers
- "💡 Pro Tip" sections with extra insights
- Learning resources section with curated links

**Psychological Hook**: Curiosity, knowledge acquisition

## Content Strategy

### Question Bank
- **Current**: 15 questions (5 per level)
- **Goal**: 50+ questions (variety and replayability)
- **Updates**: Monthly additions of new scenarios
- **Sources**: Recent breaches, security news, user suggestions

### Educational Content
- **Explanations**: 2-4 sentences per question
- **Tips**: Actionable advice (not just theory)
- **Resources**: Vetted external links (FTC, CISA, etc.)
- **Statistics**: Real data to emphasize importance

### Tone & Voice
- **Friendly**: Approachable, not intimidating
- **Empowering**: "You can do this!" not "You're vulnerable!"
- **Practical**: Focus on actions, not jargon
- **Encouraging**: Celebrate correct answers, support on incorrect

## Technical Design

### Performance Targets
- **Page Load**: < 2 seconds
- **Question Transition**: < 100ms
- **Result Calculation**: < 500ms
- **Chart Rendering**: < 1 second

### Browser Support
- Chrome 90+
- Firefox 88+
- Safari 14+
- Edge 90+
- Mobile Safari/Chrome latest

### Data Privacy
- **No Personal Data**: Only username (pseudonymous)
- **No Tracking**: No analytics/cookies beyond session
- **Local First**: Questions loaded once, client-side logic

## Future Enhancements

### Phase 2 (Short-Term)
- 🎯 More questions (50+ total)
- 🏆 Achievement badges system
- 👥 Multiplayer mode (compete with friends)
- 📊 Personal progress dashboard
- 🔄 Daily challenge mode

### Phase 3 (Medium-Term)
- 🌍 Multi-language support (Spanish, French, Hindi)
- 📱 Mobile app (React Native)
- 🎓 Certificate of completion (PDF download)
- 💬 Community discussion forum
- 📧 Email reminders for practice

### Phase 4 (Long-Term)
- 🧠 AI-powered adaptive difficulty
- 🎮 VR/AR scenarios for immersive learning
- 🏢 Enterprise version with custom content
- 📈 Advanced analytics dashboard for educators
- 🌐 Integration with LMS platforms (Canvas, Moodle)

## Success Metrics

### Engagement Metrics
- Completion rate (target: 70%)
- Average time to complete (target: 10-15 min)
- Replay rate (target: 40%)
- Leaderboard views (target: 50% of players)

### Learning Metrics
- Score improvement on retake (target: 30%+)
- Category performance variation (target: <20% difference)
- Advanced level attempts (target: 25% of players)

### Impact Metrics
- Self-reported behavior changes (survey)
- Knowledge retention (retest after 1 month)
- Real-world application (user stories)

## Conclusion
CyberQuest is designed to make cybersecurity education **fun, engaging, and effective** through:
- Scenario-based learning (not theoretical)
- Immediate feedback (not delayed testing)
- Gamification (not dry training)
- Accessibility (not exclusive to tech experts)

The game balances **education with entertainment**, ensuring players not only learn but also **enjoy the experience** and **want to return**.
