# Creating lists with words that signify each mood
happy_mood = ['happy', 'great', 'good', 'delighted', 'joyful']
sad_mood = ['sad', 'unhappy', 'not good', 'bad', 'depressed']
excited_mood = ['excited', 'ecstatic', 'elated']

# Defining a function that returns a custom message for each mood
def mood_response(mood):
    if mood in happy_mood:
        return "You have made my day!"
    elif mood in sad_mood:
        return "There's a silver lining somewhere!"
    elif mood in excited_mood:
        return "I'm excited to hear that you are excited!"
    else:
        return f"'{mood}' mood was not recognized. Please try again."