## 本地开发
` pip install -r deploy/requirements.txt -i https://mirrors.aliyun.com/pypi/simple/
mysqlclient 不同环境安装指南请看：
https://pypi.org/project/mysqlclient/
`



# 远程debug 生产需要关掉
```angular2html
docker exec -it mep_server_app bash
supervisorctl 
stop uwsgi
exit
回到自己pycharm 配置远程解释器 
启动 8000 端口
```

##项目目录下
###1.生成数据表
```angular2html
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py createsuperuser
```
###2.collect静态文件
```angular2html
python3 manage.py collectstatic
```
###3.压缩静态文件
```angular2html
python3 manage.py compress --force  # 其实不用手动执行，会随着客户端请求响应自动生成到STATIC/CACHE目录下
```

# 测试websocket (需要先注册登录)
# 不带认证注掉上边(AuthMiddlewareStack装饰器)测试 启动服务　
```
浏览器控制台测试脚本
var ws = new WebSocket("ws://192.168.1.62:8081/ws/notifications/");
ws.onopen = function() {
   ws.send("Hello, world");
};
ws.onmessage = function (evt) {
   alert(evt.data);
};
```


