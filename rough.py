import csv
import time
import os.path

def write_to_csv(filename):
    file_exists = os.path.isfile(filename)

    with open(filename, 'a') as csv_file:
        writer = csv.writer(csv_file)

        if not file_exists:
            writer.writerow(['Data', 'Timestamp'])

        for _ in range(10):
            data = random_data()
            timestamp = time.strftime('%Y-%m-%d %H:%M:%S')

            writer.writerow([data, timestamp])
            csv_file.flush()  # Flush the buffer to write immediately

            time.sleep(1)  # Wait for 1 second

def random_data():
    # Replace this with your logic to generate random data
    # For demonstration purposes, it generates a random integer
    import random
    return random.randint(1, 100)

if __name__ == '__main__':
    file_name = input("Enter the file name: ")+".csv"
    write_to_csv(file_name)
