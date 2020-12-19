# 기본탬플릿

from flask import Flask


app = Flask(__name__)


@app.route('/')
def home():
        return "hello Flask Home page"


if __name__ == '__main__':
    app.run(debug=True)

