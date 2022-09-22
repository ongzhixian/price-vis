from flask import Flask, render_template

def index():
    return render_template('index.html')

def setup_pages(app):
    app.add_url_rule("/", view_func=index)

def api_test():
    return "api test"

def setup_api(app):
    app.add_url_rule("/api/test", view_func=api_test)

def setup_web_application():
    app = Flask(__name__, static_url_path='/', static_folder='wwwroot', template_folder='templates')
    setup_api(app)
    setup_pages(app)
    return app