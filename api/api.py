from flask import Flask, jsonify, request

app = Flask(__name__)


db_list = [
    {'title': 'title 1', 'body': 'body 1'},
    {'title': 'title 2', 'body': 'body 2'},
    {'title': 'title 3', 'body': 'body 3'},
    {'title': 'title 4', 'body': 'body 4'},
    {'title': 'title 5', 'body': 'body 5'},
]


@app.route('/articles', methods=['GET'])
def get_articles():
    return jsonify(db_list)

@app.route('/article/<int:id>', methods=['GET'])
def get_article(id):
    return jsonify(db_list[id])


if __name__ == '__main__':
    app.run(debug=True)