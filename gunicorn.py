# gunicorn.py

bind = '0.0.0.0:5001'  # 绑定ip和端口号

workers = 1  # 进程数
threads = 2  # 指定每个进程开启的线程数
loglevel = 'debug'  # 日志级别，这个日志级别指的是错误日志的级别，而访问日志的级别无法设置
# accesslog = "./gunicorn_access.log"  # 访问日志文件
# errorlog = "./gunicorn_error.log"  # 错误日志文件
accesslog = "-"  # 访问日志文件
errorlog = "-"  # 错误日志文件
