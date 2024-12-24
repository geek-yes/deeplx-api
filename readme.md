# DeepLX API

[English](README.md) | [中文](README_ZH.md)

This tool serves as an interface for immersive translation, employing multiple APIs and threads. It automatically checks API validity to obtain low-latency and effective interfaces, significantly enhancing the speed and efficiency of immersive translation. It can be deployed locally (on a PC or local Docker) or run on a VPS.

## Features

- **Multi-API Support:** Leverages multiple translation APIs to ensure availability and redundancy.
- **Automatic API Validation:** Dynamically tests API endpoints to find the fastest and most reliable options.
- **Low Latency:** Optimizes for speed to provide near real-time translation.
- **Flexible Deployment:** Can be deployed on various platforms, including local PCs, Docker, and VPS.

## Getting Started

### 1. Download the Binary (Executable)

1. Go to the [releases](https://github.com/geek-yes/deeplx-api/releases) page and download the `deeplx-api.exe` binary file.
2. Place `urls.txt` and `deeplx-api.exe` in the same directory. Populate `urls.txt` with translation API URLs, one per line, in the format `http(s)://domain(ip)/translate`.
3. Run `deeplx-api.exe`. The command prompt will display the number of available URLs.
4. Configure your immersive translation service to use DeepLX (Beta) with the API address: `http://127.0.0.1:5000/translate`.

**Note:** The executable might be flagged by antivirus software (like Windows Defender). Please add the executable file to your antivirus's whitelist.

### 2. Docker Deployment

```bash
docker run \
  --name deeplx-api \
  -p 5000:5000 \
  -v /path/to/your/urls.txt:/app/urls.txt \
  -v /path/to/your/logs:/app/logs \
  --restart always \
  geekyes/deeplx-api
```
You can customize the port mapping as needed.

Replace /path/to/your/urls.txt and /path/to/your/logs with your local directory paths.

Configure your immersive translation service to use DeepLX (Beta) with API address: http://127.0.0.1:5000/translate or http://VPS_ip:5000/translate.

### 3. urls.txt Updates
The content of urls.txt will be updated periodically. Please keep an eye on this GitHub repository for the latest version.

Contributing
Contributions are welcome! Feel free to submit issues or pull requests.

License
This project is licensed under the [MIT License](LICENSE.md).
