import markdown
from markdown.extensions.codehilite import CodeHiliteExtension
from markdown.extensions.tables import TableExtension
from datetime import datetime
import homeset
import server_utils as su

with open("title.txt", "r") as file :
    txttitle = file.readlines()
blog_title = ''.join(txttitle)

def convert_markdown_file(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
    title = lines[0]
    markdown_text = ''.join(lines[1:])

    # Configure CodeHiliteExtension with the necessary parameters
    extensions = ['fenced_code', 'codehilite']
    extension_configs = {
        'codehilite': {
            'use_pygments': True,
            'css_class': 'highlight',
            'linenums': False,         # Enable line numbers
            'guess_lang': False,       # Disable language guessing
        }
    }
    codehilite_extension = CodeHiliteExtension(css_class='codehilite', linenums=False)
    nav = su.webify_nav()
    html = markdown.markdown(markdown_text, extensions=[codehilite_extension, 'fenced_code', 'mdx_math', TableExtension(use_align_attribute=True)])

    return nav, title, html

# Example Markdown text
def convert_markdown_blog(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
    title = lines[0]
    date = lines[1].strip()
    markdown_text = ''.join(lines[2:])
    extensions = ['fenced_code', 'codehilite']
    extension_configs = {
        'codehilite': {
        'use_pygments': True,
        'css_class': 'highlight',
        'linenums': False,         # Enable line numbers
        'guess_lang': False,       # Disable language guessing
        }
    }
    codehilite_extension = CodeHiliteExtension(css_class='codehilite', linenums=False)
    nav = su.webify_nav()
    html = markdown.markdown(markdown_text, extensions=[codehilite_extension, 'fenced_code', 'mdx_math', TableExtension(use_align_attribute=True)])

    return nav, title, date, html

def add_blog():
    filename = input("Enter markdown file name: ")
    html_filename = "./api/templates/blogs/" + filename.split('.')[0] + '.html'
    filename = "./md_blogs/" + filename
    print(html_filename)
    nav, title, time, content = convert_markdown_blog(filename)
    styles = """<link rel="stylesheet" type="text/css" href="{{ url_for('static', filename='styles.css') }}">"""
    style = """<link rel="stylesheet" type="text/css" href="{{ url_for('static', filename='style.css') }}">"""

    input_date = datetime.strptime(time, "%Y-%m-%d")
    input_date = input_date.date()
    formatted_date = input_date.strftime("%d %b, %Y")
    print(input_date)

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

    print(f"HTML output saved to {html_filename}")
    homeset.update_dir()
