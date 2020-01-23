from App.controllers import *
class Route:
    def map(self, app):
        app.add_url_rule('/', 'index', Index().index)

        app.add_url_rule('/home/<x>', 'home', Home().index)
        app.add_url_rule('/home/test', 'home/test', Home().test, methods=['GET','POST'])

        app.add_url_rule('/analyse', 'analyse', Analyse().index, methods=['POST'])

        return app
