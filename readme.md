deeplx-api
本工具作为沉浸式翻译的接口工具，采用多API多线程，自动判断API有效性，获取低延迟有效的接口，大大提高沉浸式翻译的速度和效率。
可以部署在本地（PC端\本地docker），也可以运行在VPS上。

使用方法：
一、直接下载二进制文件deeplx-api.exe
1.将urls.txt与deeplx-api.exe，放在同一目录下，按urls.txt内链接的格式http(s)://域名(ip)/translate），每行一条，自行添加。
2.运行deeplx-api.exe，弹出命令框内显示可用url数量。
3.设置沉浸式翻译服务为DeepLX(Beta)，API地址为http://127.0.0.1:5000/translate

提示：exe可执行文件可能会被杀毒软件（windows defender）误杀，请将exe文件添加到白名单。 

二、docker部署
docker run -p 5000:5000 -v /path/to/your/urls.txt:/app/urls.txt -v /path/to/your/logs:/app/logs --name deeplx-api --restart always geekyes/deeplx-api

1.docker run
  --name deeplx-api \
  -p 5000:5000 \
  -v /path/to/your/urls.txt:/app/urls.txt \
  -v /path/to/your/logs:/app/logs \
  --restart always  \
  geekyes/deeplx-api
映射端口可以自定义，urls.txt和logs目录选择本机目录。
2.设置沉浸式翻译服务为DeepLX(Beta)，API地址为http://127.0.0.1:5000/translate或http://VPS_ip:5000/translate

三、urls.txt内容不定时更新，请关注github仓库。