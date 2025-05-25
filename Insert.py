import mysql.connector as con
from mysql.connector import Binary
from PIL import Image
import io
from tqdm import tqdm
import os
import rasterio as rio
import hashlib


# 创建连接池
pool = con.pooling.MySQLConnectionPool(
    charset='utf8mb4',
    pool_name = "mypool",
    pool_size = 5, # 连接池大小
    host = "localhost",
    user = "root",
    passwd = "admin", # 密码
    db = "Mysql", # 数据库名
    use_pure = True,
    connect_timeout = 300, # 连接超时时间为5分钟
)

file_path = "D:/IMG_DATA/B01.TIF"
file_name = os.path.basename(file_path)

# 读取文件信息
with rio.open(file_path) as src:
    print("波段数:", src.count)
    print("宽 × 高:", src.width, "×", src.height)
    print("数据类型:", src.dtypes)
    print("坐标参考:", src.crs)

# 读取文件数据
with open(file_path, "rb") as f:
    image_data = f.read()
md5_insert = hashlib.md5(image_data).hexdigest()
print("插入前MD5:", md5_insert)


# 获取连接
db = pool.get_connection()
cursor = db.cursor()


sql = "insert into Image(name, image, description ) values( %s, %s, %s)" # 要执行的sql语句
values = ( file_name, Binary(image_data), 'This is a test image') # 要插入的值
#
try:
    cursor.execute("SET GLOBAL max_allowed_packet = 256 * 1024 * 1024")
    cursor.execute(sql, values)
    db.commit()
    print("✅ 图片插入成功！ID:", cursor.lastrowid)
except Exception as e:
    db.rollback()
    print("❌ 插入失败:", e)
finally:
    cursor.close()
    db.close()