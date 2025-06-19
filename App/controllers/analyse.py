'''Controllers by me'''
# Add this imports
from flask import Flask, render_template, request, url_for, session, redirect
from App.models.cwordurl import Cwordurl
from App.lib.myplot import Myplot


class Analyse:
    ''' Analyse '''

    def index(self):
        ''' index '''
        param = request.form.to_dict()
        if 'url' not in param or not param['url']:
            return redirect(url_for('index'))

        w = Cwordurl(param['url'])
        wd = {}
        wd['isword'] = w.get_isword()
        wd['notword'] = w.get_notword()

        wd['img0'] = Myplot(w.get_isword()).plot()
        wd['img1'] = Myplot(w.get_notword()).plot()

        return render_template('analyse.html', wd=wd)
