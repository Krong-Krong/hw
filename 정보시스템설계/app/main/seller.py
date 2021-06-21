# file name : test.py
# pwd : /project_name/app/test/test.py

from flask import Blueprint, request, render_template, flash, redirect, url_for
from flask import current_app as current_app

from app.module import dbModule

seller = Blueprint('seller', __name__, url_prefix='/seller')


@seller.route('/', methods=['POST', 'GET'])
def index():
    global snumber
    snumber = None

    if request.method == 'POST':
        value = request.form
        for i, j in value.items():
            snumber = j

    return render_template('/main/seller.html', result=snumber, resultData=None)

# SELECT8
@seller.route('/select8', methods=['GET'])
def select8():
    db_class = dbModule.Database()

    sql = "select seller_score\
            from seller\
            where seller_id = '"+snumber+"'"

    row = db_class.executeAll(sql)
    print(row)

    return render_template('/main/seller.html', result=snumber, resultData=row.to_html(index=False))



# SELECT1000
@seller.route('/select1000', methods=['GET'])
def select1000():
    db_class = dbModule.Database()

    sql = "select product_id as 상품명\
            from product_seller\
            where seller_id = '"+snumber+"'"

    row = db_class.executeAll(sql)
    print(row)

    return render_template('/main/seller.html', result=snumber, resultData=row.to_html(index=False))