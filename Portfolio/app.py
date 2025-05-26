from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/project')
def project():
    return render_template('project.html')

@app.route('/skills')
def skills():
    return render_template('skills.html')

@app.route('/certifications')
def certifications():
    return render_template('certifications.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

# Optional: Run only if this file is executed directly
if __name__ == '__main__':
    app.run(debug=True)
