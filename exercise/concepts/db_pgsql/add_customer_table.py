import psycopg2

def connect_to_db():
    connection = psycopg2.connect(user = "postgres",password="admin",host="localhost",database ="postgres")
    cursor = connection.cursor()
    
    create_schema = "CREATE schema customer"
    #cursor.execute(create_schema)

    
    create_cust_table = """CREATE TABLE customers (customer_id SERIAL PRIMARY KEY,
                                            first_name VARCHAR(50) NOT NULL,
                                            last_name VARCHAR(50) NOT NULL,
                                            email VARCHAR(100) UNIQUE);"""
    
    #cursor.execute(create_cust_table)
    

    insert_record = """INSERT INTO customers (first_name, last_name, email, country)
                                         VALUES ("Jackey", "Chan", "Jackey.Chan@hollywood.com", "USA")"""

    records_to_insert = [
        ("Jackey", "Chan", "Jackey.Chan@hollywood.com", "USA"),
        ("Rajini", "Kanth", "Rajini.Kanth@hollywood.com", "INDIA"),

    ]

    #insert_query = "INSERT INTO customers (first_name, last_name, email, country)"\
    #               "VALUES (%s, %s, %s, %s)"


    #cursor.executemany(insert_record,records_to_insert)

    #select_query = "SELECT * FROM Customers"\
    #               "WHERE customer_id = 2;"
    select_query = "select * from Customers"
    cursor.execute(select_query)

    return (cursor.fetchall())    
          

print(connect_to_db())