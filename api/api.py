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

@app.route('/article/add', methods=['POST'])
def create_article():
    post = request.json
    db_list.append(post)
    return jsonify(db_list[-1])

@app.route('/article/update/<int:id>', methods=['PUT'])
def update_article(id):
    post = request.json
    db_list[id] = post
    return jsonify(db_list)


if __name__ == '__main__':
    app.run(debug=True)