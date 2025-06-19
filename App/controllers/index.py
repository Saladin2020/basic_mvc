'''Controllers by me'''
from App.models.crud import CRUD
from flask import render_template
import sys

class Index:
    '''Index'''
    def index(self):
        '''Render the index page.'''
        return render_template('index.html')
