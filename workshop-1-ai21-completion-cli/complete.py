import os
import argparse
from pathlib import Path

import requests
from dotenv import load_dotenv

DOTENV_PATH = Path(__file__).parent / ".env"
load_dotenv(DOTENV_PATH)
AI21_API_KEY = os.getenv("AI21_API_KEY")


def complete(prompt, model="j1-jumbo", max_tokens=64):
    api_url = f"https://api.ai21.com/studio/v1/{model}/complete"
    headers = {
        "Authorization": f"Bearer {AI21_API_KEY}",
        "Content-Type": "application/json",
    }
    data = {
        "prompt": prompt,
        "maxTokens": max_tokens,
    }
    response = requests.post(api_url, json=data, headers=headers)
    if response.status_code == 200:
        completion = response.json()["completions"][0]["data"]["text"]
        print(prompt + completion)
    else:
        print("Error fetching")
        print(response.text)


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
    parser.add_argument("--max-tokens", type=int, default=64, help="Max tokens")
    args = parser.parse_args()
    if args.prompt:
        complete(args.prompt, args.model, args.max_tokens)
