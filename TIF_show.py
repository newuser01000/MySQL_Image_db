# from PIL import Image
# import matplotlib.pyplot as plt
#
# # 打开 TIFF 文件
# image = Image.open("D:/IMG_DATA/Download/B01.TIF")  # 替换为实际文件路径
#
# # 显示图像信息
# print(f"模式: {image.mode}, 尺寸: {image.size}, 格式: {image.format}")
#
# # 显示图像
# plt.imshow(image)
# plt.axis('off')  # 去除坐标轴
# plt.title("TIFF 图像显示")
# plt.show()



# import rasterio
# import matplotlib.pyplot as plt
#
# with rasterio.open("D:/IMG_DATA/Download/B01.TIF") as src:
#     img = src.read([1, 2, 3])  # 取 RGB 三个波段
#     plt.imshow(img.transpose(1, 2, 0))  # 调整通道顺序
#     plt.title("遥感图像")
#     plt.axis("off")
#     plt.show()



# 用 diff 工具或 Python 校验两个文件完全一致
# 保存原始和下载后的文件，二进制对比
import hashlib

def file_hash(path):
    with open(path, "rb") as f:
        return hashlib.md5(f.read()).hexdigest()

print("原始 hash:", file_hash("D:/IMG_DATA/B01.TIF"))
print("下载 hash:", file_hash("D:/IMG_DATA/Download/B01.TIF"))
