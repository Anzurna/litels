from flask import Flask, render_template, url_for, flash, redirect
from flask import request, jsonify

from flask_wtf import CSRFProtect

from forms import RegistrationForm,LoginForm

import gensim
from gensim.test.utils import get_tmpfile

import pymongo
import numpy
import random

csrf = CSRFProtect()

app = Flask(__name__)
csrf.init_app(app)

app.config["SECRET_KEY"] = "2fd3abf73715195591fd15023f99f66c"
app.config["SESSION_COOKIE_SECURE"] = "False"

client = pymongo.MongoClient("mongodb://localhost:27017/recommender")
db = client["database"]
articles = db["articles"]


def create_user_vector():
    user_vector = []
    for i in range(0, 300):
        user_vector.append(random.uniform(-0.5, 0.5))

    user_vector = numpy.asarray(user_vector)

    return user_vector

# f = get_tmpfile(r"C:\Main Contents\Python progs\crawl_gp\litels\recommender\scripts\doc_2_vec_model")


# doc_vector = model.infer_vector(test_article["content"])

# most_similar_docs = model.docvecs.most_similar([doc_vector], topn = 20)
# print(len(most_similar_docs))
# print(most_similar_docs)
similar_articles = []

model = 0

def is_article_meets_requirements(article):
    if article["url"] != "": #article["is_long"] and
        return True
    else: 
        return False

def get_articles(doc_vector, doc_range=10, min_amount=5):
    similar_articles = []
    # doc_vector = model.infer_vector(test_article["content"])

    most_similar_docs = model.docvecs.most_similar([doc_vector], topn = doc_range)
    while len(similar_articles) < min_amount:
        most_similar_docs = model.docvecs.most_similar([doc_vector], topn = doc_range)
        for i in range(len(most_similar_docs)):
            s_a = articles.find()[int(most_similar_docs[i][0])]
            similar_articles.append({"url": s_a["url"], 
                "title": s_a["title"],
                "id": s_a["id"],
                "date": s_a["pub_date"],
                "publisher": s_a["publication"]
                })

        doc_range += 10
    return similar_articles
    

@app.route("/")
@app.route("/recommendations")
def main():
    doc_vector = create_user_vector()
    return render_template('main.html', articles=get_articles(doc_vector))

@app.route("/redirect", methods=['POST'])
def redirect_and_register_click():
    if request.method == "POST":
        print(request.json)

    resp = jsonify(success=True)
    return resp
    # return render_template('main.html', articles=get_articles())

@app.route("/register", methods=["GET", "POST"])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f"Account created for {form.username.data}", "success")
        return redirect(url_for("main"))
    print(form.csrf_token)
    return render_template("register.html", title="Register", form=form)
@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash(f"{form.email.data} logged in succesfully", "success")
        return redirect(url_for("main"))
    return render_template("login.html", title="Login", form=form)

@app.route("/setup", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash(f"{form.email.data} logged in succesfully", "success")
        return redirect(url_for("main"))
    return render_template("login.html", title="Login", form=form)




if __name__ == "__main__":
    model = gensim.models.Doc2Vec.load(r"C:\Main Contents\Python progs\crawl_gp\litels\recommender\scripts\doc_2_vec_model")
    app.run(debug=True)
    

# ButtonPressed = 0        
# @app.route('/button', methods=["GET", "POST"])
# def button():
#     if request.method == "POST":
#         ButtonPressed += 1  # Note this increment here.
#         return render_template("button.html", ButtonPressed = ButtonPressed)
#     return redirect(url_for('button'))