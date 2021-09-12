from flask import Flask, jsonify

app = Flask(__name__)


db_list = [
    {'title1': 'body1'},
    {'title2': 'body2'},
    {'title3': 'body3'},
    {'title4': 'body4'},
    {'title5': 'body5'},
]


@app.route('/articles', methods=['GET'])
def get_articles():
    return jsonify(db_list)

@app.route('/article/<int:id>', methods=['GET'])
def get_article(id):
    return jsonify(db_list[int(id)])


if __name__ == '__main__':
    app.run(debug=True)