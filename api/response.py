from pydantic import BaseModel, Field
from typing import List, Any, Union


# 通用响应模型
class CommonResponse(BaseModel):
    code: int = Field(..., description="返回信息")
    # data: Any  # 可根据需要进一步指定
    # msg: str = Field(None, description="返回信息")


# 品类标准化响应
class NormalizeResponseData(BaseModel):
    category_list: list = Field(..., description="返回前5个相似品类",
                                example=['护肤:面部护理', '护肤:其他', '护肤:防晒', '护肤:眼部护理',
                                         '护肤:面部护理:其他'])


# 品类标准化响应
class NormalizeResponse(CommonResponse):
    data: NormalizeResponseData


# 品牌接口响应
class MainResponseData(BaseModel):
    # features: Union[dict, str] = Field(None, description="asr全流程结果",
    #                                    example={
    #                                        "features": {
    #                                            "duration": 83.24199546485261,
    #                                            "db20_splits_size": 1.1772903743204797,
    #                                            "energy_mean": 0.1369696706533432,
    #                                            "energy_std": 0.1104106679558754,
    #                                            "rhythm_per_sec": 4.565003492263084,
    #                                            "gaps_per_sec": 0.10811850376412568,
    #                                            "vocal_duration": 62080,
    #                                            "vocal_pct": 0.7457774126307692,
    #                                            "music_detected": False,
    #                                            "asr": True,
    #                                            "id": "01e2b407823db72701037003818f3e0e32_258",
    #                                            "title": "这个蜜桃味唇油可爱到我心里了 有被惊喜到",
    #                                            "video_tag_list": "四宝茶;元气四宝;元气四宝汤;元气四宝茶",
    #                                            "video_url": "https://sns-video-al.xhscdn.com/01e2b407823db72701037003818f3e0e32_258.mp4",
    #                                            "asr_text": "我的大嘴怪好朋友长的一个大大的嘴巴，尖尖的牙齿上有着漂亮的颜色，可以让小朋友在上面欢快的捉迷藏，他的嘴巴里还放着滑滑梯，还有小朋友们的家，不仅可以在里面玩耍锻炼身体，还可以休息。他的舌头就像一条通道，小朋友们可以走进大嘴怪的嘴里。嗯，腿怪不仅嘴巴大，身体也不一般，既长着翅膀，可以在天上飞，还长着鱼的尾巴，可以在水里游长着鸭子的脚，可以在路上走，真的是好，特别嘴巴大长得怪，还喜欢与小朋友们一起欢快的玩耍，心地善良，长得还漂亮。这样的大嘴怪，你喜欢吗？"
    #                                        }
    #                                    })
    msg: str = Field(None,description="返回信息")
    asr_text: str = Field(None,description="asr结果")
    video_id: str = Field(None,description="video_id")
    label: str = Field(..., description="美妆个护",
                       example='')
    predictions: list = Field(..., description="分类结果",
                              example=[
                                  {
                                      "label": "美妆个护",
                                      "score": 0.28015224069704237
                                  },
                                  {
                                      "label": "其他",
                                      "score": 0.6194684983840593
                                  }
                              ])
    code: int = Field(..., description="返回信息")


class MainResponse(CommonResponse):
    data: MainResponseData


class TargetCatResponseData(BaseModel):
    categories: list = Field(..., description="目标分类",
                                   example=["宠物用品", "宠物食品", "零食", "母婴用品", "家具", "家居百货", "珠宝配饰",
                                            "日用百货",
                                            "食品饮料", "电器", "保健品", "科技数码", "美妆个护", "购物", ]
                                   )
    msg: str = Field(None,description="返回信息")
    code: int = Field(..., description="返回信息")



class TargetCatResponse(CommonResponse):
    data: TargetCatResponseData


class ClsResponseData(BaseModel):
    label: str = Field(..., description="美妆个护",
                       example='')
    predictions: list = Field(..., description="分类结果",
                              example=[
                                  {
                                      "label": "美妆个护",
                                      "score": 0.28015224069704237
                                  },
                                  {
                                      "label": "其他",
                                      "score": 0.6194684983840593
                                  }
                              ])
    msg: str = Field(None,description="返回信息")
    code: int = Field(..., description="返回信息")



class ClsResponse(CommonResponse):
    data: ClsResponseData


# 品牌接口响应


# 品牌接口响应
class BrandResponseData(BaseModel):
    head: list = Field(..., description="1-3名 品牌列表",
                       example=['珣秘', '且初', '彤曼泉'])
    tail: list = Field(..., description="8-10名 品牌列表",
                       example=['浅藤', '赫莲娜', '芭比波朗'])
    topn: int = Field(..., description="返回的品牌处于过滤15%后的", )

    detail: list = Field(..., description="mom数据")


class BrandResponse(CommonResponse):
    data: BrandResponseData


# 品牌接口响应
class PriceBandResponseData(BaseModel):
    price_band: list = Field(..., description="价格区间列表",
                             example=[
                                 {
                                     "price_band": "0 - 40",
                                     "percentiles": 0.2,
                                     "count": "2750"
                                 },
                                 {
                                     "price_band": "40 - 60",
                                     "percentiles": 0.4,
                                     "count": "2750"
                                 },
                                 {
                                     "price_band": "60 - 80",
                                     "percentiles": 0.6,
                                     "count": "2720"
                                 },
                                 {
                                     "price_band": "80 - 130",
                                     "percentiles": 0.8,
                                     "count": "2770"
                                 },
                                 {
                                     "price_band": "> 130",
                                     "percentiles": 1,
                                     "count": "2760"
                                 }
                             ])


class PriceBandResponse(CommonResponse):
    data: PriceBandResponseData


# 商品接口响应
class ProductResponseData(BaseModel):
    product_list: list = Field(..., description="商品列表",
                               example=[
                                   {
                                       "out_brand": "斑末",
                                       "type_": "head",
                                       "spuname": "【抖音同款】范博士雪柔雅美白洗面奶男女敏感肌洗面奶深层清洁",
                                       "custom_mom_growth": 2041.3333333333337,
                                       "keyword": "斑末|雪柔雅美白洗面奶"
                                   },
                                   {
                                       "out_brand": "DIW",
                                       "type_": "head",
                                       "spuname": "香港研究院洗面奶美白淡斑提亮肤色烟酰胺氨基酸控油清洁专用女27",
                                       "custom_mom_growth": 439,
                                       "keyword": "DIW|香港研究院洗面奶"
                                   }])


class ProductResponse(CommonResponse):
    data: ProductResponseData


# 商品接口响应
class UnionResponseData(BaseModel):
    result: Union[dict, list] = Field(..., description="商品列表",
                                      example={
                                          "brand_list": {
                                              "head": [
                                                  "宜丽雅",
                                                  "芭淇",
                                                  "且初"
                                              ],
                                              "tail": [
                                                  "玉泽",
                                                  "悠宜",
                                                  "娇润泉"
                                              ],
                                              "mom": {
                                                  "top": {
                                                      "宜丽雅 Elia": {
                                                          "MoM": "92935.21%",
                                                          "previous_3_month_avg": "233.33",
                                                          "recent_3_month_avg": "217082.16"
                                                      },
                                                      "芭淇 Boqits": {
                                                          "MoM": "1834.10%",
                                                          "previous_3_month_avg": "6725.21",
                                                          "recent_3_month_avg": "130072.67"
                                                      },
                                                      "且初 Kimtrue": {
                                                          "MoM": "652.93%",
                                                          "previous_3_month_avg": "262622.10",
                                                          "recent_3_month_avg": "1977353.40"
                                                      }
                                                  },
                                                  "tail": {
                                                      "玉泽 Dr.yu": {
                                                          "MoM": "35.29%",
                                                          "previous_3_month_avg": "36725.71",
                                                          "recent_3_month_avg": "49684.72"
                                                      },
                                                      "悠宜 Unny Club": {
                                                          "MoM": "33.04%",
                                                          "previous_3_month_avg": "130900.91",
                                                          "recent_3_month_avg": "174152.50"
                                                      },
                                                      "娇润泉 Joyruqo": {
                                                          "MoM": "21.18%",
                                                          "previous_3_month_avg": "924463.77",
                                                          "recent_3_month_avg": "1120252.89"
                                                      }
                                                  }
                                              },
                                              "topn": 15
                                          },
                                          "product_list1": [{
                                              "llm_result": "云柔洗面奶",
                                              "gemini": "",
                                              "keyword": "[{\"ingredient\": \"氨基酸\", \"function\": \"净透, 卸妆, 温和, 清洁\", \"type\": \"洗面奶\", \"series\": \"云柔\"}]",
                                              "out_brand": "简初",
                                              "type_": "head",
                                              "series": "",
                                              "sales_detail": "[[202312, 226478], [202311, 278516], [202310, 95991], [202309, 6174], [202308, 196], [202307, 98]]",
                                              "custom_mom_growth": "9191.67%",
                                              "recent_total": 600985,
                                              "previous_total": 6468,
                                              "total_month": 6
                                          }
                                          ],
                                          "product_list2": [
                                              {'llm_result': '', 'gemini': '儿童画板', 'keyword': '其他|儿童画板',
                                               'out_brand': '其他', 'type_': 'head', 'series': '',
                                               'sales_detail': '[[202312, 880], [202311, 1566], [202310, 343], [202309, 246], [202308, 25440]]',
                                               'spuname': '元全儿童画板液晶手写板', 'custom_mom_growth': '-1.0%',
                                               'recent_total': 2446.4, 'previous_total': 26030.4, 'total_month': 5}]
                                      }
                                      )


class UnionResponse(CommonResponse):
    data: UnionResponseData
