import mysql.connector as con
from PIL import Image
from tqdm import tqdm
import os
import io
import hashlib

Image.MAX_IMAGE_PIXELS = None # 取消限制图片大小
# 创建连接池
pool = con.pooling.MySQLConnectionPool(
    charset='utf8mb4',
    pool_name = "mypool",
    pool_size = 5, # 连接池大小
    host = "localhost",
    user = "root",
    passwd = "admin",
    db = "Mysql",
    use_pure = True,
    connect_timeout = 300, # 连接超时时间为5分钟
)
# 连接数据库
conn = pool.get_connection()
cursor = conn.cursor( buffered = True)

# 查询语句
sql = "SELECT id, name, image FROM Image WHERE id = %s"
values = (7, )

# 执行查询语句
cursor.execute(sql, values)
result = cursor.fetchone()

if not result:
    print(f"❌ 未找到ID={values[0]}的图片")
    cursor.close()
    conn.close()
    exit()


file_name, image_data = result[1], result[2]

md5_download = hashlib.md5(image_data).hexdigest()
print("🔵 下载后 MD5:", md5_download)

# 保存图片
Download_dir = "D:/IMG_DATA/Download"
file_path = os.path.join(Download_dir, file_name)
file_path = os.path.join(Download_dir, file_name)
# os.makedirs(os.path.dirname(file_path), exist_ok=True)




with open(file_path, "wb") as f:
    f.write(image_data)
print(f"✅ 图片已保存到 {file_path}")

cursor.close()
conn.close()

if md5_download == hashlib.md5(image_data).hexdigest():
    print("✅ 校验成功：MD5 一致")
else:
    print("❌ 警告：MD5 不一致")