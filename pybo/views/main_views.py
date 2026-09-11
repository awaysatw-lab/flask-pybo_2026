from flask import Blueprint, url_for, redirect


#blueprint 라우팅 함수를 체계적으로 관리
bp=Blueprint('main', __name__, url_prefix='/')

@bp.route('/')
def index():
    return redirect(url_for('question._list'))
