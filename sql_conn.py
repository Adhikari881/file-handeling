import mysql.connector
import random
import time

def write_to_mysql( table):
    conn = mysql.connector.connect(
        user='root', password='@Kibq6066', host='localhost', database='aman_csv'
    )
    cursor = conn.cursor()

    while True:
        
        samples = {"place":[{'Data': random.randint(1,10), 'Timestamp': time.strftime('%Y-%m-%d %H:%M:%S')}]*5}
        

        for key, value in samples.items():
            print(key, value)
            for val in value:
                print(val['Data'],val['Timestamp'])
                query = f"INSERT INTO {table} (data_random, time_stamp) VALUES ('{val['Data']}', '{val['Timestamp']}')"
                print(query)
                cursor.execute(query)
                conn.commit()
                time.sleep(1)  # Wait for 1 second
        break

    conn.close()

def random_data():
    # Replace this with your logic to generate random data
    # For demonstration purposes, it generates a random integer
    return random.randint(1, 100)

if __name__ == '__main__':
    table_name = "database_1"

    write_to_mysql(table_name)
