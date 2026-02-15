/**
 * Game JavaScript for CyberQuest
 * Handles game interactions and logic
 */

// Helper function to safely get elements
function getElement(id) {
    const element = document.getElementById(id);
    if (!element) {
        console.warn(`Element with id '${id}' not found`);
    }
    return element;
}

// Timer functionality (optional feature)
let gameTimer = null;
let timeElapsed = 0;

function startTimer() {
    gameTimer = setInterval(() => {
        timeElapsed++;
        updateTimerDisplay();
    }, 1000);
}

function stopTimer() {
    if (gameTimer) {
        clearInterval(gameTimer);
    }
}

function updateTimerDisplay() {
    const minutes = Math.floor(timeElapsed / 60);
    const seconds = timeElapsed % 60;
    const timerElement = getElement('timer-display');
    
    if (timerElement) {
        timerElement.textContent = `${minutes.toString().padStart(2, '0')}:${seconds.toString().padStart(2, '0')}`;
    }
}

// Question navigation with validation
function validateCurrentQuestion() {
    const currentCard = document.querySelector('.question-card[style*="display: block"]');
    if (!currentCard) return true;
    
    const selectedOption = currentCard.querySelector('input[type="radio"]:checked');
    return selectedOption !== null;
}

// Highlight unanswered questions
function highlightUnansweredQuestions() {
    const questionCards = document.querySelectorAll('.question-card');
    const unansweredQuestions = [];
    
    questionCards.forEach((card, index) => {
        const questionId = card.dataset.questionId;
        const hasAnswer = card.querySelector('input[type="radio"]:checked') !== null;
        
        if (!hasAnswer) {
            unansweredQuestions.push(index + 1);
        }
    });
    
    return unansweredQuestions;
}

// Keyboard navigation
document.addEventListener('keydown', (event) => {
    if (!window.gameData) return;
    
    const currentQuestion = window.gameData.currentQuestion;
    const totalQuestions = window.gameData.questions.length;
    
    // Left arrow - previous question
    if (event.key === 'ArrowLeft' && currentQuestion > 1) {
        navigateQuestion(currentQuestion - 1);
    }
    
    // Right arrow - next question
    if (event.key === 'ArrowRight' && currentQuestion < totalQuestions) {
        navigateQuestion(currentQuestion + 1);
    }
    
    // Number keys - select option (1-4)
    if (event.key >= '1' && event.key <= '4') {
        const optionIndex = parseInt(event.key) - 1;
        const currentCard = document.querySelector('.question-card[style*="display: block"]');
        
        if (currentCard) {
            const options = currentCard.querySelectorAll('.option-radio');
            if (options[optionIndex]) {
                options[optionIndex].checked = true;
                
                // Trigger change event
                const changeEvent = new Event('change', { bubbles: true });
                options[optionIndex].dispatchEvent(changeEvent);
            }
        }
    }
});

// Visual feedback for option selection
document.addEventListener('DOMContentLoaded', () => {
    const optionLabels = document.querySelectorAll('.option-label');
    
    optionLabels.forEach(label => {
        label.addEventListener('click', function() {
            // Remove active class from siblings
            const container = this.closest('.options-container');
            if (container) {
                container.querySelectorAll('.option-label').forEach(l => {
                    l.classList.remove('active');
                });
            }
            
            // Add active class to clicked option
            this.classList.add('active');
        });
    });
});

// Auto-save functionality to localStorage
function autoSaveProgress() {
    if (!window.gameData) return;
    
    const saveData = {
        level: gameData.level,
        currentQuestion: gameData.currentQuestion,
        answers: gameData.answers,
        timeElapsed: timeElapsed,
        timestamp: Date.now()
    };
    
    try {
        localStorage.setItem('cyberquest_progress', JSON.stringify(saveData));
    } catch (error) {
        console.warn('Could not save progress to localStorage:', error);
    }
}

// Load saved progress
function loadSavedProgress() {
    try {
        const savedData = localStorage.getItem('cyberquest_progress');
        if (!savedData) return null;
        
        const data = JSON.parse(savedData);
        
        // Check if save is less than 2 hours old
        const twoHoursInMs = 2 * 60 * 60 * 1000;
        if (Date.now() - data.timestamp > twoHoursInMs) {
            localStorage.removeItem('cyberquest_progress');
            return null;
        }
        
        return data;
    } catch (error) {
        console.warn('Could not load saved progress:', error);
        return null;
    }
}

// Clear saved progress
function clearSavedProgress() {
    try {
        localStorage.removeItem('cyberquest_progress');
    } catch (error) {
        console.warn('Could not clear saved progress:', error);
    }
}

// Confirmation before leaving page
window.addEventListener('beforeunload', (event) => {
    if (window.gameData && Object.keys(gameData.answers).length > 0) {
        event.preventDefault();
        event.returnValue = 'You have unsaved progress. Are you sure you want to leave?';
        return event.returnValue;
    }
});

// Score animation
function animateScore(element, start, end, duration = 1000) {
    if (!element) return;
    
    const range = end - start;
    const increment = range / (duration / 16);
    let current = start;
    
    const timer = setInterval(() => {
        current += increment;
        
        if ((increment > 0 && current >= end) || (increment < 0 && current <= end)) {
            current = end;
            clearInterval(timer);
        }
        
        element.textContent = Math.round(current);
    }, 16);
}

// Confetti effect for high scores (optional)
function celebrateHighScore() {
    // Simple celebration effect - can be enhanced
    const celebration = document.createElement('div');
    celebration.className = 'celebration-overlay';
    celebration.innerHTML = '🎉🎊🏆';
    celebration.style.cssText = `
        position: fixed;
        top: 50%;
        left: 50%;
        transform: translate(-50%, -50%);
        font-size: 5rem;
        z-index: 10000;
        animation: celebrate 2s ease-out forwards;
    `;
    
    document.body.appendChild(celebration);
    
    setTimeout(() => {
        celebration.remove();
    }, 2000);
}

// Add celebration animation
const style = document.createElement('style');
style.textContent = `
    @keyframes celebrate {
        0% {
            opacity: 0;
            transform: translate(-50%, -50%) scale(0);
        }
        50% {
            opacity: 1;
            transform: translate(-50%, -50%) scale(1.2);
        }
        100% {
            opacity: 0;
            transform: translate(-50%, -50%) scale(1) translateY(-100px);
        }
    }
    
    .option-label.active {
        background: rgba(59, 130, 246, 0.15) !important;
        border-color: var(--primary-color) !important;
    }
`;
document.head.appendChild(style);

// Export functions for use in other scripts
window.CyberQuestGame = {
    validateCurrentQuestion,
    highlightUnansweredQuestions,
    autoSaveProgress,
    loadSavedProgress,
    clearSavedProgress,
    animateScore,
    celebrateHighScore
};

console.log('✅ CyberQuest game.js loaded successfully');
