from flask import Blueprint


bp = Blueprint("blue01", __name__, url_prefix='/blue')

@bp.route('/blue01', methods=['GET'])
def blue01():
    return 'blue01'
