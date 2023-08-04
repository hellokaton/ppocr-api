# -*- coding: utf-8 -*-
from fastapi import APIRouter, HTTPException, UploadFile, status
from paddleocr import PaddleOCR

from models.OCRModel import *
from models.RestfulModel import *
from utils.ImageHelper import base64_to_ndarray, bytes_to_ndarray

router = APIRouter(prefix="/ocr", tags=["OCR"])

ocr = PaddleOCR(use_angle_cls=True, lang="ch")


@router.post('/predict-by-path', response_model=Result, summary="识别本地图片")
def predict_by_path(image_path: str):
    ocr_result = ocr.ocr(image_path, cls=True)
    return Result(code=0, msg="Success", data=ocr_result, cls=OCRModel)


@router.post('/predict-by-base64', response_model=Result, summary="识别 Base64 数据")
def predict_by_base64(base64model: Base64PostModel):
    img = base64_to_ndarray(base64model.base64_str)
    ocr_result = ocr.ocr(img, cls=True)
    return Result(code=0, msg="Success", data=ocr_result, cls=OCRModel)


@router.post('/predict-by-file', response_model=Result, summary="识别上传文件")
async def predict_by_file(file: UploadFile):
    result: Result = Result()
    if file.filename.endswith((".jpg", ".jpeg", ".png")):  # 只处理常见格式图片
        file_data = file.file
        img = bytes_to_ndarray(file_data.read())
        ocr_result = ocr.ocr(img, cls=True)

        result.code = 0
        result.msg = file.filename
        result.data = ocr_result
    else:
        result.code = 500
        result.msg = "请上传 .jpg 或 .png 格式图片"
    return result
