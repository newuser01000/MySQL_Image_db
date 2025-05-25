import mysql.connector
import os

def download_large_file(file_id, output_path):
    chunk_size = 8 * 1024 * 1024

    conn = mysql.connector.connect(
        host='localhost',
        user='root',
        password='admin',
        database='Mysql',
    )
    cursor = conn.cursor()

    # 查询文件大小
    cursor.execute("SELECT LENGTH(image), name FROM Image WHERE id = %s", (file_id,))
    row = cursor.fetchone()
    if row is None or row[0] is None:
        print("File not found or empty.")
        cursor.close()
        conn.close()
        return
    total_size = row[0]

    output_path = os.path.join(output_path, row[1]).replace("\\", "/")
    with open(output_path, 'wb') as f:
        offset = 0
        while offset < total_size:
            # SUBSTRING(blob, offset+1, chunk_size)
            cursor.execute("SELECT SUBSTRING(image, %s, %s) FROM Image WHERE id = %s",
                           (offset+1, chunk_size, file_id))
            chunk = cursor.fetchone()[0]
            if chunk:
                f.write(chunk)
            offset += chunk_size

    print(f"File id {file_id} downloaded successfully to '{output_path}'.")

    cursor.close()
    conn.close()

# 示例调用
output_path = 'D:/IMG_DATA/Download'
download_large_file(21, output_path)
