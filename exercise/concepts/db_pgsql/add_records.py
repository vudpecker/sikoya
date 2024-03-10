import psycopg2

def connect_to_db():
    connection = psycopg2.connect(user = 'postgres',password='admin',host='localhost',database ='postgres')
    cursor = connection.cursor()



    create_schema = "CREATE schema buildPPL"
    cursor.execute(create_schema)
   

    create_pipeline_table = """CREATE TABLE buildPPL.buildjobs (
                                job_id integer NOT NULL,
                                job_name character varying COLLATE "default" NOT NULL,
                                target_name character varying COLLATE "default" NOT NULL,
                                job_section json NOT NULL,
                                created_date date NOT NULL,
                                CONSTRAINT build_job_pkey PRIMARY KEY (job_id)
                                );"""
    
    records_to_insert = [
        (1, "Job One", "Target A", "{\"key1\": \"value1\"}", "2024-03-09"),
        (2, "Job Two", "Target B", "{\"key2\": \"value2\"}", "2024-03-08"),
        (3, "Job Three", "Target C", "{\"key3\": \"value3\"}", "2024-03-07"),
]

    cursor.execute(create_pipeline_table)

    insert_query = """INSERT INTO buildPPL.buildjobs (job_id, job_name, target_name, job_section, created_date)
                  VALUES (%s, %s, %s, %s, %s)"""


    cursor.executemany(insert_query, records_to_insert)

    select_query = "select * from buildPPL.buildjobs"
    cursor.execute(select_query)
    
    #print(cursor.fetchone())
    print(cursor.fetchall())    
          

connect_to_db()
