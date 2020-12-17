from flask import Flask
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_USER'] = 'dbusername'
app.config['MYSQL_PASSWORD'] = 'dbpassword'
app.config['MYSQL_HOST'] = 'anycompany-aurora-cluster01.cluster-ck28rympaxpe.us-west-2.rds.amazonaws.com'
app.config['MYSQL_DB'] = 'MyDatabase'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'

mysql = MySQL(app)

@app.route('/')
def home():
    cur = mysql.connection.cursor()
    
    cur.execute('''CREATE TABLE items (id INTEGER, title VARCHAR(30), price DOUBLE)''')
    
    # cur.execute('''INSERT INTO items VALUES (1,'Coat',57.98)''')
    # cur.execute('''INSERT INTO items VALUES (2,'Pants',45.99)''')
    # mysql.connection.commit()
    
    # cur.execute('''SELECT id, title, price FROM mysql.items''')
    # rv = cur.fetchall()
    # return str(rv)
    return "done"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=80)
