#app.py
from flask import Flask, render_template, jsonify, request
from flask_mysqldb import MySQL,MySQLdb #pip install flask-mysqldb https://github.com/alexferl/flask-mysqldb
 
app = Flask(__name__)
      
app.secret_key = "caircocoders-ednalan"
      
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'mydb'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'
mysql = MySQL(app)
   
@app.route('/')
def main():
    cur = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    result = cur.execute("SELECT * FROM carbrands ORDER BY brand_id")
    carbrands = cur.fetchall()
    return render_template('index.html', carbrands=carbrands)
 
@app.route("/carbrand",methods=["POST","GET"])
def carbrand():  
    cursor = mysql.connection.cursor()
    cur = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    if request.method == 'POST':
        category_id = request.form['category_id'] 
        print(category_id)  
        result = cur.execute("SELECT * FROM carmodels WHERE brand_id = %s ORDER BY car_models ASC", [category_id] )
        carmodel = cur.fetchall()  
        OutputArray = []
        for row in carmodel:
            outputObj = {
                'id': row['brand_id'],
                'name': row['car_models']}
            OutputArray.append(outputObj)
    return jsonify(OutputArray)
     
if __name__ == '__main__':
    app.run(debug=True)