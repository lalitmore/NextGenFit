import os
import requests

import google.generativeai as genai
import os


def get_workout_recommendation(prompt):
    
    genai.configure(api_key=os.environ["API_KEY"])
    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content(prompt)
    #print(response.text)

    return response.text

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