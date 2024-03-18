from server_utils import update_paths
import converter
import homeset
import refresh_utils as rf


def add_page():

    with open("title.txt", "r") as file :
        txttitle = file.readlines()
    blog_title = ''.join(txttitle)

    filename = input("Enter new page markdown file: ")
    filepath = "./md_pages/" + filename;
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

    homeset.update_dir()
    homeset.update_home()
    rf.refresh_all_pages()
    rf.refresh_all_blogs()

def update_title():

    title = input("Enter new title name: ")
    with open("title.txt", "w") as file:
        file.write(title)
    file.close()
