import os
from flask import Flask, render_template, request, flash, redirect, url_for
from application.models import Influencers, Sponsors, Admin, Ad_Request, Campaigns
from flask import current_app as app
from .database import db



@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

@app.route("/admin_login",methods=["GET"])
def admin_login():
    return render_template("admin_login.html")

@app.route("/users",methods=["GET"])
def users():
    return render_template("users.html")

@app.route("/admin_details", methods=["GET","POST"])
def admin_details():
    username = request.form.get("username")
    password = request.form.get("password")

    u = Admin.query.filter_by(username = username)
    if(u):
        return render_template("admin_dashboard.html")
    else:
        return render_template("login_error.html")
    
@app.route("/sponsor",methods=["GET"])
def sponsor():
    return render_template("sponsor_login.html")

@app.route("/influencer",methods=["GET"])
def influencer():
    return render_template("influencer_login.html")

@app.route("/influencer_login", methods=["GET","POST"])
def influencer_login():
    username = request.form.get("username")
    password = request.form.get("password")
    u = Influencers.query.filter_by(username = username).first()
    if(u.password == password):
        return redirect("/influencer_dashboard/{u.id}")
    else:
        return render_template("login_error.html")

@app.route("/sponsor_login", methods=["GET","POST"])
def sponsor_login():
    username = request.form.get("username")
    password = request.form.get("password")  
    u = Sponsors.query.filter_by(username = username).first()
    uid = u.id
    if(u.password == password):
        return redirect(f'/sponsor_dashboard/{uid}')
    else:
        return render_template("login_error.html")

@app.route("/influencer_register",methods=["GET","POST"])
def influencer_register():
    return render_template("influencer_register.html")

@app.route("/influencer_details", methods=["GET","POST"])
def influencer_details():
    if request.method =="POST":
        fname = request.form.get("fname")
        lname = request.form.get("fname")
        city = request.form.get("city")
        uname = request.form.get("username")
        category = request.form.get("category")
        niche = request.form.get("niche")
        email = request.form.get("mail")
        password = request.form.get("password")

        u = Influencers.query.filter_by(username = uname).first()
        e = Influencers.query.filter_by(email = email).first()
        if(u):
            print("User already Exists")
            flash("User already exists!!!")
            return render_template("influencer_register.html")

        if(e):
            print("email already Exists")
            flash("email already exists!!!")
            return render_template("influencer_register.html")
    
        new_influencer = Influencers(fname = fname, lname = lname, city = city, username = uname, category = category, niche = niche, email = email, password = password)
        db.session.add(new_influencer)
        db.session.commit()
        return render_template("influencer_login.html")

@app.route("/sponsor_register",methods=["GET","POST"])
def sponsor_register():
    return render_template("sponsor_register.html")

@app.route("/sponsor_details", methods=["GET","POST"])
def sponsor_details():
    company = request.form.get("company")
    city = request.form.get("city")
    industry = request.form.get("industry")
    budget = request.form.get("budget")
    uname = request.form.get("username")
    email = request.form.get("email")
    password = request.form.get("password")

    u = Influencers.query.filter_by(username = uname).first()
    e = Influencers.query.filter_by(email = email).first()
    if(u):
        print("User already Exists")
        flash("User already exists!!!")
        return redirect(url_for('sponsor_register'))
    if(e):
        print("User already Exists")
        flash("User already exists!!!")
        return redirect(url_for('sponsor_register'))
 
    new_sponsor = Sponsors(company = company, city = city, industry = industry, budget = budget,  username = uname, email = email, password = password)
    db.session.add(new_sponsor)
    db.session.commit()
    return render_template("sponsor_login.html")

@app.route("/login_error", methods=["GET","POST"])
def login_error():
    return render_template("login_error.html")

@app.route("/add_campaigns/<int:uid>", methods=["POST","GET"])
def add_campaigns(uid):
    name = request.form.get("name")
    description = request.form.get("description")
    startdate = request.form.get("startdate")
    enddate = request.form.get("enddate")
    budget = request.form.get("budget")
    visibility = request.form.get("radio1")
    goals = request.form.get("goals")
    new_campaign = Campaigns(name = name, description=description, start_date = startdate, end_date = enddate, budget = budget, visibility = visibility, goals = goals, sponsor_id = uid)
    db.session.add(new_campaign)
    db.session.commit()
    return redirect(f'/sponsor_dashboard/{uid}')


@app.route("/influencer_dashboard/<int:uid>",methods=["GET","POST"])
def influencer_dashboard(uid):
    influencer = Influencers.query.filter_by(id = uid).first()
    return render_template("influencer_dashboard.html",d=influencer)


@app.route("/sponsor_dashboard/<int:uid>",methods=["GET","POST"])
def sponsor_dashboard(uid):
    sponsor = Sponsors.query.filter_by(id = uid).first()
    campaigns = Campaigns.query.filter_by(sponsor_id = uid).all()
    return render_template("sponsor_dashboard.html",d=sponsor, c = campaigns)
  
'''
@app.route("/admin_dashboard",methods=["GET","POST"])
def admin_dashboard():
    return render_template("admin_dashboard.html")  

@app.route("/profile_influencer",methods=["GET","POST"])
def profile_influencer():
    return render_template("influencer_dashboard.html",name="Hariharan")

@app.route("/find_influencer",methods=["GET","POST"])
def find_influencer():
    return render_template("influencer_dashboard.html",find="Hariharan")

'''