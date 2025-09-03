from db import *
from classes import *

def list():
    try:
        sql = 'select * from view_sale'
        cur.execute(sql)
        rows = cur.fetchall()
        if rows != None:
            sales = []
            for row in rows:
                sale = Sale()
                sale.seq=row['seq']
                sale.code=row['code']
                sale.name=row['name']
                sale.date=row['fdate']
                sale.price=row['price']
                sale.qnt=row['qnt']
                sale,sum=row['qbt']
                sales.append(sale)
            return sales
    except Exception as err:
        print('매출목록오류:', err)

if __name__=='__main__':
    sales = list()
    for sale in sales:
        sale.print()