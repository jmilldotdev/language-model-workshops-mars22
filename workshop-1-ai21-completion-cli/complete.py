import os
import argparse
import requests
from dotenv import load_dotenv

DOTENV_PATH = ".env"
load_dotenv(DOTENV_PATH)
AI21_API_KEY = os.getenv("AI21_API_KEY")


def complete(prompt, model="j1-jumbo"):
    print(prompt)
    print(model)
    api_url = f"https://api.ai21.com/studio/v1/{model}/complete"
    headers = {
        "Authorization": f"Bearer {AI21_API_KEY}",
        "Content-Type": "application/json",
    }
    data = {
        "prompt": prompt,
    }
    response = requests.post(api_url, json=data, headers=headers)
    print(response.json())
    if response.status_code == 200:
        completion = response.json()["completions"][0]["data"]["text"]
        print(prompt + completion)
    else:
        print("Error fetching")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="AI21 Completion CLI")
    parser.add_argument("prompt", type=str, help="Prompt to complete")
    parser.add_argument(
        "--model",
        type=str,
        choices=["j1-jumbo", "j1-large"],
        default="ji-jumbo",
        help="Model to use",
    )
    args = parser.parse_args()
    if args.prompt:
        complete(args.prompt, args.model)
