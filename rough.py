import csv
import time
import os.path, random

def write_to_csv():

    samples = {"place":[{'Data': random.randint(1,10), 'Timestamp': time.strftime('%Y-%m-%d %H:%M:%S')}]*5}
    for key, value in samples.items():
            pass
    filename = key+'.csv'
    file_exists = os.path.isfile(filename)

    with open(filename, 'a') as csv_file:
        writer = csv.writer(csv_file)

        if not file_exists:
            writer.writerow(['Data', 'Timestamp'])


        for key, value in samples.items():
            print(key, value)
            for val in value:
                print(val['Data'],val['Timestamp'])
                writer.writerow([val['Data'],val['Timestamp']])
                csv_file.flush()  # Flush the buffer to write immediately


if __name__ == '__main__':
    write_to_csv()
