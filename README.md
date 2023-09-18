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
```python 
BITLY_TOKEN=your_api_token_here
```
### How to get
Import the load_dotenv function from the dotenv library:
```python 
from dotenv import load_dotenv
```

Call the load_dotenv() function to load the environment variables from the .env file into your Python environment:

```python
load_dotenv()
```
Now you can access your environment variables using os.environ:
```python
import os

token = os.environ.get("NEW_TOKEN")
```

## Run

Open a new terminal window and use the following command:

```python main.py```

