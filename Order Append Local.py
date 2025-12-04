import pymysql
import csv

# 1. Connect Database
connection = pymysql.connect(
    host='localhost',
    user='root',
    password='Yiqihapi@durant',
    db='recommendation',
    charset='utf8mb4'
)

cursor = connection.cursor()

# 2. Open CSV File
csv_file_path = r"C:\Users\skydu\Documents\Machine Learning\inflow_salesorder for ML.csv"

with open(csv_file_path, 'r', encoding='utf-8') as file:
    csv_data = csv.reader(file)
    
    next(csv_data)  # Skip the first row

    # 3. Insert data by rows
    for row in csv_data:
        sql = """
        INSERT INTO fact_order_line 
        (order_number, order_date, customer_name, product_name, 
         product_quantity, product_unitprice, product_subtotal, amount_paid) 
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        """
        cursor.execute(sql, row)

# 4. Submit and close connection
connection.commit()
cursor.close()
connection.close()

print("Data Import Completed！")
