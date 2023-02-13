"""
对象数组根据字段排序
"""


def list_sort_by_object_property():
    data_list = [
        {"no": 28, "weight": [90]},
        {"no": 25, "weight": [90]},
        {"no": 1, "weight": [100]},
        {"no": 2, "weight": [20]},
    ]
    print("original list: \n\t", data_list)

    # 单级排序，仅按照score排序
    new_s = sorted(data_list, key=lambda e: e.__getitem__('weight')[0])
    print("new list:\n\t ", new_s)

    # 多级排序,先按照score，再按照no排序
    new_s_2 = sorted(new_s, key=lambda e: (e.__getitem__('weight')[0], e.__getitem__('no')))
    print("new_list_2: \n\t", new_s_2)


if __name__ == '__main__':
    list_sort_by_object_property()
