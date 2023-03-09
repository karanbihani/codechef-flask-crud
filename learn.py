from flask import Flask
from markupsafe import escape

app = Flask(__name__)

@app.route('/')
def hello_world():
    return "Hello World"

@app.route('/<name>') #<> captures the route name
def hello_user(name):
    return f"Hello, {escape(name)}"

@app.route('/post/<int:post_id>') # This is called a converter it can take many diff types
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return f'Post {post_id}'

# Converter type: 
# 1. String (default) accept any text without a slash
# 2. int accepts positive int
# 3. float accepts positive floating pt cals
# 4. path like string but also accepts slashes
# 5. uuid accepts UUID strings

# if "/projects/" then "/projects/" and "/projects" both have same link/route
# but if "project" then only that works "/project/ throws 404 error

if __name__ == "__main__":
    app.run()

