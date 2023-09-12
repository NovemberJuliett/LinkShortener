# Link Shortener

This code helps shorten your links using the bit.ly service right from the terminal. Additionally, this code helps count clicks on your short links.
## How to install

Python3 should already be installed. Use pip (or pip3, if there is a conflict with Python2) to install dependencies:
```python 
pip install requests, python-dotenv
```

Then you should install enviroment variables:

```python
pip install python-dotenv
```

After this create an .env file in your project directory (or in the root of your project) and store your sensitive information in this file. For example, you have an API token called NEW_TOKEN (you could receive yours from bit.ly site). Replace "your_api_token_here" with your actual API token.
```python 
NEW_TOKEN=your_api_token_here
```

In your Python code, import the load_dotenv function from the dotenv library:
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

## How to use

Open a new terminal window and use the following command:

```python main.py```

To install all project packages at once, use the following command in terminal:

```python
pip install -r requirements.txt
```
