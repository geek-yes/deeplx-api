**2. README_ZH.md (中文版)**


# DeepLX API

[English](README.md) | [中文](README_ZH.md)

本工具作为沉浸式翻译的接口工具，采用多 API 多线程，自动判断 API 有效性，获取低延迟有效的接口，大大提高沉浸式翻译的速度和效率。可以部署在本地（PC 端\本地 Docker），也可以运行在 VPS 上。

## 功能特点

- **多 API 支持:** 利用多个翻译 API，确保可用性和冗余性。
- **自动 API 验证:** 动态测试 API 端点，以找到最快和最可靠的选项。
- **低延迟:** 优化速度，提供近乎实时的翻译。
- **灵活部署:** 可以部署在各种平台上，包括本地 PC，Docker 和 VPS。

## 入门指南

### 1. 下载二进制文件 (可执行文件)

1. 前往 [releases](https://github.com/geek-yes/deeplx-api/releases) 页面下载 `deeplx-api.exe` 二进制文件。
2. 将 `urls.txt` 和 `deeplx-api.exe` 放在同一目录下。在 `urls.txt` 中填充翻译 API URL，每行一个，格式为 `http(s)://域名(ip)/translate`。
3. 运行 `deeplx-api.exe`。命令提示符将显示可用的 URL 数量。
4. 配置您的沉浸式翻译服务以使用 DeepLX (Beta)，API 地址：`http://127.0.0.1:5000/translate`。

**注意:** 可执行文件可能会被杀毒软件（如 Windows Defender）标记。请将可执行文件添加到杀毒软件的白名单。

### 2. Docker 部署

```bash
docker run \
  --name deeplx-api \
  -p 5000:5000 \
  -v /path/to/your/urls.txt:/app/urls.txt \
  -v /path/to/your/logs:/app/logs \
  --restart always \
  geekyes/deeplx-api
```
您可以根据需要自定义端口映射。

将 /path/to/your/urls.txt 和 /path/to/your/logs 替换为您本地的目录路径。

配置您的沉浸式翻译服务以使用 DeepLX (Beta)，API 地址：http://127.0.0.1:5000/translate 或 http://VPS_ip:5000/translate。

### 3. urls.txt 更新
urls.txt 的内容将定期更新。请关注此 GitHub 存储库以获取最新版本。

贡献
欢迎贡献！请随时提交问题或拉取请求。

许可证
本项目根据 [MIT 许可证](LICENSE.md) 开源。
