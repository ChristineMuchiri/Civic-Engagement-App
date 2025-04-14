from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html", title="Home")

@app.route('/report', methods=['GET', 'POST'])
def report():
    if request.method == "POST":
        corruption_type = request.form.get('type')
        location = request.form.get('location')
        description = request.form.get('message')
        files = request.files.getlist('evidence')
        
        flash('Thank you! Your report has been submitted.')
        return redirect(url_for('home'))
    return render_template('index.html', title='Report')
if __name__ == '__main__':
    app.run(debug=True)