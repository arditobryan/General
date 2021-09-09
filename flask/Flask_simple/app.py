from flask import Flask, render_template
import os

#sets the template folder from templates (default) to the root folder
app = Flask(__name__, template_folder="")
 
@app.route('/')
def index():
    return render_template('app1.html')

if __name__ == '__main__':
    app.run()