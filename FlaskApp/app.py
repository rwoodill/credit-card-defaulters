from flask import Flask, jsonify, render_template, request

#################################################
# Flask Setup
#################################################
app = Flask(__name__)

#################################################
# Flask Routes
#################################################
@app.route("/")
def home_route():
    return render_template("index.html")

@app.route("/about")
def about_route():
    return render_template("about.html")

# ---------------------------------------------------------
# jupyter notebook
# ---------------------------------------------------------
@app.route('/jupyter_notebook_analysis', methods=['GET'])
def get_notebook():
    return render_template("data_analysis.html")




if __name__ == "__main__":
    app.run(debug=False)