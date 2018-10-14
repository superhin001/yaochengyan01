import pymysql
from config.config import *


def get_db_conn():
    conn = pymysql.connect(host=db_host,
                           port=db_port,
                           user=db_user,
                           password=db_password,
                           db=db,)
    return conn

def Query_sql(sql):
    logging.info(sql)
    conn = get_db_conn()
    cur = conn.cursor()
    cur.execute(sql)
    result = cur.fetchall()
    logging.info(result)
    cur.close()
    conn.close()
    return result


def change_db(sql):
    logging.info(sql)
    conn = get_db_conn()
    cur = conn.cursor()
    try:
        cur.execute(sql)
        conn.commit()
    except Exception as e:
        conn.rollback()
        print('数据库更改失败')
    finally:
        cur.close()
        conn.close()

def check_cardNumber(cardNumber):
    result = Query_sql("select * from cardinfo where cardNumber='{}'".format(cardNumber))
    if result:
        return True
    else:
        return False

def del_cardNumber(cardNumber):
    change_db("delete from cardinfo where cardNumber='{}'".format(cardNumber))

def insert_cardNumber(cardNumber):
    change_db("insert into cardinfo (cardNumber) values ('{}')".format(cardNumber))

def update_cardinfo(cardNumber):
    change_db("update cardinfo set cardstatus=NULL,userId=NULL where cardNumber='{}'".format(cardNumber))

def check_cardstatus(cardNumber):
    result = Query_sql("select cardstatus from cardinfo where cardNumber='{}'".format(cardNumber))
    #print(result)
    return result[0][0]

def updata_cardinfo_binding(cardNumber):
    change_db("update cardinfo set cardstatus=5010,userId=6875 where cardNumber='{}'".format(cardNumber))






if __name__ == '__main__':
    print(check_cardNumber('ycy000'))
    # print(insert_cardNumber('ycy000'))
    # print(check_cardstatus('ycy147'))
    # print(update_cardinfo('ycy147'))
