#!/bin/sh

# 设置日志文件路径
LOG_FILE="/app/logs/startup.log"

# 获取当前时间
CURRENT_TIME=$(date "+%Y-%m-%d %H:%M:%S")

# 添加启动日志记录
echo "$CURRENT_TIME - Starting deeplx-api..." | tee -a "$LOG_FILE"

# 切换工作目录到 /app
cd /app

# 显示 /app 目录下的文件列表
ls -l | tee -a "$LOG_FILE"

# 检查 deeplx-api.py 是否存在
if [ ! -f deeplx-api.py ]; then
  echo "$CURRENT_TIME - Error: deeplx-api.py not found in /app directory!" | tee -a "$LOG_FILE"
  exit 1
fi

# 检查 urls.txt 是否存在
if [ ! -f urls.txt ]; then
  echo "$CURRENT_TIME - Error: urls.txt not found in /app directory!" | tee -a "$LOG_FILE"
  exit 1
fi

# 启动应用程序
echo "$CURRENT_TIME - Starting deeplx-api application..." | tee -a "$LOG_FILE"
python deeplx-api.py 2>&1 | tee -a "$LOG_FILE"

# 添加应用程序启动完成日志记录
echo "$CURRENT_TIME - deeplx-api application started successfully." | tee -a "$LOG_FILE"
