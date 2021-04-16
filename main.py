
from app import create_app
from flask import render_template
import eventlet

app = create_app()




@app.route('/')
def index():
    return render_template('document.html')


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=1, port='5000')




    # from eventlet import wsgi
    #
    # wsgi.server(eventlet.listen(('', 5000)), app)

