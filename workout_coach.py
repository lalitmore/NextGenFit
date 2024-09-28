import os
import requests

# Set up the Gemini API key
API_KEY = os.getenv('GEMINI_API_KEY')  # Replace with your actual Gemini API key
API_URL = 'https://gemini.googleapis.com/v1/chat'

# Function to interact with the Gemini API and generate workouts
def get_workout_recommendation(prompt):
    headers = {
        'Authorization': f'Bearer {API_KEY}',
        'Content-Type': 'application/json'
    }

    # Request payload
    data = {
        "prompt": prompt,  # User's query for personalized workout
        "model": "gemini-v1",  # Replace with the correct Gemini model version
        "max_tokens": 200  # Adjust the response length as needed
    }

    # Send the request to the Gemini API
    response = requests.post(API_URL, json=data, headers=headers)

    if response.status_code == 200:
        result = response.json()
        # Extract the generated workout plan from the response
        return result['choices'][0]['text']
    else:
        return f"Error: {response.status_code}, {response.text}"

# Get user inputs
def get_user_inputs():
    print("Welcome to the AI-Powered Workout Coach!")
    fitness_goal = input("What is your fitness goal? (e.g., weight loss, muscle gain, etc.): ")
    fitness_level = input("What is your fitness level? (beginner, intermediate, advanced): ")
    equipment = input("What equipment do you have available? (e.g., bodyweight, dumbbells, etc.): ")
    workout_duration = input("How much time do you have for a workout? (e.g., 20 minutes, 30 minutes): ")
    health_restrictions = input("Do you have any health restrictions? (e.g., back pain, knee issues): ")

    # Construct the workout prompt based on user inputs
    prompt = f"My fitness goal is {fitness_goal}. I am at {fitness_level} level. \
              I have access to {equipment} and I can work out for {workout_duration}. \
              I have {health_restrictions} as a restriction. Please recommend a workout plan."

    return prompt

# Main function to run the AI workout coach
if __name__ == "__main__":
    # Get user inputs
    prompt = get_user_inputs()
    
    # Get a workout plan from the Gemini API
    workout_plan = get_workout_recommendation(prompt)
    
    # Display the generated workout plan
    print("\nHere is your personalized workout plan:\n")
    print(workout_plan)
