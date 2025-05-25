from App import create_app

app = create_app()


if __name__ == '__main__':
    app.run( debug = True, port = 5000, host = '0.0.0.0' )
    # 开启调试模式，修改代码后自动重启
    # 启动指定服务器的端口号，默认是5000
    # 主机，默认时127.0.0.1，允许外部访问