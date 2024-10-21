# Task 1: Your Mood Today
# Importing 'mood_responses' module
import mood_responses

# Collecting user input and responding according to the mood with 'mood_responses' function
mood_input = input("How are you feeling today? ").strip().lower()
print(mood_responses.mood_response(mood_input))