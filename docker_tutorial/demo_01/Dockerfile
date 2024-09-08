# 使用
FROM python:3.8.3-alpine3.12
# 當前目錄 映射 到容器内 /app目錄
ADD . /app
# 設置 /app為工作目錄
WORKDIR /app
# 安装 python 依賴包
RUN pip install -r requirements.txt
# 啟用
CMD python main.py