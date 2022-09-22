from main import app

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

# def index():
#     return "OK"

# def setup_routes_for_pages(app):
#     app.add_url_rule("/", view_func=index)

# def setup_routes_for_api(app):
#     app.add_url_rule("/api/test", view_func=index)
