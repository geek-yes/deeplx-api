# deeplx-api

本工具作为沉浸式翻译的接口工具，采用多 API 多线程，自动判断 API 有效性，获取低延迟有效的接口，大大提高沉浸式翻译的速度和效率。可以部署在本地（PC 端\本地 Docker），也可以运行在 VPS 上。

## 使用方法：

### 一、前往[releases](https://github.com/geek-yes/deeplx-api/releases)下载二进制文件 deeplx-api.exe

1. 将 `urls.txt` 与 `deeplx-api.exe`，放在同一目录下，按 `urls.txt` 内链接的格式 `http(s)://域名(ip)/translate`，每行一条，自行添加。
2. 运行 `deeplx-api.exe`，弹出命令框内显示可用 URL 数量。
3. 设置沉浸式翻译服务为 DeepLX (Beta)，API 地址为 `http://127.0.0.1:5000/translate`

提示：`exe` 可执行文件可能会被杀毒软件（Windows Defender）误杀，请将 `exe` 文件添加到白名单。

### 二、Docker 部署

```bash
docker run
  --name deeplx-api \
  -p 5000:5000 \
  -v /path/to/your/urls.txt:/app/urls.txt \
  -v /path/to/your/logs:/app/logs \
  --restart always \
  geekyes/deeplx-api
```

映射端口可以自定义，urls.txt 和 logs 目录选择本机目录。

设置沉浸式翻译服务为 DeepLX (Beta)，API 地址为 http://127.0.0.1:5000/translate 或 http://VPS_ip:5000/translate

### 三、urls.txt 内容不定时更新，请关注 GitHub 仓库。
