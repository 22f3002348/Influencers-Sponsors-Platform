from .database import db

class Campaigns(db.Model):
    __tablename__= 'campaigns'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable = False, unique = True)
    name = db.Column(db.String, nullable = False)
    description = db.Column(db.String, nullable = False)
    start_date = db.Column(db.String, nullable = False)
    end_date  = db.Column(db.String, nullable = False)
    budget = db.Column(db.Float, nullable = False)
    visibility = db.Column(db.String, nullable = False)
    goals = db.Column(db.String, nullable = False)
    sponsor_id = db.Column(db.String, nullable = False)

class Influencers(db.Model):
    __tablename__= 'influencer'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable = False, unique = True)
    fname = db.Column(db.String, nullable = False)
    lname = db.Column(db.String, nullable = False)
    city = db.Column(db.String, nullable = False)
    username = db.Column(db.String, nullable = False, unique = True)
    category  = db.Column(db.String, nullable = False)
    niche  = db.Column(db.String, nullable = False)
    email = db.Column(db.Integer, nullable = False)
    password = db.Column(db.String, nullable = False)
    
class Sponsors(db.Model):
    __tablename__= 'sponsor'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable = False, unique = True)
    company = db.Column(db.String, nullable = False)
    city = db.Column(db.String, nullable = False)
    industry = db.Column(db.String, nullable = False)
    budget  = db.Column(db.Float, nullable = False)
    username = db.Column(db.String, nullable = False, unique = True)
    email = db.Column(db.String, nullable = False)
    password = db.Column(db.String, nullable = False)
    
class Admin(db.Model):
    __tablename__ = 'admin'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable = False, unique = True)
    username = db.Column(db.String, nullable = False, unique = True)
    password = db.Column(db.String, nullable = False)

class Ad_Request(db.Model):
    __tablename__ = 'ad_request'
    campaign_id = db.Column(db.Integer, db.ForeignKey("campaigns.campaign_id") ,primary_key=True, nullable = False)
    influencer_id = db.Column(db.Integer,db.ForeignKey("influencer.influencer_id"), primary_key=True, nullable = False)
    messages = db.Column(db.String, nullable = False)
    requirements = db.Column(db.String, nullable = False)
    payment = db.Column(db.Integer, nullable = False)
    status = db.Column(db.String, nullable = False)

