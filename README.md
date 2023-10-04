# Link Shortener

This code helps shorten your links using the bit.ly service right from the terminal. Additionally, this code helps count clicks on your short links.
## Environment

Python3 should already be installed.

## Requirements

To install all project packages at once, use the following command in terminal:

```python
pip install -r requirements.txt
```
## Environment variables

Create an .env file in your project directory (or in the root of your project) and store your sensitive information in it, using API token.

### How to get

Open this [link](https://dev.bitly.com/) and get your API token following the instructions from Bitly.

Put your token into the .env file and assign its value to the new environment variable. For example:

```python 
BITLY_TOKEN="your_api_token_here"
```

## Run

Open a new terminal window and run the script. Put the link you want to shorten or check right after the run command. For example:

```python main.py https://dvmn.org```