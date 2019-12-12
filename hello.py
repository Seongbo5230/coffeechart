from flask import Flask, escape, url_for, request, render_template
app = Flask(__name__)

@app.route('/')
def index():
  return "Index Page"

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)

@app.route('/login', methods=['GET', 'POST'])
def login():
  if request.method == 'POST':
    return do_the_login()
  else:
    return show_the_login_form()

@app.route('/user/<username>')
def profile(username):
  # show the user profile for that user
  return '{}\'s profile'.format(escape(username))

# with app.test_request_context():
#   print(url_for('index'))
#   print(url_for('login'))
#   print(url_for('login', next='/'))
#   print(url_for('profile', username="Seong Bo"))

@app.route('/post/<int:post_id>')
def show_post(post_id):
  #show the post with the given id, the id is an int
  return 'Post %d' % post_id

@app.route('/path/<path:subpath>')
def show_subpath(subpath):
  # show the subpath after /path/
  return 'Subpath %s' % escape(subpath)

@app.route('/projects/')
def projects():
  # The canonical URL for the projects endpoint has a trailing slash.
  # It’s similar to a folder in a file system. 
  # If you access the URL without a trailing slash, Flask redirects you to the canonical URL with the trailing slash.
  return 'The project page'

@app.route('/about')
def about():
  # The canonical URL for the about endpoint does not have a trailing slash.
  # It’s similar to the pathname of a file.
  # Accessing the URL with a trailing slash produces a 404 “Not Found” error. 
  # This helps keep URLs unique for these resources, which helps search engines avoid indexing the same page twice.
  return 'The about page'
