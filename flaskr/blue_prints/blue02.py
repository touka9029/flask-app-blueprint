from flask import Blueprint


bp = Blueprint("blue02", __name__, url_prefix='/blue')

@bp.route('/blue02', methods=['GET'])
def blue01():
    return 'blue02'
