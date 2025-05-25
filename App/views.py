#蓝图
from flask import Blueprint,render_template,request,redirect,url_for,current_app
from .models import  *
from werkzeug.utils import secure_filename
from PIL import Image
import os


blue = Blueprint('blue', __name__)

@blue.route('/')
def fresh_page():  # put application's code here
    return render_template('index.html')


@blue.route('/display')
def new_page():
    return render_template('display.html')
    # return  render_template('display.html')


# 跳转数据库页面
@blue.route('/loaddb')
def loaddb():
    return render_template('image_db.html')

#加载文件

@blue.route('/upload', methods=['GET', 'POST'])
def upload():
    file = request.files['uploadfile']
    if file:
        filename = secure_filename(file.filename)
        ext = os.path.splitext(filename)[1].lower()

        # 保存路径：将 TIF 转为 PNG
        save_path = os.path.join(current_app.config['UPLOAD_FOLDER'], 'displayed.png')

        if ext == '.tif' or ext == '.tiff':
            img = Image.open(file)
            img.convert('RGB').save(save_path)
        else:
            file.save(save_path)

        return redirect(url_for('display'))
    return '上传失败'



# @blue.route('/index/')
# def index():
#     return render_template('index.html', name = 'Flask TEST')

    #jsonify()函数用于将Python对象转换为JSON格式数据，并返回一个Response对象。
    #return jsonify({'name': 'Flask TEST', 'age': 25})
