import os
from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_HOST'] = os.getenv('MYSQL_HOST', 'mysql')
app.config['MYSQL_USER'] = os.getenv('MYSQL_USER', 'root')
app.config['MYSQL_PASSWORD'] = os.getenv('MYSQL_PASSWORD', '')
app.config['MYSQL_DB'] = os.getenv('MYSQL_DB', 'flaskapp')

mysql = MySQL(app)
CORS(app)

@app.route("/test", methods=['POST'])
def test():
    try:
        data = request.get_json()
        Id = data['Id']
        nm = data['nm']
        email = data['nm1']
        
        cur = mysql.connection.cursor()
        query = "INSERT INTO users (id, name, email) VALUES (%s, %s, %s)"
        cur.execute(query, (Id, nm, email))
        mysql.connection.commit()
        
        cur.execute("SELECT * FROM users")
        fetchdata = cur.fetchall()
        cur.close()
        
        return jsonify(fetchdata), 200
    except Exception as e:
        print(f"Error: {e}")
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True, port=5000, host='0.0.0.0')
