from flask import Flask, request

app = Flask(__name__)

@app.route('/submit', methods=['POST'])
def submit():
    username = request.form['username']
    password = request.form['password']
    return f"Username: {username}, Password: {password}"

@app.route('/search')
def search():
    query = request.args.get('query')
    return f"Searching for: {query}"

@app.route('/json/data', methods=['POST'])
def get_data():
    data = request.get_json()
    return f"Received data: {data}"

@app.route('/upload', methods=['POST'])
def upload_file():
    file = request.files['file']
    file.save(f"/path/to/save/{file.filename}")
    return 'File uploaded successfully!'

if __name__ == "__main__":
    app.run(debug=True)