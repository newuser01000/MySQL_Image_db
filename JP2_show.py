# import rasterio
# import matplotlib.pyplot as plt
# import hashlib
# import os
#
# jp2_file = 'D:/IMG_DATA/Download/B11.jp2'
# with rasterio.open(jp2_file) as src:
#     band = src.read(1)
#     print("波段数:", src.count)
#     print("图像尺寸 (高度, 宽度):", src.height, src.width)
#     print("波段数量:", src.count)
#     print("坐标参考系统:", src.crs)

# with open(jp2_file, "rb") as f:
#     image = f.read()
# md5_insert = hashlib.md5(image).hexdigest()
# print("插入后MD5:", md5_insert)

# plt.imshow(band, cmap='gray')
# file_name = os.path.basename(jp2_file)
# plt.title(file_name)
# plt.show()
#


# from PIL import Image
# import matplotlib.pyplot as plt
# import matplotlib
# import os
# jp2_file = 'D:/IMG_DATA/Download/TCI.jp2'
# # 打开 JP2 图像
# img = Image.open(jp2_file)
#
# # 可选：转换为 RGB（如果图像不是 RGB 格式）
# img = img.convert("RGB")
# matplotlib.rcParams['font.sans-serif'] = ['SimHei']  # 设置中文字体
# # 显示图像
# plt.imshow(img)
# plt.axis('off')
# plt.title(os.path.basename(jp2_file))
# plt.show()


# import rasterio
# import matplotlib.pyplot as plt
# import numpy as np
# import os
#
# jp2_file = 'D:/IMG_DATA/Download/TCI.jp2'
# # 打开 JP2 多波段图像
# with rasterio.open(jp2_file) as src:
#     print("图像尺寸:", src.width, src.height)
#     print("波段数:", src.count)
#
#     # 假设使用第 3-2-1 波段（RGB）
#     r = src.read(3)
#     g = src.read(2)
#     b = src.read(1)
#
#     # 合成为 RGB 图像并归一化
#     rgb = np.stack([r, g, b], axis=-1).astype(np.float32)
#     rgb = (rgb - rgb.min()) / (rgb.max() - rgb.min())
#
#     # 显示图像
#     plt.imshow(rgb)
#     plt.axis('off')
#     plt.title(os.path.basename(jp2_file))
#     plt.show()



from osgeo import gdal
import matplotlib.pyplot as plt

ds = gdal.Open('D:/IMG_DATA/Download/B08.jp2')
if ds is None:
    print("Failed to open JP2 file")
else:
    band = ds.GetRasterBand(1)
    array = band.ReadAsArray()
    plt.imshow(array, cmap='gray')
    plt.axis('off')
    plt.show()
