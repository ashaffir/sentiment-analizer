""" Getting started with Flask: 
    https://www.youtube.com/watch?v=lj4I_CvBnt0&ab_channel=freeCodeCamp.org
"""

from crypt import methods
from datetime import datetime
from flask import Flask, redirect, url_for, request, render_template, make_response
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import importlib_resources

import twitter

app = Flask(__name__)
app.config[
    "SQLALCHEMY_DATABASE_URI"
] = "sqlite:///posts.sqlite"  # 4 slashes (////) allow absolute path, 3 (///) relative to this location

db = SQLAlchemy(app)
migrate = Migrate(app, db)


class BlogPost(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    author = db.Column(db.String(20), nullable=False, default="N/A")
    post_date = db.Column(db.DateTime, nullable=False, default=datetime.now)

    def __str__(self) -> str:
        return f"Blog post ID: {self.id}"


@app.route(
    "/",
    methods=[
        "GET",
        "POST",
    ],
)
@app.route("/home")
async def home():
    context = {}
    if request.method == "POST":
        username = request.form["username"]
        followers = await twitter.get_user_followers(username)
        print(f"{followers[-10:]=}")
        context["followers"] = followers

    return render_template("home.html", context=context)


@app.route("/post/<int:postId>", methods=["GET", "POST"])
def post(postId):
    context = {}
    post = BlogPost.query.get_or_404(postId)
    context["post"] = post

    if request.method == "POST":
        post.title = request.form["title"]
        post.content = request.form["content"]
        post.author = request.form["author"]
        db.session.commit()
        return redirect(url_for("posts"))
    else:
        return render_template("post.html", context=context)


@app.route("/posts", methods=["GET", "POST"])
def posts():
    context = {}

    posts = BlogPost.query.order_by(BlogPost.post_date).all()

    if request.method == "POST":
        if "delete_post" in request.form:
            db.session.delete(BlogPost.query.get_or_404(request.form["delete_post"]))
            db.session.commit()
            posts = BlogPost.query.order_by(BlogPost.post_date).all()

        elif "filter" in request.form:
            filter_by = request.form["filter_by"]
            posts = BlogPost.query.filter_by(author=filter_by)
            context["posts"] = posts

        else:
            print(f"{request.form=}")
            title = request.form["title"]
            content = request.form["content"]
            author = request.form["author"]

            new_post = BlogPost(title=title, author=author, content=content)
            db.session.add(new_post)
            db.session.commit()
            posts = BlogPost.query.order_by(BlogPost.post_date).all()
            context["posts"] = posts

    context["posts"] = posts
    return render_template("posts.html", context=context)


def create_posts():
    db.session.add(
        BlogPost(title="Second post", author="Alf", content="kakakak kasdf gglaglag")
    )
    db.session.add(
        BlogPost(title="Third post", author="Alf", content="hshsh sdsd kasdf")
    )
    db.session.commit()


def inner():
    return "Inner"


# Alternative to decorate method below
app.add_url_rule("/inner", "inner page", inner)


@app.route("/guest/<name>")
def guest_page(name):
    return f"Hey there {name}"


@app.route("/admin", methods=["POST"])
def admin_page():
    return "Admin Page"


@app.route("/user/<name>")
def user_page(name):
    if name == "admin":
        return redirect(url_for("admin_page"))
    else:
        return redirect(url_for("guest_page", name=name))


@app.route("/user/<int:id>")
def user(id):
    return f"Page for user ID {id}"


@app.route("/success/<name>")
def success(name):
    return render_template("welcome.html", name=name)


@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        print(f"POST: {request.args=}")
        name = request.form["name"]

        return redirect(url_for("setcookie", name=name))
    else:
        print(f"GET: {request.args=}")
        # for name passed in URL argument after '?'
        name = request.args.get("name")
        # return render_template(url_for("success", name=name)

    return render_template("login.html")


# Coockies
@app.route("/setcookie", methods=["POST", "GET"])
def setcookie():
    if request.method == "POST":
        user = request.form["name"]

        res = make_response(render_template("readcookie.html"))
        res.set_cookie("userID", user)

        return res
    else:
        return render_template("login.html")


@app.route("/getcookie")
def getcookie():
    name = request.cookies.get("userID")
    return f"<h1>Welcome {name}</h1>"


if __name__ == "__main__":
    app.run("localhost", 8333, debug=True)
