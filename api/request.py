from pydantic import BaseModel, Field, validator
from typing import Literal, Any


# from exception.handlers import CategoryError


# 请求类型
# class BaseRequest(BaseModel):
#     @validator('category', check_fields=False)
#     def check_category_contains_colon(cls, v):
#         if ':' not in v:
#             raise CategoryError(400, '请输入完整的品类树(eg. 护肤:面部护理:洁面)')
#         return v


class NormalizeRequest(BaseModel):
    category: str = Field(..., description="用户输入的品类名", example="护肤")


class MainRequest(BaseModel):
    video_url: str = Field(..., description="视频链接",
                           example="https://sns-video-al.xhscdn.com/01e2b407823db72701037003818f3e0e32_258.mp4")
    video_id: str = Field(..., description="视频的唯一id", example="01e2b407823db72701037003818f3e0e32_258")
    video_tag_list: str = Field(..., description="视频标签", example='四宝茶;元气四宝;元气四宝汤;元气四宝茶')
    title: str = Field(..., description="视频标题", example="这个蜜桃味唇油可爱到我心里了 有被惊喜到")
    content: str = Field(..., description="视频文字内容",
                         example="唇油;唇蜜;变色唇膏;水光唇釉;美妆好物;apieu;apieu唇油")
    data: list = Field(..., description="视频数据")


class BatchRequest(BaseModel):
    data: list = Field(..., description="视频数据")


class ClsRequest(BaseModel):
    title: str = Field(..., description="视频标题", example="这个蜜桃味唇油可爱到我心里了 有被惊喜到")
    content: str = Field(..., description="视频文字内容",
                         example="唇油;唇蜜;变色唇膏;水光唇釉;美妆好物;apieu;apieu唇油")
