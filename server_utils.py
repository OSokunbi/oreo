import os

def update_paths(filename):
    redirect = filename.split('.')[0]
    additional_code = f'''@app.route('/{redirect}')
def {redirect}():
    return render_template('pages/{redirect}.html')\n
'''
    with open('./api/server.py', 'r') as file:
        if additional_code in file.read():
            print("Function already exists. Skipping update.")
            return

    with open('./api/server.py', 'r') as file:
       lines = file.readlines()

    # Find the index of the line containing "if __name__ == '__main__':"
    main_index = lines.index("@app.route('/blogs/<post_id>')\n")

    # Insert the additional code before the "if __name__ == '__main__':" line
    lines.insert(main_index, additional_code)

    with open('./api/server.py', 'w') as file:
       file.writelines(lines)
       print("Updated Routes")

special_files = ['home.html', 'dir.html']  # List of files to appear first
other_files = []  # List of other files
def update_nav():
    folder_path = "./api/templates/pages"
    for file_name in os.listdir(folder_path):
        if os.path.isfile(os.path.join(folder_path, file_name)):
            if file_name in special_files:
                special_files.remove(file_name)
                special_files.append(file_name)
            else:
                other_files.append(file_name)

        other_files.sort()

def webify_nav():
    update_nav()
    nav = """<nav><p><a href="{{ url_for('index') }}">Home</a><a href="{{ url_for('dir') }}">Blog</a>"""
    for file in other_files:
        name = file.split('.')[0]

        nav += """<a href = "{{ """
        nav += f"""url_for('{name}')"""
        nav += """ }}">"""
        nav += f"""{name.capitalize()}</a>"""
    nav += "</p></nav>"
    other_files.clear()
    return nav
