import click
import requests
import json

@click.command()
@click.option("--api-key", help="Your api key for ChatGPT")
@click.option("--prompt", prompt="What can I do for you today?", help="Write a function in Python to find even numbers")
@click.option("--file", help="File to write ChatGPT response to")
@click.option("--max-tokens", default=7, help="The maximum number of tokens to generate in the completion")
@click.option("--temperature", default=0, help="What sampling temperature to use")

def chat(api_key, prompt, file, max_tokens, temperature):
    """Make an api call to ChatGPT and write the respone to a file"""
    if api_key is None:
        raise click.ClickException("missing api key. Please pass an api key via --api-key")
    else:
        api_url = "https://api.openai.com/v1/completions"
        headers = {"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"}
        data = {"model": "text-davinci-003", "prompt": f"{prompt}", "temperature": temperature, "max_tokens": max_tokens}

        try:
            response = requests.post(api_url, headers=headers, json=data)
        except requests.exceptions as err:
            raise click.ClickException(err)

        json_response = response.json()

        if file is None:
            click.echo(json_response["choices"][0]["text"])
        else:
            with open(file, 'w') as f:
                f.write(json_response["choices"][0]["text"])
                click.echo(json_response)
                click.echo(f"Text written to {file}")

