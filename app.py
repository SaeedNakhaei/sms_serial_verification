from flask import Flask
app = Flask(__name__)


def main_page():
    ''' This is the main page of the site
    '''
    return "Hello"
