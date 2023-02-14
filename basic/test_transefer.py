import json

dic = {"name": "jd"}


# 字典转json
def dict_to_json():
    res_json = json.dumps(dic)
    print(res_json)


# json转字典
def json_to_dict():
    res = """
    {
        "name":"jd"
    }
    """
    res_dic = json.loads(res)
    print(res_dic)


if __name__ == '__main__':
    dict_to_json()
    json_to_dict()
