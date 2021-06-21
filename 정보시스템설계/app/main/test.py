# file name : test.py
# pwd : /project_name/app/test/test.py

from flask import Blueprint, request, render_template, flash, redirect, url_for
from flask import current_app as current_app

from app.module import dbModule

test = Blueprint('test', __name__, url_prefix='/test')


@test.route('/', methods=['GET'])
def index():
    return render_template('/main/test.html', resultData=None)


# SELECT1
@test.route('/select1', methods=['GET'])
def select1():
    db_class = dbModule.Database()

    sql = "select female_style.height, female_style.weight, female_style.character, female_style.body, female_style.drinking, female_style.smoking\
            from matching, female_style\
            where matching.m_id = '10002' and matching.f_id = female_style.id"

    row = db_class.executeAll(sql)
    print(row)

    return render_template('/main/test.html', resultData=row.to_html())


# SELECT2
@test.route('/select2', methods=['GET'])
def select2():
    db_class = dbModule.Database()

    sql = "select coupling.love_date\
            from matching, coupling\
            where matching.m_id = '10002' and matching.matching_code = coupling.matching_code"

    row = db_class.executeAll(sql)
    print(row)

    return render_template('/main/test.html', resultData=row.to_html())


# SELECT3
@test.route('/select3', methods=['GET'])
def select3():
    db_class = dbModule.Database()

    sql = "select seller.seller_score, ordering.product_id\
            from seller, product_seller, ordering\
            where ordering.ordered_id = '10003' and ordering.product_id = product_seller.product_id and product_seller.seller_id = seller.seller_id"

    row = db_class.executeAll(sql)
    print(row)

    return render_template('/main/test.html', resultData=row.to_html())


# SELECT4
@test.route('/select4', methods=['GET'])
def select4():
    db_class = dbModule.Database()

    sql = "select ordering.product_id\
            from ordering, matching\
            where matching.matching_code = 'M0005' and matching.m_id = ordering.ordered_id"

    row = db_class.executeAll(sql)
    print(row)

    return render_template('/main/test.html', resultData=row.to_html())


# SELECT5
@test.route('/select5', methods=['GET'])
def select5():
    db_class = dbModule.Database()

    sql = "select count(*)\
            from coupling"

    row = db_class.executeAll(sql)
    print(row)

    return render_template('/main/test.html', resultData=row.to_html())


# SELECT6
@test.route('/select6', methods=['GET'])
def select6():
    db_class = dbModule.Database()

    sql = "select *\
            from male_want_female\
            where id = '10010'"

    row = db_class.executeAll(sql)
    print(row)

    return render_template('/main/test.html', resultData=row.to_html())


# SELECT7
@test.route('/select7', methods=['GET'])
def select7():
    db_class = dbModule.Database()

    sql = "select count(*)\
            from matching"

    row = db_class.executeAll(sql)
    print(row)

    return render_template('/main/test.html', resultData=row.to_html())


# SELECT8
@test.route('/select8', methods=['GET'])
def select8():
    db_class = dbModule.Database()

    sql = "select seller_score\
            from seller\
            where seller_id = '50007'"

    row = db_class.executeAll(sql)
    print(row)

    return render_template('/main/test.html', resultData=row.to_html())




