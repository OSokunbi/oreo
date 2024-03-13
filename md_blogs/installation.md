ʕ •ᴥ•ʔ How to Install Oreo
2024-03-01
### installing and using oreo
to get started on installing and creating your blogs using oreo first create a githu repo. then create a [clone](http://github.com/OSokunbi/) of the oreo github repo. then open up your cloned repo using your code editor of choice.

now follow these commands:

```
git remote remove origin
rm -rf .git
git init
git branch -M main
git add -A
git commit -m "initial commit"
git remote add origin https://github.com/YOU/YOUR_GITHUB_REPO_NAME
git push -u origin main
```

after doing this delete the README.md file

### getting started
all pages and blogs in oreos are written in [markdown syntax](https://www.markdownguide.org/basic-syntax/)

to get started run the following command:

```
python oreos.py
```

after running this a list of options should appear, to get started first type in **update title**. this will change the title of your blog. to dorun the command in oreo:

```
update title
```

### creating the site
host your blog site using [vercel](https://vercel.com/dashboard/). simply add your blog's github repo as the github repo your vercel project should refer to and you shoudl be all set from there.

### understanding oreo commands

#### add blog
in order to add blog post you must first make a markdown file ending in **.md**. after doing this you want to drag that markdown file into the md_blogs folder. then runn the following command in oreo:

```
add blog
```

this command is pretty simple and straightforward, it will prompt you to enter the name of the blog post that you would like to add to your blog. you must then enter the name of the markdown file that you added in. for exampleif i added a new markdown file called hello.md i would type hello.md whenprompted with the name of the markdown file.

#### update home
this command is pretty simple as well, after making changes to home.md you can run the following command in oreo:

```
update home
```

this command will apply all the changes that you made in home.md to your homepage

#### update dir
another straightforward command. this command will update your blogs directory if any changes are needed that were not automatically applied during
the adding of a new post, or if you want to do things such as manually change the date that a post if attached to inside of its corresponding html file. to run this command in oreo type:

```
update dir
```

#### add page
this command will add another page to your blog site. to run this command in oreo you must first create a new markdown file for your new page in the md_pages folder and run:

```
add page
```

this will automatically rebuild the navbar to add a navigation url to your new page on every single page, including all your posts as well as add your new page.

#### exit

this commands is used to exit oreo. to run this command in oreo type:

```
exit
```

this will exit out of oreo as well as update your blog push all the changes to your blog's github repo

## structures

### md_blogs structure
here is the structure for how your markdown blogs should look:
```
First line : (Blog Title)
Second Line: (Date in this format: 2024-03-04)
(write here)
```

here's an example:

```
Example Blog
2024-01-01
(write markdown syntax here)
```

### page structures
here is the structure for how your markdown blogs should look:
```
First line : (Page Title for Navbar)
(write here)
```

here's an example:

```
Books
(write markdown syntax here)
```
