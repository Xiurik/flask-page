
# region 'Imports'
from flask import Flask, redirect, render_template, request

# endregion

# region 'Load'
app = Flask(__name__)
# endregion

# region 'Routing'
@app.route("/")
def home():
    return render_template('index.html')

@app.route("/work")
def work():
    return render_template('work.html')

@app.route("/works")
def works():
    return render_template('works.html')

@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/contact")
def contact():
    return render_template('contact.html')

@app.route("/components")
def components():
    return render_template('components.html')

@app.route("/thanks")
def thanks():
    return render_template('thanks.html')
# endregion

# region 'LogIn'
@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        data = request.form.to_dict()
        #? Now data is a dictionary like this:
        #? {'email': 'irwin.romero.rdz@gmail.com', 'subject': 'testing', 'message': 'testing mesage'}
        print(data)
        return redirect('thanks')
    else:
        return 'Something went wrong'
# endregion
