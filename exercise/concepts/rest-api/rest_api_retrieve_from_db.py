from flask import Flask
#from concepts.db_pgsql import add_customer_table
import psycopg2

app = Flask(__name__)

@app.route('/customers', methods=['GET'])
def get_customers():

  connection = psycopg2.connect(user = "postgres",password="admin",host="localhost",database ="postgres")
  cursor = connection.cursor()

  select_query = "select * from Customers"
  cursor.execute(select_query)
  
  return(cursor.fetchall())

  #return add_customer_table.connect_to_db()

app.run(port=8005, debug=True)

