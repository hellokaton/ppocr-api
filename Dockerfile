FROM registry.baidubce.com/paddlepaddle/paddle:2.5.1

EXPOSE 8000

# 设置当前目录为工作目录
WORKDIR ./

ADD . .

# pip换源并安装python依赖
RUN python3 -m pip install -i https://mirror.baidu.com/pypi/simple --upgrade pip
RUN pip3 config set global.index-url https://mirror.baidu.com/pypi/simple
RUN pip3 install -r requirements.txt

# CMD ["python3", "./main.py"]
CMD ["uvicorn", "main:app", "--host", "0.0.0.0"]