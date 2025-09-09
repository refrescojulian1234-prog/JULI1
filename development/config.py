"""
Configuration file for Julian's Math Test Program
Contains all configurable settings and constants.
"""

import os
from pathlib import Path

# Application Settings
APP_NAME = "Julian's Math Test Program"
VERSION = "2.0.0-dev"
AUTHOR = "Julian"

# File Paths
BASE_DIR = Path(__file__).parent
DATA_DIR = BASE_DIR / "data"
RESULTS_FILE = DATA_DIR / "test_results.json"
USER_PROFILES_FILE = DATA_DIR / "user_profiles.json"

# Create data directory if it doesn't exist
DATA_DIR.mkdir(exist_ok=True)

# Difficulty Configurations
DIFFICULTIES = {
    '1': {
        'name': 'Beginner',
        'questions': 5,
        'min_num': 1,
        'max_num': 10,
        'operations': ['+', '-'],
        'description': '5 questions, numbers 1-10'
    },
    'b': {
        'name': 'Beginner',
        'questions': 5,
        'min_num': 1,
        'max_num': 10,
        'operations': ['+', '-'],
        'description': '5 questions, numbers 1-10'
    },
    '2': {
        'name': 'Easy',
        'questions': 8,
        'min_num': 5,
        'max_num': 20,
        'operations': ['+', '-'],
        'description': '8 questions, numbers 5-20'
    },
    'e': {
        'name': 'Easy',
        'questions': 8,
        'min_num': 5,
        'max_num': 20,
        'operations': ['+', '-'],
        'description': '8 questions, numbers 5-20'
    },
    '3': {
        'name': 'Medium',
        'questions': 10,
        'min_num': 10,
        'max_num': 35,
        'operations': ['+', '-', '*'],
        'description': '10 questions, numbers 10-35, includes multiplication'
    },
    'm': {
        'name': 'Medium',
        'questions': 10,
        'min_num': 10,
        'max_num': 35,
        'operations': ['+', '-', '*'],
        'description': '10 questions, numbers 10-35, includes multiplication'
    },
    '4': {
        'name': 'Hard',
        'questions': 12,
        'min_num': 15,
        'max_num': 50,
        'operations': ['+', '-', '*'],
        'description': '12 questions, numbers 15-50, includes multiplication'
    },
    'h': {
        'name': 'Hard',
        'questions': 12,
        'min_num': 15,
        'max_num': 50,
        'operations': ['+', '-', '*'],
        'description': '12 questions, numbers 15-50, includes multiplication'
    },
    '5': {
        'name': 'Expert',
        'questions': 15,
        'min_num': 20,
        'max_num': 99,
        'operations': ['+', '-', '*'],
        'description': '15 questions, numbers 20-99, includes multiplication'
    },
    'x': {
        'name': 'Expert',
        'questions': 15,
        'min_num': 20,
        'max_num': 99,
        'operations': ['+', '-', '*'],
        'description': '15 questions, numbers 20-99, includes multiplication'
    }
}

# Scoring Settings
BASE_POINTS = 10
MAX_TIME_BONUS = 5
TIME_BONUS_THRESHOLD = 5  # seconds

# Performance Ratings
PERFORMANCE_RATINGS = {
    90: "🌟 EXCELLENT!",
    80: "👍 VERY GOOD!",
    70: "👌 GOOD!",
    60: "📈 FAIR",
    50: "📚 NEEDS PRACTICE",
    0: "🔄 KEEP TRYING!"
}

# UI Settings
SEPARATOR_LENGTH = 60
QUESTION_SEPARATOR_LENGTH = 40