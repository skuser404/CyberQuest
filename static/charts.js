/**
 * Charts JavaScript for CyberQuest
 * Handles Chart.js visualizations and data presentation
 */

// Chart color schemes
const CHART_COLORS = {
    correct: {
        background: 'rgba(16, 185, 129, 0.6)',
        border: 'rgba(16, 185, 129, 1)'
    },
    incorrect: {
        background: 'rgba(239, 68, 68, 0.6)',
        border: 'rgba(239, 68, 68, 1)'
    },
    primary: {
        background: 'rgba(59, 130, 246, 0.6)',
        border: 'rgba(59, 130, 246, 1)'
    },
    secondary: {
        background: 'rgba(139, 92, 246, 0.6)',
        border: 'rgba(139, 92, 246, 1)'
    }
};

// Default Chart.js configuration
Chart.defaults.font.family = "'Inter', sans-serif";
Chart.defaults.font.size = 13;
Chart.defaults.color = '#374151';

/**
 * Create a category performance chart
 */
function createCategoryChart(canvasId, categoryData) {
    const ctx = document.getElementById(canvasId);
    if (!ctx) {
        console.warn(`Canvas element '${canvasId}' not found`);
        return null;
    }
    
    const categories = Object.keys(categoryData);
    const correctCounts = categories.map(cat => categoryData[cat].correct);
    const totalCounts = categories.map(cat => categoryData[cat].total);
    const incorrectCounts = totalCounts.map((total, i) => total - correctCounts[i]);
    const percentages = categories.map(cat => categoryData[cat].percentage);
    
    return new Chart(ctx, {
        type: 'bar',
        data: {
            labels: categories,
            datasets: [{
                label: 'Correct Answers',
                data: correctCounts,
                backgroundColor: CHART_COLORS.correct.background,
                borderColor: CHART_COLORS.correct.border,
                borderWidth: 2
            }, {
                label: 'Incorrect Answers',
                data: incorrectCounts,
                backgroundColor: CHART_COLORS.incorrect.background,
                borderColor: CHART_COLORS.incorrect.border,
                borderWidth: 2
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            scales: {
                x: {
                    stacked: true,
                    grid: {
                        display: false
                    },
                    ticks: {
                        autoSkip: false,
                        maxRotation: 45,
                        minRotation: 0
                    }
                },
                y: {
                    stacked: true,
                    beginAtZero: true,
                    ticks: {
                        stepSize: 1,
                        precision: 0
                    },
                    grid: {
                        color: 'rgba(0, 0, 0, 0.05)'
                    }
                }
            },
            plugins: {
                legend: {
                    display: true,
                    position: 'top',
                    labels: {
                        padding: 15,
                        usePointStyle: true
                    }
                },
                tooltip: {
                    backgroundColor: 'rgba(0, 0, 0, 0.8)',
                    padding: 12,
                    cornerRadius: 8,
                    titleFont: {
                        size: 14,
                        weight: 'bold'
                    },
                    bodyFont: {
                        size: 13
                    },
                    callbacks: {
                        afterLabel: function(context) {
                            const categoryIndex = context.dataIndex;
                            return `Accuracy: ${percentages[categoryIndex]}%`;
                        }
                    }
                }
            },
            animation: {
                duration: 1000,
                easing: 'easeInOutQuart'
            }
        }
    });
}

/**
 * Create a doughnut chart for score distribution
 */
function createScoreDonut(canvasId, score, maxScore) {
    const ctx = document.getElementById(canvasId);
    if (!ctx) {
        console.warn(`Canvas element '${canvasId}' not found`);
        return null;
    }
    
    const missed = maxScore - score;
    const percentage = ((score / maxScore) * 100).toFixed(1);
    
    return new Chart(ctx, {
        type: 'doughnut',
        data: {
            labels: ['Earned Points', 'Missed Points'],
            datasets: [{
                data: [score, missed],
                backgroundColor: [
                    CHART_COLORS.correct.background,
                    CHART_COLORS.incorrect.background
                ],
                borderColor: [
                    CHART_COLORS.correct.border,
                    CHART_COLORS.incorrect.border
                ],
                borderWidth: 2
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            cutout: '70%',
            plugins: {
                legend: {
                    position: 'bottom',
                    labels: {
                        padding: 20,
                        usePointStyle: true
                    }
                },
                tooltip: {
                    backgroundColor: 'rgba(0, 0, 0, 0.8)',
                    padding: 12,
                    cornerRadius: 8,
                    callbacks: {
                        label: function(context) {
                            const label = context.label || '';
                            const value = context.parsed;
                            const total = context.dataset.data.reduce((a, b) => a + b, 0);
                            const percent = ((value / total) * 100).toFixed(1);
                            return `${label}: ${value} (${percent}%)`;
                        }
                    }
                }
            },
            animation: {
                animateRotate: true,
                animateScale: true
            }
        },
        plugins: [{
            id: 'centerText',
            afterDraw: function(chart) {
                const ctx = chart.ctx;
                const centerX = (chart.chartArea.left + chart.chartArea.right) / 2;
                const centerY = (chart.chartArea.top + chart.chartArea.bottom) / 2;
                
                ctx.save();
                ctx.font = 'bold 32px Inter';
                ctx.fillStyle = '#374151';
                ctx.textAlign = 'center';
                ctx.textBaseline = 'middle';
                ctx.fillText(`${percentage}%`, centerX, centerY);
                ctx.restore();
            }
        }]
    });
}

/**
 * Create a radar chart for multi-dimensional skill assessment
 */
function createSkillRadar(canvasId, categoryData) {
    const ctx = document.getElementById(canvasId);
    if (!ctx) {
        console.warn(`Canvas element '${canvasId}' not found`);
        return null;
    }
    
    const categories = Object.keys(categoryData);
    const percentages = categories.map(cat => categoryData[cat].percentage);
    
    return new Chart(ctx, {
        type: 'radar',
        data: {
            labels: categories,
            datasets: [{
                label: 'Your Performance',
                data: percentages,
                backgroundColor: 'rgba(59, 130, 246, 0.2)',
                borderColor: 'rgba(59, 130, 246, 1)',
                borderWidth: 2,
                pointBackgroundColor: 'rgba(59, 130, 246, 1)',
                pointBorderColor: '#fff',
                pointBorderWidth: 2,
                pointRadius: 5,
                pointHoverRadius: 7
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            scales: {
                r: {
                    beginAtZero: true,
                    max: 100,
                    ticks: {
                        stepSize: 20,
                        callback: function(value) {
                            return value + '%';
                        }
                    },
                    grid: {
                        color: 'rgba(0, 0, 0, 0.1)'
                    },
                    angleLines: {
                        color: 'rgba(0, 0, 0, 0.1)'
                    },
                    pointLabels: {
                        font: {
                            size: 12
                        }
                    }
                }
            },
            plugins: {
                legend: {
                    display: false
                },
                tooltip: {
                    backgroundColor: 'rgba(0, 0, 0, 0.8)',
                    padding: 12,
                    cornerRadius: 8,
                    callbacks: {
                        label: function(context) {
                            return `Accuracy: ${context.parsed.r}%`;
                        }
                    }
                }
            },
            animation: {
                duration: 1500,
                easing: 'easeInOutQuart'
            }
        }
    });
}

/**
 * Create a line chart for progress over time (if historical data available)
 */
function createProgressLine(canvasId, historicalData) {
    const ctx = document.getElementById(canvasId);
    if (!ctx) {
        console.warn(`Canvas element '${canvasId}' not found`);
        return null;
    }
    
    const dates = historicalData.map(d => d.date);
    const scores = historicalData.map(d => d.percentage);
    
    return new Chart(ctx, {
        type: 'line',
        data: {
            labels: dates,
            datasets: [{
                label: 'Score Percentage',
                data: scores,
                backgroundColor: 'rgba(59, 130, 246, 0.1)',
                borderColor: 'rgba(59, 130, 246, 1)',
                borderWidth: 3,
                fill: true,
                tension: 0.4,
                pointBackgroundColor: 'rgba(59, 130, 246, 1)',
                pointBorderColor: '#fff',
                pointBorderWidth: 2,
                pointRadius: 5,
                pointHoverRadius: 7
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            scales: {
                x: {
                    grid: {
                        display: false
                    }
                },
                y: {
                    beginAtZero: true,
                    max: 100,
                    ticks: {
                        stepSize: 20,
                        callback: function(value) {
                            return value + '%';
                        }
                    },
                    grid: {
                        color: 'rgba(0, 0, 0, 0.05)'
                    }
                }
            },
            plugins: {
                legend: {
                    display: false
                },
                tooltip: {
                    backgroundColor: 'rgba(0, 0, 0, 0.8)',
                    padding: 12,
                    cornerRadius: 8
                }
            },
            animation: {
                duration: 1500,
                easing: 'easeInOutQuart'
            }
        }
    });
}

// Export chart creation functions
window.CyberQuestCharts = {
    createCategoryChart,
    createScoreDonut,
    createSkillRadar,
    createProgressLine,
    CHART_COLORS
};

console.log('✅ CyberQuest charts.js loaded successfully');
