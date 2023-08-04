# -*- coding: utf-8 -*-

from typing import List, Union
from pydantic import BaseModel
from fastapi import status
from fastapi.responses import JSONResponse, Response

from .OCRModel import OCRModel


class Result(BaseModel):
    code: int = 0  # 响应代码
    msg: str = None  # 响应信息
    data: Union[List, str] = []  # 数据


def resp_200(*, data: Union[list, dict, str]) -> Response:
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content={
            'code': 0,
            'msg': "Success",
            'data': data,
        }
    )


def resp_400(*, data: str = None, message: str = "BAD REQUEST") -> Response:
    return JSONResponse(
        status_code=status.HTTP_400_BAD_REQUEST,
        content={
            'code': 400,
            'msg': message,
            'data': data,
        }
    )
