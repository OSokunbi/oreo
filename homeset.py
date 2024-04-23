import os
from bs4 import BeautifulSoup
import converter
import markdown
import json
import re
import server_utils as su
from datetime import datetime

blogs = {}
def update_home():

    with open("title.txt", "r") as file :
        txttitle = file.readlines()
    blog_title = ''.join(txttitle)

    with open("./md_pages/home.md", 'r') as file:
        homecontent = file.readlines()
    home = ''.join(homecontent)
    content = markdown.markdown(home)
    styles = """<link rel="stylesheet" type="text/css" href="{{ url_for('static', filename='styles.css') }}">"""
    style = """<link rel="stylesheet" type="text/css" href="{{ url_for('static', filename='style.css') }}">"""
    nav = su.webify_nav()
    formatted_blog = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>ᕕʕ •.• ʔ୨ oreoluwa's blog</title>
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

    with open("./api/templates/pages/home.html", 'w') as file:
        file.write(formatted_blog)

    print(f"Home page updated successfully!")

def generate_directory(folder_path):
    directory = {}
    for filename in os.listdir(folder_path):
        if filename.endswith('.md'):
            key = (filename.split('.')[0])
            blogs[key] = '/blogs/' + filename.split('.')[0] + ".html"
            with open(os.path.join(folder_path, filename), 'r') as file:
                first_line = file.readline().strip()
                directory[filename] = first_line
    return directory

def update_dir():

    with open("title.txt", "r") as file :
        txttitle = file.readlines()
    blog_title = ''.join(txttitle)

    folder_path = "./md_blogs/"
    directory = generate_directory(folder_path)
    blog_list = ""
    blog_entries = []
    for filename, title in directory.items():
        filename = filename.split('.')[0]
        link_to_file = f""" "{{ url_for('get_blog', post_id='{filename}') }}" """
        with open(f'./api/templates/blogs/{filename}.html', 'r', encoding='utf-8') as file:
            html_content = file.read()

        soup = BeautifulSoup(html_content, 'html.parser')

        pattern = r'datetime="([^"]+)"'
        match = re.search(pattern, html_content)

        datetime_value = match.group(1)
        date_object = datetime.strptime(datetime_value, "%Y-%m-%d")

        blog_entries.append((filename, date_object, title, link_to_file))
    blog_entries.sort(key=lambda x: x[1], reverse=True)

    for entry in blog_entries:
        filename, date_object, title, link_to_file = entry
        formatted_date = date_object.strftime("%d %b, %Y")
        blog_list +=  f"<span><time>{formatted_date}</span>" + f"<a href ={link_to_file}>{title}</a><br>"


    nav = su.webify_nav()
    dir = format_links(blog_list)
    styles = """<link rel="stylesheet" type="text/css" href="{{ url_for('static', filename='styles.css') }}">"""
    style = """<link rel="stylesheet" type="text/css" href="{{ url_for('static', filename='style.css') }}">"""


    formatted_dir = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Blogs | {blog_title}</title>
        {style}
        {styles}
        </head>
        <header>
        <a class="title" href=""> <h1> {blog_title} </h1> </a>
        {nav}
        </header>
    <main>
        <p class='blog-posts'>
            {dir}
        </p>
        </main>
        <footer style="padding:25px 0;">
            <span>
            built with <a href="https://github.com/OSokunbi/oreo">oreo</a>
            </span>
        </footer>
        </html>
        """

    with open("./api/templates/pages/dir.html", 'w') as file:
        file.write(formatted_dir)

    print(f"Directory updated successfully!")
    json_file_path = "blogs.json"
    with open(json_file_path, 'w') as json_file:
        json.dump(blogs, json_file)

    print("Blogs saved to JSON file:", json_file_path)

def format_links(input_string):
    output_string = input_string.replace("{", "{{")
    output_string = output_string.replace("}", "}}")
    return output_string

def delete_html_files_without_md(html_folder, md_folder):
    html_files = os.listdir(html_folder)
    for html_file in html_files:
        if html_file.endswith('.html'):
            filename_without_extension = os.path.splitext(html_file)[0]
            md_file_path = os.path.join(md_folder, filename_without_extension + '.md')
            if not os.path.exists(md_file_path):
                html_file_path = os.path.join(html_folder, html_file)
                os.remove(html_file_path)
                print(f"Deleted {html_file} because corresponding .md file doesn't exist.")
