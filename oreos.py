import converter
import homeset
from homeset import blogs, update_dir, update_home
import subprocess
import time
import refresh_utils as rf
import page_controls as pagc

def apply_changes():
    html_folder = "./api/templates/blogs/"
    md_folder = "./md_blogs/"
    homeset.delete_html_files_without_md(html_folder, md_folder)
    rf.refresh_all_pages()
    rf.refresh_all_blogs()
    update_dir()
    update_home()
    print("Rebuilding Site...")

    subprocess.run(["git", "add", "-A"])
    subprocess.run(["git", "commit", "-m", "updated blogs"])
    subprocess.run(["git", "push"])


def run_program():
    print("""Commands:
            add blog
            add page
            update dir
            update home
            update title
            exit
            """)
    choice = input("Enter choice: ")

    while(choice != "exit"):
        if(choice == "update title"):
            pagc.update_title()
            rf.refresh_all_pages()
            rf.refresh_all_blogs()
        if(choice == "add page"):
            pagc.add_page()
        if(choice == "add blog"):
            converter.add_blog()
        elif(choice == "update dir"):
            homeset.update_dir()
        elif(choice == "update home"):
            homeset.update_home()
        choice = input("Enter choice: ")

if __name__ == "__main__":
    run_program()
    apply_changes()
