
from flask import (
    Blueprint,redirect,render_template,flash,url_for,request,g,jsonify,make_response
)
from werkzeug.exceptions import abort
from app.web.auth import login_required
from app.web.db import get_db
from app.manage.main import Core

bp = Blueprint('server',__name__)


@bp.route('/')
def index():
    #serverid = ['10001','10002','10003','10004','10005','10006',]
    core = Core()
    serverids = core.init_serid()
    php = request.args.get('api',default=None)
    #print(serverids)
    if php:
        return jsonify(serverids)

    return render_template('server/index.html', posts=serverids)


@bp.route('/create')
def create():
    return 'Server create'

@bp.route('/update',methods = ('GET','POST'))
def update():
    return 'Server update'


@bp.route('/start')
def start():
    #print(request.args)
    serid = request.args['id'].split(',')
    k = request.args['stype']

    m = Core()

    return m.main(k, serid)


@bp.route('/add')
def add_numbers():

    serid = request.args.get('serid', 0,)  # serid
    stype = request.args.get('stype', 0, type=int)  # k
    serid = str(serid)

    if stype not in [1, 2, 3]:  # 操作状态
        return jsonify(result={serid: 4})

    m = Core()
    res = m.main(serid, stype)

    response = make_response(jsonify(result=res))
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Methods'] = 'POST'
    response.headers['Access-Control-Allow-Headers'] = 'x-requested-with,content-type'
    return response
    #return jsonify(result=res)


@bp.route('/test')
def test():
    response = make_response(jsonify(response=get_articles(ARTICLES_NAME)))
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Methods'] = 'POST'
    response.headers['Access-Control-Allow-Headers'] = 'x-requested-with,content-type'

    return render_template('server/test.html')