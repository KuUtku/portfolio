# Import
from flask import Flask, render_template,request, redirect



app = Flask(__name__)

# İçerik sayfasını çalıştırma
@app.route('/')
def index():
    return render_template('index.html')


# Dinamik beceriler
@app.route('/', methods=['POST'])
def process_form():
    # Redirect to the appropriate project page depending on which "SHOW PROJECT" button was pressed.
    # Replace the placeholder URLs below with your actual project links.
    if 'button_python' in request.form:
        return redirect('https://example.com/python-project')
    if 'button_discord' in request.form:
        return redirect('https://github.com/KuUtku/Discord_bot-new-')
    if 'button_html' in request.form:
        return redirect('https://example.com/html-project')
    if 'button_db' in request.form:
        return redirect('https://example.com/db-project')

    # Fallback: return to the homepage
    return redirect('/')


if __name__ == "__main__":
    app.run(debug=True)
