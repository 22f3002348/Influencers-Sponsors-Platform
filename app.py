from flask import Flask, render_template, request

app = Flask(__name__)

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


if __name__ == "__main__":
    app.debug = True
    app.run()