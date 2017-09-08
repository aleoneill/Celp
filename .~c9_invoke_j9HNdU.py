# main py file to run flask
from flask import *
from schoo_Stat import school_info
import os # library for system functions
from werkzeug.utils import secure_filename

app = Flask(__name__) # initializes app
UPLOAD_FOLDER = 'static/people'
ALLOWED_EXTENSIONS = set(['png', 'jpg'])
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
colleges = {
    "CSU Monterey Bay" : {'data' : {}, "comments" : {}, ' picture' : 'static/campus_pics/Monterey.png'},
    "San Jose State" : {'data' : {}, "comments" : {}, 'counter' : 0, 'picture' : 'static/campus_pics/CSUMontereyBay.png'},
    "San Diego State" : {'data' : {}, "comments" : {}, 'counter' : 0, 'picture' : 'static/campus_pics/CSUMontereyBay'},
    "UC Irvine" : {'data' : {}, "comments" : {}, 'counter' : 0, 'picture' : 'static/campus_pics/CSUMontereyBay'},
    "UC Berkeley" : {'data' : {}, "comments" : {}, 'counter' : 0, 'picture' : 'static/campus_pics/CSUMontereyBay'},
    "UC Davis" : {'data' : {}, "comments" : {}, 'counter' : 0, 'picture' : 'static/campus_pics/CSUMontereyBay'},
    "CSU Long Beach" : {'data' : {}, "comments" : {}, 'counter' : 0, 'picture' : 'static/campus_pics/CSUMontereyBay'}
}
class selected():
    selected_college = ""
    stats = school_info
x = selected()

#Homepage#######################################
@app.route('/') # homepage route
def home():
    print x.stats
    return render_template("home.html") # renders homepage

@app.route('/', methods=["POST"]) # homepage route
def choose_college():
    x.selected_college = request.form['college']
    print x.selected_college
    return redirect(url_for('college'))

@app.route("/college")
def college():
    params = {'college' : x.selected_college, 'image' : colleges[x.selected_college]['picture']}
    return render_template("college.html", params=params)

@app.route('/comment') # homepage route
def form():
    return render_template("comment.html") # renders homepage

@app.route('/comment', methods=["POST"])
def take_comment():
    name = request.form['name']
    email = request.form['email']
    comment = request.form['comment']
    file = request.files['image']
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    path = '/static/people/' + filename
    print path
    colleges[x.selected_college]['comments'][1] = {'name' : name, 'comment' : comment, 'email' : email, 'image' : path}
    params = colleges[x.selected_college]['comments'][1]
    params['college'] = x.selected_college
    return render_template("college_comments.html", params=params)
    

#Checking if run from user######################
if __name__ == '__main__':
    app.run(
        port=int(os.getenv('PORT', 8080)),
        host=os.getenv("IP", "0.0.0.0"),
        debug=True
        )        