This workshop includes a simple completions script powered by [AI21](https://studio.ai21.com/docs/api/)

To run this completion script:

1. Obtain an API key from [AI21](https://studio.ai21.com/account) by signing up for an account on their site and filling out the access form.
2. Copy the `.env.example` file in this folder and rename it `.env`. Add your AI21 API key.
3. Install the required packages, `pip install -r requirements.txt`
4. Run `python complete.py "My super awesome prompt"`. Optionally provide `--model` and `--max-tokens` arguments.