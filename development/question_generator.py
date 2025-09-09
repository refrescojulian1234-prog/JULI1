"""
Question generator module for Julian's Math Test Program
Handles creation and validation of math questions.
"""

import random
from typing import Tuple, List


class QuestionGenerator:
    """Generates math questions based on specified parameters."""
    
    def __init__(self, min_num: int, max_num: int, operations: List[str]):
        """
        Initialize the question generator.
        
        Args:
            min_num: Minimum number to use in questions
            max_num: Maximum number to use in questions
            operations: List of allowed operations
        """
        self.min_num = min_num
        self.max_num = max_num
        self.operations = operations
    
    def generate_question(self, difficulty_modifier: float = 1.0) -> Tuple[str, int]:
        """
        Generate a single math question.
        
        Args:
            difficulty_modifier: Multiplier to adjust difficulty (1.0 = normal)
            
        Returns:
            Tuple of (question_string, correct_answer)
        """
        # Adjust number range based on difficulty modifier
        adjusted_min = max(1, int(self.min_num * difficulty_modifier))
        adjusted_max = int(self.max_num * difficulty_modifier)
        
        num1 = random.randint(adjusted_min, adjusted_max)
        num2 = random.randint(adjusted_min, adjusted_max)
        operation = random.choice(self.operations)
        
        # Handle specific operation rules
        if operation == '-':
            # Ensure subtraction doesn't result in negative numbers
            if num1 < num2:
                num1, num2 = num2, num1
        elif operation == '*':
            # Keep multiplication results reasonable
            num1 = random.randint(adjusted_min, min(12, adjusted_max))
            num2 = random.randint(2, min(12, adjusted_max))
        
        question = f"{num1} {operation} {num2}"
        correct_answer = self._calculate_answer(num1, num2, operation)
        
        return question, correct_answer
    
    def _calculate_answer(self, num1: int, num2: int, operation: str) -> int:
        """Calculate the correct answer for a question."""
        if operation == '+':
            return num1 + num2
        elif operation == '-':
            return num1 - num2
        elif operation == '*':
            return num1 * num2
        else:
            raise ValueError(f"Unsupported operation: {operation}")
    
    def generate_challenge_question(self) -> Tuple[str, int]:
        """
        Generate a challenge question (harder than normal).
        
        Returns:
            Tuple of (question_string, correct_answer)
        """
        return self.generate_question(difficulty_modifier=1.5)
    
    def validate_answer(self, user_answer: str, correct_answer: int) -> bool:
        """
        Validate user's answer.
        
        Args:
            user_answer: User's input answer
            correct_answer: The correct answer
            
        Returns:
            True if answer is correct, False otherwise
        """
        try:
            return int(user_answer) == correct_answer
        except (ValueError, TypeError):
            return False