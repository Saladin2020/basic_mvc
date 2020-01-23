'''Controllers by me'''
from flask import Flask,render_template,request,url_for,session,redirect

class Home:
    ''' Home '''
    def index(self,x):
        ''' index '''
        return render_template('home.html', test=x)

    def test(self):
        ''' test '''
        return render_template('home.html', test=request.args.get('x'))