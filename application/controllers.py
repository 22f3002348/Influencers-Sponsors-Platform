import os
from flask import Flask, render_template, request
from application.models import Influencers
from flask import current_app as app



@app.route("/influencer_details", methods=["GET","POST"])
def influencer_details():
    fname = request.form.get("fname")
    lname = request.form.get("fname")
    city = request.form.get("city")
    uname = request.form.get("username")
    category = request.form.get("category")
    niche = request.form.get("niche")
    email = request.form.get("mail")
    password = request.form.get("password")

    u = Influencers.query.filter(Influencers.username == uname)
    print("User:........",u)
    return render_template("influencer_login.html")

@app.route("/influencer_register",methods=["GET","POST"])
def influencer_register():
    return render_template("influencer_register.html")


@app.route("/influencer_dashboard",methods=["GET","POST"])
def influencer_dashboard():
    data ={
        "name":"Hariharan",
        "username":"Hari",
        "email":"hari@gmail.com",
        "category":"Food",
        "niche":"Street Food"
    }
    return render_template("influencer_dashboard.html",d= data)

@app.route("/sponsor_dashboard",methods=["GET","POST"])
def sponsor_dashboard():
    data ={
        "name":"Harry",
        "username":"harry",
        "email":"harry@gmail.com",
        "company":"Tata",
        "city":"Chennai"
    }
    return render_template("sponsor_dashboard.html",d= data)  

@app.route("/admin_dashboard",methods=["GET","POST"])
def admin_dashboard():
    return render_template("admin_dashboard.html")  

'''@app.route("/profile_influencer",methods=["GET","POST"])
def profile_influencer():
    return render_template("influencer_dashboard.html",name="Hariharan")

@app.route("/find_influencer",methods=["GET","POST"])
def find_influencer():
    return render_template("influencer_dashboard.html",find="Hariharan")'''

