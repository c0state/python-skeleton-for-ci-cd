from flask import Flask, render_template, send_from_directory
app = Flask(__name__)


@app.route('/js/<path:path>')
def send_js(path):
    return send_from_directory(u'templates/js', path)


@app.route('/css/<path:path>')
def send_css(path):
    return send_from_directory(u'templates/css', path)


@app.route('/fonts/<path:path>')
def send_fonts(path):
    return send_from_directory(u'templates/fonts', path)


@app.route('/img/<path:path>')
def send_img(path):
    return send_from_directory(u'templates/img', path)


@app.route('/')
@app.route('/index.html')
def root_index_page():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
