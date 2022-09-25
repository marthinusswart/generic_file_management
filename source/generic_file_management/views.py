
from flask import render_template, Blueprint

views = Blueprint('views', __name__)


@views.route('/tests', methods=['GET', 'POST'])
def test_upload():
    return render_template("test_upload.html")
