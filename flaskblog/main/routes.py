from flask import Blueprint, request, render_template

from flaskblog.models import Post

main = Blueprint('main', __name__)

@main.route('/')
def index():
    page = request.args.get('page', 1, type=int)
    posts = Post.query.order_by(Post.date_posted.desc()).paginate(per_page=2, page=page)
    return render_template('index.html', title='Home', posts=posts)

@main.route('/about')
def about():
    return render_template('about.html', title='About')