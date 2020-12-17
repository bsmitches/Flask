from flask import Flask, request
from flask_mysqldb import MySQL
import os

app = Flask(__name__)
app.config.from_envvar('APP_SETTINGS')

mysql = MySQL(app)
@app.route('/')
def home():
    cur = mysql.connection.cursor()
    cur.execute('''SELECT id, title, price FROM items''')
    rv = cur.fetchall()
    stream = os.popen('ec2-metadata --availability-zone')
    location = stream.read()
    returnstr = f'<h1>Instance {location}</h1><table><tr><th>SKU</th><th>Item</th><th>Price</th></tr>'
    for i in rv:
        returnstr += f'<tr><td>{i["id"]}</td><td>{i["title"]}</td><td>${i["price"]}</td></tr>'
    returnstr += '</table><a href="/add">Add another item</a>'
    return returnstr
@app.route('/add', methods=['POST','GET'])
def add():
    if request.method == 'POST':
        cur = mysql.connection.cursor()
        form = request.form
        i, t, p = form['id'], form['title'], form['price']
        cur.execute(f'INSERT INTO items VALUES ({i},"{t}",{p})')
        mysql.connection.commit()
        return f'<h2>Item {t} added</h2><a href="/">View all items</a>'
    else:
        return '''<form method='post'><p><label for=id>ItemId/SKU</label><input type=number name=id><p><label for=title>Title</title><input type=text name=title><p><label for=price>Price</price><input type=number name=price step="0.01"><p><input type=submit value=Add></form>'''
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=80)