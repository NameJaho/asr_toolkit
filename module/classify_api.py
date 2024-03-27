import json

import requests
from loguru import logger


def classify(texts):
    url = "http://183.6.28.97:8190/taskflow/utc"

    headers = {"Content-Type": "application/json"}

    data = {"data": {"text": texts}}
    try:
        res = requests.post(url=url, headers=headers, data=json.dumps(data))
    except:
        logger.error("请求分类接口失败")
        return "", []
    else:
        r = res.json()['result']
    logger.info(r)
    if r[0]['predictions']:
        labels = sorted(r[0]['predictions'], key=lambda x: x['score'], reverse=True)
        if len(labels) > 1 and '其他' == labels[0]['label']:
            r[0]['label'] = labels[1]['label']
        else:
            r[0]['label'] = labels[0]['label']
    else:
        r[0]['label'] = ""
    label = r[0]['label']
    predictions = r[0]['predictions']
    return label, predictions
