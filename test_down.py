import mysql.connector
import os
import io
from PIL import Image
import matplotlib.pyplot as plt
import tifffile
import pymysql

def download(file_id, output_path):
    # 连接数据库
    # conn = mysql.connector.connect(
    #     host='localhost',
    #     user='root',
    #     password='admin',
    #     database='Image_database',
    # )

    conn = pymysql.connect(
        host='localhost',
        user='root',
        password='admin',
        database='Image_database',
        charset='utf8mb4'
    )
    cursor = conn.cursor()

    # 查询文件
    sql = "SELECT name,image FROM Image WHERE id = %s"
    cursor.execute(sql, (file_id,))
    result = cursor.fetchone()

    if result:
        output_path = os.path.join(output_path, result[0]).replace("\\", "/")
        with open(output_path, 'wb') as f:
            f.write(result[1])
        print(f"File '{file_id}' downloaded successfully to '{output_path}'.")
        # tif_data = result[1]
        # image = tifffile.imread(io.BytesIO(tif_data))
        # plt.imshow(image, cmap='gray')
        # plt.show()

    else:
        print(f"File '{file_id}' not found in the database.")

    cursor.close()
    conn.close()

# 示例调用
out_path = "D:/IMG_DATA/Download"
download(33, out_path)
