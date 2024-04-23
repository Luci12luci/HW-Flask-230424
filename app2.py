from flask import Flask, jsonify, request

books = [
    {'id': 1, 'title': 'The Great Gatsby', 'author': 'F. Scott Fitzgerald'},
    {'id': 2, 'title': 'To Kill a Mockingbird', 'author': 'Harper Lee'}
]

app = Flask(__name__)

@app.route('/')
def home():
    return 'Nasa kniznica'

@app.route('/knihy/', methods=['GET'])
def get_books():
    return jsonify({'books': books})

@app.route('/knihy/', methods=['POST'])
def add_book():
    print(request)
    new_book = {
        'id': books[-1]['id'] + 1,
        'title': request.json['title'],
        'author': request.json['author']
    }
    books.append(new_book)
    return jsonify(new_book), 201

if __name__ == "__main__":
    app.run()

@app.route('/books/<int:id>', methods=['GET'])
def get_book(id):
        for book in books:
         if book["id"] == id:
            return jsonify(book)

        return jsonify({"error": f"Book with ID {id} not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)

def update_book(id, title, author):
    if id in books:
        books[id]["title"] = title
        books[id]["author"] = author
        return books[id]
    else:
        return None

@app.route('/books/<int:id>', methods=['PUT'])
def update_book(id):
    data = request.get_json()
    title = data.get("title")
    author = data.get("author")

    updated_book = update_book(id, title, author)
    if updated_book:
        return jsonify(updated_book), 200
    else:
        return jsonify({"error": "Kniha nebola nájdená"}), 404

if __name__ == '__main__':
    app.run(debug=True)

@app.route('/books/<int:id>', methods=['DELETE'])
def delete_book(id):
    if id in books:
        del books[id]
        return jsonify({"message": f"Book with ID {id} has been deleted."}), 200
    else:
        return jsonify({"error": f"Book with ID {id} not found."}), 404

if __name__ == '__main__':
    app.run(debug=True)
