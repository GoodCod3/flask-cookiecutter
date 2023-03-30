from flask import Flask

app = Flask(__name__)


@app.route('/version', methods=(['GET']))
def version():
    return "pro-20230328v1"


if __name__ == '__main__':
    app.run(host='0.0.0.0')
