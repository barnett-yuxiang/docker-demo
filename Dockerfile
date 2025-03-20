# 使用 Python 官方基础镜像
FROM python:3.11-slim

# 设置工作目录
WORKDIR /app

# 安装依赖
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# 拷贝当前目录到容器中
COPY . .

# 定义容器启动时执行的命令
CMD ["python", "app.py"]
