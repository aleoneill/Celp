# main py file to run flask
from flask import *
from schoo_Stat import *
import os # library for system functions
from werkzeug.utils import secure_filename
from samples import *

app = Flask(__name__) # initializes app
UPLOAD_FOLDER = 'static/people'
ALLOWED_EXTENSIONS = set(['png', 'jpg'])
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
colleges = {
    "CSU Monterey Bay" : {'data' : {}, "comments" : {}, 'counter' : 0, 'picture' : 'static/campus_pics/csumb.jpg', 'back_stats' : 'static/campus_pics/Otter.png'},
    "San Jose State" : {'data' : {}, "comments" : {}, 'counter' : 0, 'picture' : 'static/campus_pics/SJSU.jpg.jpg', 'back_stats' : 'static/campus_pics/Spartan.png'},
    "San Diego State" : {'data' : {}, "comments" : {}, 'counter' : 0, 'picture' : 'static/campus_pics/SDSU.jpg', 'back_stats' : 'static/campus_pics/Aztec.png'},
    "UC Berkeley" : {'data' : {}, "comments" : {}, 'counter' : 0, 'picture' : 'static/campus_pics/UCB.jpg', 'back_stats' : 'static/campus_pics/Bear.png'},
    "UC Davis" : {'data' : {}, "comments" : {}, 'counter' : 0, 'picture' : 'static/campus_pics/UCD.jpg', 'back_stats' : 'static/campus_pics/Aggies.png'},
    "UC Irvine" : {'data' : {}, "comments" : {}, 'counter' : 0, 'picture' : 'static/campus_pics/UCI.jpg', 'back_stats' : 'static/campus_pics/Anteater.png'}
}

colleges = call_samples(colleges)
colleges = statistics(colleges)

class selected():
    selected_college = ""
x = selected()

#Homepage#######################################
@app.route('/') # homepage route
def home():
    return render_template("home.html") # renders homepage

@app.route('/', methods=["POST"]) # homepage route
def choose_college():
    x.selected_college = request.form['college']
    print x.selected_college
    return redirect(url_for('college'))

@app.route("/college")
def college():
    #params = {'college' : x.selected_college, 'image' : colleges[x.selected_college]['picture']}
    params = {}
    for i in range(1,4):
        params[i] = colleges[x.selected_college]['comments'][i]
    print params
    params['college'] = x.selected_college
    params['school_pic'] = colleges[x.selected_college]['picture']
    params['back_stats'] = colleges[x.selected_college]['back_stats']
    params['stats'] = colleges[x.selected_college]['data']
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
    return redirect(url_for('college'))
    # parameters = {}
    # for i in range(1,4):
    #     parameters[i] = colleges[x.selected_college]['comments'][i]
    # print parameters
    # parameters['college'] = x.selected_college
    # return render_template("college_comments.html", parameters=parameters)

#Checking if run from user######################
if __name__ == '__main__':
    app.run(
        port=int(os.getenv('PORT', 8080)),
        host=os.getenv("IP", "0.0.0.0"),
        debug=True
        )

# fix image link in comments
# attach stories to college.html
# make campuses
# create logo key in college dictionary