'''Controllers by me'''
from App.models.crud import CRUD
from flask import render_template
import sys

class Index:
    '''Index'''
    def index(self):
        '''Returns argument a is squared.'''
        #crud = CRUD()
        return render_template('index.html')