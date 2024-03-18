import os
import converter
from server_utils import update_paths
from homeset import update_dir
from homeset import update_home
import homeset
from datetime import datetime

def refresh_blog(filename):

    with open("title.txt", "r") as file :
        txttitle = file.readlines()
    blog_title = ''.join(txttitle)

    html_filename = "./api/templates/blogs/" + filename.split('.')[0] + '.html'
    filename = "./md_blogs/" + filename
    nav, title, time, content = converter.convert_markdown_blog(filename)
    styles = """<link rel="stylesheet" type="text/css" href="{{ url_for('static', filename='styles.css') }}">"""
    style = """<link rel="stylesheet" type="text/css" href="{{ url_for('static', filename='style.css') }}">"""

    input_date = datetime.strptime(time, "%Y-%m-%d")
    input_date = input_date.date()
    formatted_date = input_date.strftime("%d %b, %Y")

    formatted_date = input_date.strftime("%d %b, %Y")

    scripts = '''<script type="text/javascript"
            src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.4/MathJax.js?config=TeX-AMS_HTML-full"></script>
    <script type="text/x-mathjax-config">
        MathJax.Hub.Config({
            tex2jax: {
                inlineMath: [["$", "$"], ["\\\\(", "\\\\)"]],
                displayMath: [["$$", "$$"], ["\\\\[", "\\\\]"]],
                processEscapes: true
            },
            config: ["MMLorHTML.js"],
            jax: ["input/TeX", "output/HTML-CSS", "output/NativeMML"],
            extensions: ["MathMenu.js", "MathZoom.js"]
        });
    </script>'''

    formatted_blog = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>{title} | {blog_title}</title>
        {style}
        {styles}
        {scripts}
    </head>
    <header>
    <a class="title" href=""> <h1> {blog_title} </h1> </a>
        {nav}
        </header>
        <main>
        <h1>{title}</h1>
        <p>
            <i>
            <time datetime="{input_date}">{formatted_date}</time></i>
            </p>
            <body>
            {content}
            </body>
            </main>
            <footer style="padding:25px 0;">
                <span>
                built with <a href="https://github.com/OSokunbi/oreo">oreo</a>
                </span>
            </footer>
            </html>
            """
    with open(html_filename, 'w') as file:
        file.write(formatted_blog)
    print("Refreshed", html_filename)

def refresh_page(filename):
    filepath = "./md_pages/" + filename;
    with open("title.txt", "r") as file :
        txttitle = file.readlines()
    blog_title = ''.join(txttitle)

    with open(f"./api/templates/pages/{filename.split('.')[0]}.html", 'w') as file:
        file.write("")
    nav, title, content = converter.convert_markdown_file(filepath)
    update_paths(filename)

    styles = """<link rel="stylesheet" type="text/css" href="{{ url_for('static', filename='styles.css') }}">"""
    style = """<link rel="stylesheet" type="text/css" href="{{ url_for('static', filename='style.css') }}">"""

    formatted_page = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>{title} | {blog_title}</title>
        {style}
        {styles}
        </head>
        <header>
        <a class="title" href=""> <h1> {blog_title} </h1> </a>
        {nav}
        </header>
    <main>
        {content}
    </main>
    <footer style="padding:25px 0;">
        <span>
        built with <a href="https://github.com/OSokunbi/oreo">oreo</a>
        </span>
    </footer>
        </html>
        """
    with open(f"./api/templates/pages/{filename.split('.')[0]}.html", 'w') as file:
        file.write(formatted_page)

    print(f"Refreshed {filename.split('.')[0] + '.html'}")

def refresh_all_pages():
    html_folder = "./api/templates/pages/"
    md_folder = "./md_pages/"
    homeset.delete_html_files_without_md(html_folder, md_folder)
    special_files = ['home.html', 'dir.html']
    folder_path = "./api/templates/pages/"
    html_files = os.listdir(folder_path)
    for html_file in html_files:
        if html_file.endswith('.html') and not html_file in special_files:
            md_eq = os.path.splitext(html_file)[0] + ".md"
            refresh_page(md_eq)

    update_dir()
    update_home()

def refresh_all_blogs():
    folder_path = "./api/templates/blogs/"
    html_files = os.listdir(folder_path)
    for html_file in html_files:
        if html_file.endswith('.html'):
            md_eq = os.path.splitext(html_file)[0] + ".md"
            refresh_blog(md_eq)
