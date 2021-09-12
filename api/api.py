from flask import Flask, jsonify, request
import pymysql

app = Flask(__name__)
app.config['JSON_SQRT_KEYS'] = False


def getConnection():
    return pymysql.connect(
        host='localhost',
        user='root',
        password='Kei19971018?',
        db='shop_app',
        cursorclass=pymysql.cursors.DictCursor,
    )


@app.route('/items', methods=['GET'])
def get_items():
    connection = getConnection()
    try:
        with connection.cursor() as cursor:
            sql = 'SELECT * FROM items'
            cursor.execute(sql)
            items = cursor.fetchall()
    finally:
        connection.close()

    return jsonify({
        'status': 'OK',
        'items': items
    })

@app.route('/item/<int:id>', methods=['GET'])
def get_item(id):
    connection = getConnection()
    try:
        with connection.cursor() as cursor:
            sql = 'SELECT * FROM items WHERE id = %s'
            cursor.execute(sql, id)
            item = cursor.fetchone()
    finally:
        connection.close()

    return jsonify({
        'status': 'OK',
        'items': item
    })

@app.route('/item/add', methods=['POST'])
def create_item():
    item = request.json
    item_cost = item.get('cost')
    item_name = item.get('name')
    item_stock = item.get('stock')

    connection = getConnection()
    try:
        with connection.cursor() as cursor:
            sql = 'INSERT INTO items (name, cost, stock) VALUES (%s, %s, %s)'
            cursor.execute(sql, (item_name, item_cost, item_stock))
    finally:
        connection.commit()
        connection.close()

    return 'success'

@app.route('/item/update/<int:id>', methods=['PUT'])
def update_item(id):
    item = request.json
    item_cost = item.get('cost')
    item_name = item.get('name')
    item_stock = item.get('stock')

    connection = getConnection()
    try:
        with connection.cursor() as cursor:
            sql = 'UPDATE items SET name = %s, cost = %s, stock = %s WHERE id = %s'
            cursor.execute(sql, (item_name, item_cost, item_stock, id))
    finally:
        connection.commit()
        connection.close()

    return 'success'

@app.route('/item/delete/<int:id>', methods=['DELETE'])
def delete_item(id):
    connection = getConnection()
    try:
        with connection.cursor() as cursor:
            sql = 'DELETE FROM items WHERE id = %s'
            cursor.execute(sql, id)
    finally:
        connection.commit()
        connection.close()

    return 'success'


if __name__ == '__main__':
    app.run(debug=True)