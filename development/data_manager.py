"""
Data management module for Julian's Math Test Program
Handles saving and loading of test results and user profiles.
"""

import json
import os
from datetime import datetime
from typing import Dict, List, Any, Optional
from pathlib import Path
from config import RESULTS_FILE, USER_PROFILES_FILE


class DataManager:
    """Manages data persistence for test results and user profiles."""
    
    def __init__(self):
        """Initialize the data manager."""
        self.results_file = RESULTS_FILE
        self.profiles_file = USER_PROFILES_FILE
        
        # Ensure data directory exists
        self.results_file.parent.mkdir(exist_ok=True)
    
    def save_test_result(self, result_data: Dict[str, Any]) -> bool:
        """
        Save a test result to the results file.
        
        Args:
            result_data: Dictionary containing test result data
            
        Returns:
            True if saved successfully, False otherwise
        """
        try:
            # Load existing results
            results = self.load_test_results()
            
            # Add timestamp if not present
            if 'timestamp' not in result_data:
                result_data['timestamp'] = datetime.now().isoformat()
            
            # Add the new result
            results.append(result_data)
            
            # Save back to file
            with open(self.results_file, 'w') as f:
                json.dump(results, f, indent=2, default=str)
            
            return True
            
        except Exception as e:
            print(f"❌ Error saving test result: {e}")
            return False
    
    def load_test_results(self) -> List[Dict[str, Any]]:
        """
        Load all test results from file.
        
        Returns:
            List of test result dictionaries
        """
        try:
            if self.results_file.exists():
                with open(self.results_file, 'r') as f:
                    return json.load(f)
            return []
            
        except Exception as e:
            print(f"❌ Error loading test results: {e}")
            return []
    
    def get_user_statistics(self, username: Optional[str] = None) -> Dict[str, Any]:
        """
        Get statistics for a specific user or all users.
        
        Args:
            username: Username to get stats for (None for all users)
            
        Returns:
            Dictionary containing statistics
        """
        results = self.load_test_results()
        
        if username:
            results = [r for r in results if r.get('username') == username]
        
        if not results:
            return {
                'total_tests': 0,
                'average_score': 0,
                'average_accuracy': 0,
                'best_score': 0,
                'total_questions': 0,
                'total_correct': 0
            }
        
        total_tests = len(results)
        total_score = sum(r.get('final_score', 0) for r in results)
        total_accuracy = sum(r.get('accuracy_percentage', 0) for r in results)
        best_score = max(r.get('final_score', 0) for r in results)
        total_questions = sum(r.get('questions_count', 0) for r in results)
        total_correct = sum(r.get('correct_answers', 0) for r in results)
        
        return {
            'total_tests': total_tests,
            'average_score': round(total_score / total_tests, 1),
            'average_accuracy': round(total_accuracy / total_tests, 1),
            'best_score': best_score,
            'total_questions': total_questions,
            'total_correct': total_correct,
            'last_test_date': results[-1].get('timestamp', 'Unknown')
        }
    
    def save_user_profile(self, username: str, profile_data: Dict[str, Any]) -> bool:
        """
        Save or update a user profile.
        
        Args:
            username: Username
            profile_data: Profile data dictionary
            
        Returns:
            True if saved successfully, False otherwise
        """
        try:
            profiles = self.load_user_profiles()
            profiles[username] = {
                **profile_data,
                'last_updated': datetime.now().isoformat()
            }
            
            with open(self.profiles_file, 'w') as f:
                json.dump(profiles, f, indent=2, default=str)
            
            return True
            
        except Exception as e:
            print(f"❌ Error saving user profile: {e}")
            return False
    
    def load_user_profiles(self) -> Dict[str, Dict[str, Any]]:
        """
        Load all user profiles from file.
        
        Returns:
            Dictionary of user profiles
        """
        try:
            if self.profiles_file.exists():
                with open(self.profiles_file, 'r') as f:
                    return json.load(f)
            return {}
            
        except Exception as e:
            print(f"❌ Error loading user profiles: {e}")
            return {}
    
    def get_leaderboard(self, limit: int = 10) -> List[Dict[str, Any]]:
        """
        Get leaderboard of top scores.
        
        Args:
            limit: Maximum number of entries to return
            
        Returns:
            List of top score entries
        """
        results = self.load_test_results()
        
        # Sort by score (descending) and take top entries
        sorted_results = sorted(results, 
                              key=lambda x: x.get('final_score', 0), 
                              reverse=True)
        
        return sorted_results[:limit]