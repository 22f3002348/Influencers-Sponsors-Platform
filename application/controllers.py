import math
import os
from flask import Flask, render_template, request, flash, redirect, url_for
from sqlalchemy import and_, or_
from application.models import Influencers, Sponsors, Admin, Ad_Request, Campaigns
from flask import current_app as app
from .database import db
from datetime import datetime
import matplotlib.pyplot as plt
from sqlalchemy.orm import joinedload

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
    u = Admin.query.filter_by(username = username).first()
    if(u):
        if(u.password == password):
            return redirect(f'/admin_dashboard/{u.id}')
        else:
            return render_template("login_error.html")
    else:
        return render_template("login_error.html")

@app.route("/admin_dashboard/<int:aid>", methods=["GET","POST"])
def admin_dashboard(aid):
    ads = Ad_Request.query.all()
    inf = Influencers.query.all()
    spon = Sponsors.query.all()
    cam = Campaigns.query.all()
    imagepaths =[]

    figure, axes = plt.subplots()
    users = {"Influencers":len(inf), "Sponsors": len(spon)}
    axes.bar(users.keys(), users.values())
    imagename = f'Admin{aid}_users.jpg'
    imagepath = os.path.join('static', 'images', imagename)
    plt.title(f'Total Active Users')
    plt.xlabel("Users")
    plt.ylabel("Number")
    plt.savefig(imagepath)
    imagepaths.append(imagepath)

    f_inf = Influencers.query.filter_by(flag=1).all()
    f_spon = Sponsors.query.filter_by(flag=1).all()

    figure, axes2 = plt.subplots()
    users = {"Flagged Influencers":len(f_inf), "Flagged Sponsors": len(f_spon)}
    axes2.bar(users.keys(), users.values())
    imagename = f'Admin{aid}_flagged_users.jpg'
    imagepath = os.path.join('static', 'images', imagename)
    plt.title(f'Total Flagged Users')
    plt.xlabel("Users")
    plt.ylabel("Number")
    plt.savefig(imagepath)
    imagepaths.append(imagepath)

    camp = Campaigns.query.filter_by(flag =0).all()
    f_cam = Campaigns.query.filter_by(flag =1).all()

    figure, axes3 = plt.subplots()
    users = {"Campaigns":len(camp), "Flagged Campaigns": len(f_cam)}
    axes3.bar(users.keys(), users.values())
    imagename = f'Admin{aid}_flagged_campaigns.jpg'
    imagepath = os.path.join('static', 'images', imagename)
    plt.title(f'Flagged and Active Campaigns')
    plt.xlabel("Campaigns")
    plt.ylabel("Number")
    plt.savefig(imagepath)
    imagepaths.append(imagepath)

    return render_template("admin_dashboard.html",aid = aid, ads = ads,status = imagepaths, inf = inf, spon = spon, cam = cam)

@app.route("/flag_campaign/<int:fid>/<int:aid>", methods = ["GET","POST"])
def flag_campaign(fid,aid):
    f = Campaigns.query.filter_by(id = fid).first()
    f.flag = 1
    db.session.commit()
    return redirect(f'/admin_dashboard/{aid}')


@app.route("/unflag_campaign/<int:fid>/<int:aid>", methods = ["GET","POST"])
def unflag_campaign(fid,aid):
    f = Campaigns.query.filter_by(id = fid).first()
    f.flag = 0
    db.session.commit()
    return redirect(f'/admin_dashboard/{aid}')


@app.route("/flag_influencer/<int:fid>/<int:aid>", methods = ["GET","POST"])
def flag_influencer(fid,aid):
    f = Influencers.query.filter_by(id = fid).first()
    f.flag = 1
    db.session.commit()
    return redirect(f'/admin_dashboard/{aid}')


@app.route("/unflag_influencer/<int:fid>/<int:aid>", methods = ["GET","POST"])
def unflag_influencer(fid,aid):
    f = Influencers.query.filter_by(id = fid).first()
    f.flag = 0
    db.session.commit()
    return redirect(f'/admin_dashboard/{aid}')


@app.route("/flag_sponsor/<int:fid>/<int:aid>", methods = ["GET","POST"])
def flag_sponsor(fid,aid):
    f = Sponsors.query.filter_by(id = fid).first()
    f.flag = 1
    db.session.commit()
    return redirect(f'/admin_dashboard/{aid}')


@app.route("/unflag_sponsor/<int:fid>/<int:aid>", methods = ["GET","POST"])
def unflag_sponsor(fid,aid):
    f = Sponsors.query.filter_by(id = fid).first()
    f.flag = 0
    db.session.commit()
    return redirect(f'/admin_dashboard/{aid}')

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
    if(u):
        if(u.password == password):
            return redirect(f'/influencer_dashboard/{u.id}')
        else:
            return render_template("login_error.html")
    else:
        return render_template("login_error.html")

@app.route("/sponsor_login", methods=["GET","POST"])
def sponsor_login():
    username = request.form.get("username")
    password = request.form.get("password")  
    u = Sponsors.query.filter_by(username = username).first()
    if(u):
        uid = u.id
        if(u.password == password):
            return redirect(f'/sponsor_dashboard/{uid}')
        else:
            return render_template("login_error.html")
    else:
        return render_template("login_error.html")

@app.route("/influencer_register",methods=["GET","POST"])
def influencer_register():
    return render_template("influencer_register.html")

@app.route("/influencer_details", methods=["GET","POST"])
def influencer_details():
    if request.method =="POST":
        fname = request.form.get("fname")
        lname = request.form.get("lname")
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
            flash("Username already exists!!!")
            return render_template("influencer_register.html")

        if(e):
            print("email already Exists")
            flash("Email already exists!!!")
            return render_template("influencer_register.html")
    
        new_influencer = Influencers(fname = fname, lname = lname, city = city, username = uname, category = category, niche = niche, email = email, password = password, flag=0, earnings = 0.0)
        db.session.add(new_influencer)
        db.session.commit()
        return render_template("influencer_login.html")

@app.route("/edit_influencer_details/<int:iid>", methods=["GET","POST"])
def edit_influencer_details(iid):
    influencer = Influencers.query.get(iid)
    uname = request.form.get("username")
    email = request.form.get("email")
    u = Influencers.query.filter_by(username = uname).first()
    e = Influencers.query.filter_by(email = email).first()
    if(u):
        if(u.username == uname): 
            if(u.id != iid):
                print("User already Exists")
                flash("Username already exists!!!")
                return redirect(f'/influencer_dashboard/{iid}')
    if(e):
        if(u.email == email):
            if(u.id != iid):
                print("User already Exists")
                flash("Email already exists!!!")
                return redirect(f'/influencer_dashboard/{iid}')
    influencer.fname = request.form.get("fname")
    influencer.lname = request.form.get("lname")
    influencer.city = request.form.get("city")
    influencer.username = uname
    influencer.category = request.form.get("category")
    influencer.niche = request.form.get("niche")
    influencer.email = email
    influencer.password = request.form.get("password")    
    db.session.commit()
    return redirect(f'/influencer_dashboard/{iid}')

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

    u = Sponsors.query.filter_by(username = uname).first()
    e = Sponsors.query.filter_by(email = email).first()
    if(u):
        print("User already Exists")
        flash("User already exists!!!")
        return redirect(url_for('sponsor_register'))
    if(e):
        print("User already Exists")
        flash("Email already exists!!!")
        return redirect(url_for('sponsor_register'))
 
    new_sponsor = Sponsors(company = company, city = city, industry = industry, budget = budget,  username = uname, email = email, password = password, flag=0)
    db.session.add(new_sponsor)
    db.session.commit()
    return render_template("sponsor_login.html")

@app.route("/edit_sponsor_details/<int:sid>", methods=["GET","POST"])
def edit_sponsor_details(sid):
    sponsor = Sponsors.query.get(sid)
    uname = request.form.get("username")
    email = request.form.get("email")
    u = Sponsors.query.filter_by(username = uname).first()
    e = Sponsors.query.filter_by(email = email).first()
    if(u):
        if(u.username == uname): 
            if(u.id != sid):
                print("User already Exists")
                flash("User already exists!!!")
                return redirect(f'/sponsor_dashboard/{sid}')
    if(e):
        if(u.email == email):
            if(u.id != sid):
                print("User already Exists")
                flash("email already exists!!!")
                return redirect(f'/sponsor_dashboard/{sid}')
    sponsor.company = request.form.get("company")
    sponsor.city = request.form.get("city")
    sponsor.industry = request.form.get("industry")
    sponsor.budget = request.form.get("budget")
    sponsor.username = uname
    sponsor.email = email
    sponsor.password = request.form.get("password")    
    db.session.commit()
    return redirect(f'/sponsor_dashboard/{sid}')


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
    category = request.form.get("category")
    visibility = request.form.get("visibility")
    goals = request.form.get("goals")
    progress = 0.0
    new_campaign = Campaigns(name = name, description=description, start_date = startdate, end_date = enddate, budget = budget, category=category ,visibility = visibility, goals = goals, sponsor_id = uid, progress = progress, flag=0)
    db.session.add(new_campaign)
    db.session.commit()
    return redirect(f'/sponsor_dashboard/{uid}')

@app.route("/edit_campaigns/<int:cid>", methods=["POST","GET"])
def edit_campaigns(cid):
    campaign = Campaigns.query.filter_by(id = cid).first()
    campaign.name = request.form.get("name")
    campaign.description = request.form.get("description")
    campaign.start_date = request.form.get("startdate")
    campaign.end_date = request.form.get("enddate")
    campaign.budget = request.form.get("budget")
    campaign.category = request.form.get("category")
    campaign.visibility = request.form.get("visibility")
    campaign.goals = request.form.get("goals")
    db.session.commit()
    return redirect(f'/sponsor_dashboard/{campaign.sponsor_id}')


@app.route("/delete_campaigns/<int:cid>", methods=["POST","GET"])
def delete_campaigns(cid):
    campaign = Campaigns.query.get(cid)
    sid = campaign.sponsor_id
    db.session.delete(campaign)
    db.session.commit()
    return redirect(f'/sponsor_dashboard/{sid}')

@app.route("/ad_request/<int:cid>", methods=["POST","GET"])
def ad_request(cid):
    campaign_id = cid
    campaign = Campaigns.query.filter_by(id = campaign_id).first()
    influencer_id = request.form.get("influencer_id")
    messages = request.form.get("messages")
    requirements = request.form.get("requirements")
    payment = request.form.get("payment")
    status = "Pending"
    existing_ad = Ad_Request.query.filter(Ad_Request.campaign_id == campaign.id, Ad_Request.influencer_id == influencer_id).first()
    if(existing_ad): 
        flash("Request already given to the Influencer")
        return redirect(f'/sponsor_dashboard/{campaign.sponsor_id}')   
    new_ad = Ad_Request(campaign_id = campaign_id, influencer_id = influencer_id, messages = messages, requirements = requirements, payment = payment, status = status, last_modified_by = campaign.sponsor.company)
    db.session.add(new_ad)
    db.session.commit()    
    return redirect(f'/sponsor_dashboard/{campaign.sponsor_id}')

@app.route("/influencer_ad_request/<int:iid>/<int:cid>", methods=["POST","GET"])
def influencer_ad_request(iid,cid):
    campaign_id = cid
    campaign = Campaigns.query.filter_by(id = campaign_id).first()
    influencer_id = iid
    messages = request.form.get("messages")
    requirements = request.form.get("requirements")
    payment = request.form.get("payment")
    status = "Pending"
    existing_request = Ad_Request.query.filter(Ad_Request.campaign_id == campaign_id, Ad_Request.influencer_id == influencer_id).first()
    if(existing_request):
        flash("Request Already Given!")
        return redirect(f'/influencer_dashboard/{iid}')
    influencer = Influencers.query.filter_by(id=influencer_id).first()
    new_ad = Ad_Request(campaign_id = campaign_id, influencer_id = influencer_id, messages = messages, requirements = requirements, payment = payment, status = status, last_modified_by = influencer.username)
    db.session.add(new_ad)
    db.session.commit()    
    return redirect(f'/influencer_dashboard/{iid}')

@app.route("/edit_ad_request/<int:rid>", methods=["POST","GET"])
def edit_ad_request(rid):
    ad_request_id = rid
    ad = Ad_Request.query.filter_by(id = ad_request_id).first()
    existing_ad = Ad_Request.query.filter(Ad_Request.campaign_id == ad.campaigns.id, Ad_Request.influencer_id == request.form.get("influencer_id"))
    if(existing_ad): 
        flash("Request already given to the Influencer")
        return redirect(f'/sponsor_dashboard/{ad.campaigns.sponsor_id}')
    ad.influencer_id = request.form.get("influencer_id")
    ad.messages = request.form.get("messages")
    ad.requirements = request.form.get("requirements")
    ad.payment = request.form.get("payment")
    ad.last_modified_by = ad.campaigns.sponsor.company
    ad.status = "Pending"
    db.session.commit()    
    return redirect(f'/sponsor_dashboard/{ad.campaigns.sponsor_id}')

@app.route("/delete_ad_request/<int:rid>", methods=["POST","GET"])
def delete_ad_request(rid):
    ad = Ad_Request.query.get(rid)
    sid = ad.campaigns.sponsor_id
    db.session.delete(ad)
    db.session.commit()    
    return redirect(f'/sponsor_dashboard/{sid}')

@app.route("/modified_ad_request/<int:rid>", methods=["POST","GET"])
def modified_ad_request(rid):
    ad = Ad_Request.query.get(rid)
    ad.messages = request.form.get("messages")
    ad.requirements = request.form.get("requirements")
    ad.payment = request.form.get("payment")
    ad.last_modified_by = ad.influencer.username
    db.session.commit()    
    return redirect(f'/influencer_dashboard/{ad.influencer_id}')

@app.route("/accept_ad_request/<int:rid>", methods=["POST","GET"])
def accept_ad_request(rid):
    ad = Ad_Request.query.get(rid)
    ad.status = "Accepted"
    #ad.last_modified_by = ad.influencer.username
    db.session.commit()    
    return redirect(f'/influencer_dashboard/{ad.influencer_id}')

@app.route("/sponsor_accept_ad_request/<int:rid>", methods=["POST","GET"])
def sponsor_accept_ad_request(rid):
    ad = Ad_Request.query.get(rid)
    ad.status = "Accepted"
    #ad.last_modified_by = ad.campaigns.sponsor.username
    db.session.commit()    
    return redirect(f'/sponsor_dashboard/{ad.campaigns.sponsor_id}')

@app.route("/reject_ad_request/<int:rid>", methods=["POST","GET"])
def reject_ad_request(rid):
    ad = Ad_Request.query.get(rid)
    ad.status = "Rejected"
    #ad.last_modified_by = ad.influencer.username
    db.session.commit()    
    return redirect(f'/influencer_dashboard/{ad.influencer_id}')

@app.route("/sponsor_reject_ad_request/<int:rid>", methods=["POST","GET"])
def sponsor_reject_ad_request(rid):
    ad = Ad_Request.query.get(rid)
    ad.status = "Rejected"
    #ad.last_modified_by = ad.campaigns.sponsor.username
    db.session.commit()    
    return redirect(f'/sponsor_dashboard/{ad.campaigns.sponsor_id}')

@app.route("/search_influencer/<int:uid>",methods = ["GET","POST"])
def search_influencer(uid):
    search = request.form.get("search-influencer")
    influencers = Influencers.query.filter(and_(or_(Influencers.fname.like(f'%{search}%'), Influencers.lname.like(f'%{search}%'), Influencers.category.like(f'%{search}%'), Influencers.niche.like(f'%{search}%')), Influencers.flag == 0 )).all()
    return render_template("influencers_search.html", searches = influencers, u=uid)
  
@app.route("/search_campaign/<int:uid>",methods = ["GET","POST"])
def search_campaign(uid):
    search = request.form.get("search-campaign")
    campaigns = Campaigns.query.filter(and_(or_( Campaigns.name.like(f'%{search}%'), Campaigns.category.like(f'%{search}%')), Campaigns.visibility=="public", Campaigns.flag == 0 )).all()
    return render_template("campaigns_search.html", searches = campaigns, u=uid)

@app.route("/influencer_dashboard/<int:iid>",methods=["GET","POST"])
def influencer_dashboard(iid):
    influencer = Influencers.query.filter_by(id = iid).first()
    received_ad_requests = Ad_Request.query.join(Ad_Request.campaigns).filter( Ad_Request.influencer_id == iid, Ad_Request.status == "Pending", Campaigns.flag == 0).options(joinedload(Ad_Request.campaigns)).all()  
    accepted_ad_requests = Ad_Request.query.join(Ad_Request.campaigns).filter(Ad_Request.influencer_id == iid,Ad_Request.status == "Accepted",Campaigns.flag == 0).options(joinedload(Ad_Request.campaigns)).all()
    currentdate = datetime.now()
    accepted_dict ={}
    days_dict ={}
    imagepaths = []
    for ad in accepted_ad_requests:
        startdate = datetime.strptime(ad.campaigns.start_date, "%d/%m/%Y")
        enddate = datetime.strptime(ad.campaigns.end_date, "%d/%m/%Y")
        if(currentdate <= startdate):
            ad.campaigns.progress = 0.0
        elif(currentdate > startdate and currentdate < enddate):
            days = (enddate-startdate).days
            progress_percentage = 100/days
            if(((currentdate - startdate).days * progress_percentage) != ad.campaigns.progress):
                ad.campaigns.progress = math.trunc((currentdate - startdate).days * progress_percentage)
                
        elif(currentdate >= enddate):
            ad.campaigns.progress = 100.0 
            ad.influencer.earnings += (ad.payment)  
        accepted_dict[ad.campaigns.name] = ad.campaigns.progress
        days_dict[ad.campaigns.name] = (enddate-startdate).days
    
    figure, axes2 = plt.subplots()
    axes2.bar(days_dict.keys(), days_dict.values())
    imagename = f'influencer{iid}_campaigns_days.jpg'
    imagepath = os.path.join('static', 'images', imagename)
    plt.title(f'Campaigns - Duration')
    plt.xlabel("Campaigns")
    plt.ylabel("Duration (in days)")
    plt.savefig(imagepath)
    imagepaths.append(imagepath)

    figure, axes = plt.subplots()
    axes.set_ylim(0,100)
    axes.bar(accepted_dict.keys(), accepted_dict.values())
    imagename = f'influencer{iid}_campaigns.jpg'
    imagepath = os.path.join('static', 'images', imagename)
    plt.title(f'Campaigns - Progress')
    plt.xlabel("Campaigns")
    plt.ylabel("Progress (in %)")
    plt.savefig(imagepath)
    imagepaths.append(imagepath)
    db.session.commit()
    return render_template("influencer_dashboard.html",d=influencer,aad = accepted_ad_requests,status=imagepaths, ad = received_ad_requests)


@app.route("/sponsor_dashboard/<int:sid>",methods=["GET","POST"])
def sponsor_dashboard(sid):
    sponsor = Sponsors.query.filter_by(id = sid, flag = 0).first()
    campaigns = Campaigns.query.filter_by(sponsor_id = sid, flag =0).all()
    ad_requests = []
    received_ad_requests = []
    accepted_ad_requests = []
    for campaign in campaigns:
        for ad_request in campaign.ad_requests:
            if(ad_request.last_modified_by == sponsor.company) and ad_request.status =="Pending":
                ad_requests.append(ad_request)
            elif(ad_request.last_modified_by == ad_request.influencer.username) and ad_request.status =="Pending":
                received_ad_requests.append(ad_request)
            elif(ad_request.status =="Accepted"):
                accepted_ad_requests.append(ad_request)
    
    currentdate = datetime.now()
    days_dict = {}
    accepted_dict ={}
    imagepaths = []
    for ad in accepted_ad_requests:
        startdate = datetime.strptime(ad.campaigns.start_date, "%d/%m/%Y")
        enddate = datetime.strptime(ad.campaigns.end_date, "%d/%m/%Y")
        if(currentdate <= startdate):
            ad.campaigns.progress = 0.0
        elif(currentdate > startdate and currentdate < enddate):
            days = (enddate-startdate).days
            progress_percentage = 100/days
            if(((currentdate - startdate).days * progress_percentage) != ad.campaigns.progress):
                ad.campaigns.progress = math.trunc((currentdate - startdate).days * progress_percentage)
        elif(currentdate >= enddate):
            ad.campaigns.progress = 100.0
        days_dict[ad.campaigns.name] = (enddate-startdate).days
        accepted_dict[ad.campaigns.name] = ad.campaigns.progress

    for campaign in campaigns:
        if campaign.name not in days_dict.keys():
            startdate = datetime.strptime(campaign.start_date, "%d/%m/%Y")
            enddate = datetime.strptime(campaign.end_date, "%d/%m/%Y")
            days_dict[campaign.name] = (enddate-startdate).days

    figure, axes2 = plt.subplots()
    axes2.bar(days_dict.keys(), days_dict.values())
    imagename = f'sponsor{sid}_campaigns_days.jpg'
    imagepath = os.path.join('static', 'images', imagename)
    plt.title(f'Campaigns - Duration')
    plt.xlabel("Campaigns")
    plt.ylabel("Duration (in days)")
    plt.savefig(imagepath)
    imagepaths.append(imagepath)

    figure, axes = plt.subplots()
    axes.set_ylim(0,100)
    axes.bar(accepted_dict.keys(), accepted_dict.values())
    imagename = f'sponsor{sid}_campaigns.jpg'
    imagepath = os.path.join('static', 'images', imagename)
    plt.title(f'Campaigns - Progress')
    plt.xlabel("Campaigns")
    plt.ylabel("Progress (in %)")
    plt.savefig(imagepath)
    imagepaths.append(imagepath)

    db.session.commit()  
    return render_template("sponsor_dashboard.html",d=sponsor, c = campaigns, aad = accepted_ad_requests, status=imagepaths, rad = received_ad_requests, ad = ad_requests)
  

