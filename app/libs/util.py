"""
 公共方法
 Created by 带入 on 2020/4/20.
"""
import re, uuid, json, hashlib, base64, time,datetime

def next_id():
    return '%015d%s000' % (int(time.time() * 1000), uuid.uuid4().hex)
