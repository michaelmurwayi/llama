import csv
import openai

import colorama
from colorama import Fore


def load_dataset(file_path):
    dataset = []
    with open(file_path, 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
        for row in reader:
            dataset.append(row)
    return dataset

def preprocess_dataset(dataset):
    processed_data = []
    for row in dataset:
        user_input = row[1:]
        bot_response = row[0]
        processed_data.append((user_input, bot_response))
        # import ipdb;ipdb.set_trace()
    return processed_data


def train_model(prompt, dataset):
    openai.api_key = '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'  # Replace with your OpenAI API key

    # Train the model
    response = openai.Completion.create(
        engine='text-davinci-003',
        prompt=prompt,
        max_tokens=50
    )

    return response.choices[0].text.strip()


# Load the dataset from CSV
csv_file_path = 'resource/dataset.csv'
dataset = load_dataset(csv_file_path)

# Preprocess the dataset
processed_data = preprocess_dataset(dataset)

# User input to initiate the conversation
# user_input = input("User: ")

# Train the model and get the response
# bot_response = train_model(f"User: {user_input}\nBot:", processed_data)

while True:
    # User input to initiate the conversation
    
    user_input = input(Fore.RED + "User: ")

    # Train the model and get the response
    openai_response = train_model(f"User: {user_input}\nBot:", processed_data)
    print(Fore.BLUE + "Bot:", openai_response)