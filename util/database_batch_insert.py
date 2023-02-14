#!/usr/bin/python
# -*- coding: UTF-8 -*-
import random

import pymysql

'''
需求: 使用SQL在数据库中给没有子级的菜单全部加上三个按钮

所有父id:pids
所有id: ids

没有子级：任何一行数据的pid不包含ids数组中的值
'''

t_name = "t_b2_permission"
host = "localhost"
port = 13306
user = "test"
password = "test"
database = "scm_test"
charset = "utf8mb4"

global t_name, pids, ids, my_cursor


def db_init():
    global db, my_cursor

    config = {
        "host": host,
        "port": port,
        "user": user,
        "passwd": password,
        "database": database,
        "charset": charset,
        # 一次执行多个SQL需要配置
        "client_flag": pymysql.constants.CLIENT.MULTI_STATEMENTS
    }
    db = pymysql.connect(**config)
    my_cursor = db.cursor(pymysql.cursors.DictCursor)


if __name__ == '__main__':
    db_init()
    pids = list()
    ids = list()

    sql_query = "SELECT * FROM %s" % t_name
    my_cursor.execute(sql_query)
    result = my_cursor.fetchall()
    db.commit()

    for i in result:
        pids.append(i.__getitem__("p_id"))
        ids.append(i.__getitem__("id"))
    ids.append(0)

    pids = list(set(pids))
    resIds = list(set(ids).difference(set(pids)))

    # 生成随机id
    randomIdList = []
    for i in range(10000):
        randomId = random.randint(10000, 20000)
        if randomId not in randomIdList:
            randomIdList.append(randomId)

    # insert
    index = 0
    for i in resIds:
        sql_insert_add = """
        INSERT INTO t_b2_permission_1 (id, created_by, created_time, deleted, updated_by, updated_time, name, p_id, path, action, code, display_name, icon, menu_id, remark, sort, type, value)
            VALUES (%d, 1, '2022-12-07 16:46:49.089176', false, null, null, '新增', null, '', '', '', '新增', '', %s,  '', null, 'button', 'add');
         """ % (randomIdList[index], i)

        sql_insert_edit = """
        INSERT INTO t_b2_permission_1 (id, created_by, created_time, deleted, updated_by, updated_time, name, p_id, path, action, code, display_name, icon, menu_id, remark, sort, type, value)
            VALUES (%d, 1, '2022-12-07 16:46:55.864841', false, null, null, '编辑', null, '', '', '', '编辑', '', %s,  '', null, 'button', 'edit');
        """ % (randomIdList[index + 1], i)

        sql_insert_delete = """
        INSERT INTO t_b2_permission_1 (id, created_by, created_time, deleted, updated_by, updated_time, name, p_id, path, action, code, display_name, icon, menu_id, remark, sort, type, value)
            VALUES (%d, 1, '2022-12-07 16:47:01.470596', false, null, null, '删除', null, '', '', '', '删除', '', %s,  '', null, 'button', 'delete');
        """ % (randomIdList[index + 2], i)

        index += 3
        cursor_insert = db.cursor()
        cursor_insert.execute(sql_insert_add)
        cursor_insert.execute(sql_insert_edit)
        cursor_insert.execute(sql_insert_delete)

        print(sql_insert_add)
    db.commit()
