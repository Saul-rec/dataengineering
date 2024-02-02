from flask import Flask, request, jsonify
from requests import request as rq

app = Flask(__name__)

books = [
    {"id": 1, "author": "Javier Moro", "title": "El rey de Bengala"},
    {"id": 2, "author": "Jordi Sierra i Fabra", "title": "Las chicas de alambre"},
    {"id": 3, "author": "Reyes Monforte", "title": "Un burka por amor"},
    {"id": 4, "author": "Frank McCourt", "title": "Las cenizas de Ángela"},
    {"id": 5, "author": "Jon Krakauer", "title": "Hacia rutas salvajes"}
]
body = {}
@app.route('/saludo', methods=['GET'])
def hello_world():
    return "Hola a todos"
 
@app.route('/despedida', methods=['GET'])
def adios_world():
    return "Adios"
 
@app.route('/books', methods=['GET'])
def mostrar_books():
    sorted_books = sorted(books, key=lambda x: x['id'])
    body['books'] = sorted_books
    return jsonify(body)


@app.route('/books',methods=['POST'])
def post_books():
    jsonReq = request.get_json()
 
    new_book = {
        "id": len(books) + 1 ,
        "title" : jsonReq.get('title'),
        "author" : jsonReq.get('author')
    }
 
    books.append(new_book)
    # return jsonify({"Salida": "Creado correctamente"})
    return jsonify(new_book), 201
 
 
@app.route('/books/<int:book_id>',methods=['PUT'])
def update_books(book_id):
    specific_book = next(filter(lambda book: book['id'] == book_id, books), None)
    if specific_book is None:
        return jsonify({"Error": "Book no encontrado"}),404
    else:
        index = books.index(specific_book)
        books[index]['title'] = request.json['title']
        books[index]['author'] = request.json['author']
        return jsonify(books[index]), 202

if __name__ == '__main__':
    app.run(debug=True)
