import mysql.connector
import os
import pymysql
import hashlib
import MySQLdb
import time

def md5_bytes(data):
    return hashlib.md5(data).hexdigest()

def upload(file_path):
    #此方法上传速度缓慢
    # conn = pymysql.connector.connect(
    #     host='localhost',
    #     user='root',
    #     password='admin',
    #     database='Image_database',
    # )

    conn = MySQLdb.connect(
        host='localhost',
        user='root',
        password='admin',
        database='Image_database',
        charset='utf8mb4',
    )

    cursor = conn.cursor()

    # 读取JP2文件为二进制
    with open(file_path, 'rb') as f:
        binary_data = f.read()

    original_hash = md5_bytes(binary_data)
    print(f"原始文件哈希: {original_hash}")


    original_size = os.path.getsize(file_path)
    read_size = len(binary_data)
    if original_size != read_size:
        raise ValueError(f"文件读取不完整: 原始大小 {original_size} 字节, 读取 {read_size} 字节")
    else:
        print(f"文件读取成功: 原始大小 {original_size} 字节, 读取 {read_size} 字节")

    # 插入SQL（使用BLOB类型）
    print("开始写入数据库...")

    start_time = time.time()
    sql = "INSERT INTO Image (name, image, description) VALUES (%s, %s, %s)"
    file_name = os.path.basename(file_path)
    cursor.execute(sql, (file_name, binary_data, "jp2文件存储测试"))
    conn.commit()
    end_time = time.time()
    print(f"写入数据库耗时: {end_time - start_time} 秒")
    print("写入数据库成功")

    #
    print("开始验证图像哈希...")
    cursor.execute("SELECT image FROM Image ORDER BY id DESC LIMIT 1")
    db_data = cursor.fetchone()[0]
    db_hash = md5_bytes(db_data)
    print(f"数据库中图像哈希: {db_hash}")
    if original_hash != db_hash:
        raise ValueError("❌ 哈希不一致，数据在写入过程中损坏")
    else:
        print("✅ 图像写入成功，哈希一致")
    print("验证图像哈希完成")
    #


    print(f"File '{file_name}' uploaded successfully.")


    cursor.close()
    conn.close()

# 示例调用
file_path = "D:/IMG_DATA/B08.jp2"
upload(file_path)





