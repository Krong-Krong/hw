# file name : test.py
# pwd : /project_name/app/test/test.py

from flask import Blueprint, request, render_template, flash, redirect, url_for
from flask import current_app as current_app

from app.module import dbModule

server = Blueprint('server', __name__, url_prefix='/server')


@server.route('/', methods=['GET', 'POST'])
def index():

    global matching_code
    global id

    matching_code = None
    id = None

    if request.method == 'POST':
        value = request.form
        for i, j in value.items():
            if i == '매칭코드':
                matching_code = j
            else:
                id = j

    return render_template('/main/server.html', matching_code=matching_code, id=id, resultData=None)

# SELECT4
@server.route('/select4', methods=['GET'])
def select4():
    db_class = dbModule.Database()

    sql = "select ordering.product_id\
            from ordering, matching\
            where matching.matching_code = '" + matching_code +"' and matching.m_id = ordering.ordered_id"

    row = db_class.executeAll(sql)
    print(row)

    return render_template('/main/server.html',  matching_code=matching_code, id=id, resultData=row.to_html(index=False))


# SELECT5
@server.route('/select5', methods=['GET'])
def select5():
    db_class = dbModule.Database()

    sql = "select count(*)\
            from coupling"

    row = db_class.executeAll(sql)
    print(row)

    return render_template('/main/server.html', matching_code=matching_code, id=id, resultData=row.to_html(index=False))


# SELECT6
@server.route('/select6', methods=['GET'])
def select6():
    db_class = dbModule.Database()

    sql = "select *\
            from male_want_female\
            where id = '"+id+"'"

    row = db_class.executeAll(sql)
    print(row)

    return render_template('/main/server.html', matching_code=matching_code, id=id, resultData=row.to_html(index=False))


# SELECT7
@server.route('/select7', methods=['GET'])
def select7():
    db_class = dbModule.Database()

    sql = "select count(*)\
            from matching"

    row = db_class.executeAll(sql)
    print(row)

    return render_template('/main/server.html', matching_code=matching_code, id=id, resultData=row.to_html(index=False))


# SELECT100
@server.route('/select100', methods=['GET'])
def select100():
    db_class = dbModule.Database()

    sql = "select ordering.product_id\
            from ordering, matching\
            where matching.matching_code = '" + matching_code +"' and matching.f_id = ordering.ordered_w_id"

    row = db_class.executeAll(sql)
    print(row)

    return render_template('/main/server.html',  matching_code=matching_code, id=id, resultData=row.to_html(index=False))

# SELECT99
@server.route('/select99', methods=['GET'])
def select99():
    db_class = dbModule.Database()

    sql = "select matching.m_id as 남성ID, count(*) as 매칭횟수\
            from matching\
            group by m_id\
            order by 매칭횟수 desc"

    row = db_class.executeAll(sql)
    print(row)

    return render_template('/main/server.html',  matching_code=matching_code, id=id, resultData=row.to_html(index=False))

# SELECT98
@server.route('/select98', methods=['GET'])
def select98():
    db_class = dbModule.Database()

    sql = "select matching.f_id as 여성ID, count(*) as 매칭횟수\
            from matching\
            group by f_id\
            order by 매칭횟수 desc"

    row = db_class.executeAll(sql)
    print(row)

    return render_template('/main/server.html',  matching_code=matching_code, id=id, resultData=row.to_html(index=False))


# SELECT97
@server.route('/select97', methods=['GET'])
def select97():
    db_class = dbModule.Database()

    sql = "select *\
            from female_want_male\
            where id = '"+id+"'"

    row = db_class.executeAll(sql)
    print(row)

    return render_template('/main/server.html', matching_code=matching_code, id=id, resultData=row.to_html(index=False))



# SELECT96
@server.route('/select96', methods=['GET'])
def select96():
    db_class = dbModule.Database()

    sql = "select seller_id, seller_phone_number as 연락처\
            from seller"

    row = db_class.executeAll(sql)
    print(row)

    return render_template('/main/server.html', matching_code=matching_code, id=id, resultData=row.to_html(index=False))


# SELECT95
@server.route('/select95', methods=['GET'])
def select95():
    db_class = dbModule.Database()

    sql = "select product_id as 상품명, product_price as 가격\
            from product"

    row = db_class.executeAll(sql)
    print(row)

    return render_template('/main/server.html', matching_code=matching_code, id=id, resultData=row.to_html(index=False))