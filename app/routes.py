from app import app
@app.route('/index')
def index():
    x=15
    y=5
    return str(x-y)
