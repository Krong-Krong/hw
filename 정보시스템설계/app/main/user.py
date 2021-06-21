from flask import Blueprint, request, render_template, flash, redirect, url_for
from flask import current_app as current_app

from app.module import dbModule

user = Blueprint('user', __name__, url_prefix='/user')


@user.route('/', methods=['POST', 'GET'])
def index():
    global number
    number = None

    if request.method == 'POST':
        value = request.form
        for i, j in value.items():
            number = j
    return render_template('/main/user.html', result=number, resultData=None)



# SELECT1
@user.route('/select1', methods=['GET'])
def select1():
    db_class = dbModule.Database()

    sql = "select female_style.height, female_style.weight, female_style.character, female_style.personality, female_style.drinking, female_style.smoking\
            from matching, female_style\
            where matching.m_id = '" + number +"' and matching.f_id = female_style.id"
    row = db_class.executeAll(sql)
    print(row)

    return render_template('/main/user.html',  result=number, resultData=row.to_html(index=False))


# SELECT2
@user.route('/select2', methods=['GET'])
def select2():
    db_class = dbModule.Database()

    sql = "select coupling.love_date\
            from matching, coupling\
            where matching.m_id = '"+ number +"' and matching.matching_code = coupling.matching_code"

    row = db_class.executeAll(sql)
    print(row)

    return render_template('/main/user.html', result=number, resultData=row.to_html(index=False))


# SELECT3
@user.route('/select3', methods=['GET'])
def select3():
    db_class = dbModule.Database()

    sql = "select seller.seller_score, ordering.product_id\
            from seller, product_seller, ordering\
            where ordering.ordered_id = '"+ number +"' and ordering.product_id = product_seller.product_id and product_seller.seller_id = seller.seller_id"

    row = db_class.executeAll(sql)
    print(row)

    return render_template('/main/user.html', result=number, resultData=row.to_html(index=False))
