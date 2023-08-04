# SimplePaddleOCRApi

一个可 Docker(compose) 部署的, 基于 `FastAPI` 的简易版 Paddle OCR Web API.

## 接口功能

- [x] 局域网范围内路径图片 OCR 识别
- [x] Base64 数据识别
- [x] 上传文件识别

## 部署方式

在 `Centos7` 的服务器中测试成功, 需要先安装好 `Docker`

```shell
git clone https://ghproxy.com/https://github.com/hellokaton/ppocr-api.git
cd ppocr-api

# 制作 Docker 镜像
docker build -t ppocrapi:1.0 .
```

编辑 `docker-compose.yml`

```yaml
version: "3"

services:
  app:
    container_name: ppocr-api
    image: ppocrapi:1.0
    environment:
      - "TZ=Asia/Hong_Kong"
    ports:
      - "10778:8000"
    restart: unless-stopped
```

4. 生成 Docker 容器并运行

```shell
docker-compose up -d
```

5. 访问接口

- 识别上传文件：`http://[host]:10778/ocr/predict-by-file`
- 识别Base64图片：`http://[host]:10778/ocr/predict-by-base64`

项目修改自 https://github.com/cgcel/SimplePaddleOCRApi
