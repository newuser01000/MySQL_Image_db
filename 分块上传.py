import MySQLdb
import os
import hashlib
import time

def md5_bytes(data):
    return hashlib.md5(data).hexdigest()

def read_file_in_chunks(file_path, chunk_size=8 * 1024 * 1024):
    """分块读取文件，返回完整的字节串"""
    data = bytearray()
    with open(file_path, 'rb') as f:
        while chunk := f.read(chunk_size):
            data.extend(chunk)
    return bytes(data)

def upload(file_path):
    conn = MySQLdb.connect(
        host='localhost',
        user='root',
        passwd='admin',
        db='Image_database',
        charset='utf8mb4'
    )
    cursor = conn.cursor()

    file_name = os.path.basename(file_path)
    binary_data = read_file_in_chunks(file_path)
    original_hash = md5_bytes(binary_data)

    print(f"✅ 读取完成，共 {len(binary_data) / (1024*1024):.2f} MB，哈希: {original_hash}")

    start_time = time.time()
    sql = "INSERT INTO Image (name, image, description) VALUES (%s, %s, %s)"
    cursor.execute(sql, (file_name, binary_data, "分块读取上传测试"))


    conn.commit()
    end_time = time.time()
    print(f"✅ 上传完成，耗时: {end_time - start_time:.2f} 秒")

    # 校验数据一致性
    cursor.execute("SELECT image FROM Image ORDER BY id DESC LIMIT 1")
    db_data = cursor.fetchone()[0]
    db_hash = md5_bytes(db_data)

    print(f"数据库哈希: {db_hash}")
    assert db_hash == original_hash, "❌ 哈希不一致，数据损坏"
    print("✅ 分块上传成功，数据一致")

    cursor.close()
    conn.close()


file_path = "D:/IMG_DATA/B08.jp2"
upload(file_path)