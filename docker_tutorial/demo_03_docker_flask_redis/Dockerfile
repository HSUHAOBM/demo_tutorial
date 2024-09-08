# 使用python3.8 alpine 模板
FROM python:3.8.3-alpine3.12
# 當前目錄 映射到容器中的 /app目錄
ADD . /app
# 設置工作目錄
WORKDIR /app
# 安装python 依賴
RUN pip install -r requirements.txt
# 啟用服務
CMD python main.py
