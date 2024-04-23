from flask import Flask, render_template, redirect
import json

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('pages/home.html')

@app.route('/blogs')
def dir():
    return render_template('pages/dir.html')

@app.route('/blogs/<post_id>')
def get_blog(post_id):
    json_file_path = "blogs.json"
    with open(json_file_path, 'r') as json_file:
        blog_posts = json.load(json_file)
    blogs = blog_posts
    if post_id in blogs:
        link = f"{blogs[post_id]}"
        return render_template(link)
    else:
        return "Blog post not found", 404
if __name__ == '__main__':
    app.run(debug=True)
