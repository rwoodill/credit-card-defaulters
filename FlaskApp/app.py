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
@app.route('/jupyter_notebook_data_cleaning', methods=['GET'])
def get_data_cleaning_notebook():
    return render_template("Data_cleanning_app_data.html")

@app.route('/jupyter_notebook_ml_model', methods=['GET'])
def get_ml_notebook():
    return render_template("machine_learning.html")


if __name__ == "__main__":
    app.run(debug=False)