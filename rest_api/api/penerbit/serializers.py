from flask_restplus import fields
from rest_api.api.restplus import api

book_expect = api.model('Book', {
    'isbn' : fields.String(description="Ini adalah isbn buku"),
    'pengarang' : fields.String(description="Ini adalah pengarang buku"),
    'penerbit' : fields.String(description="Ini adalah penerbit buku"),
    'harga' : fields.Integer(description="Ini adalah harga buku"),
    'status' : fields.String(description="Ini adalah status buku"),
    'title' : fields.String(description="Ini adalah judul buku")
})

book_response = api.inherit('Book response', book_expect, {
    'id' : fields.Integer(description="Ini adalah id buku"),
    'client' : fields.String(attribute='client.username'),
    'client_id' : fields.String(attribute='client.id')
})

pagination = api.model('A page of results', {
    'page': fields.Integer(description='Number of this page of results'),
    'pages': fields.Integer(description='Total number of pages of results'),
    'per_page': fields.Integer(description='Number of items per page of results'),
    'total': fields.Integer(description='Total number of results')
})

page_of_books = api.inherit('Page of Books', pagination, {
    'items' : fields.List(fields.Nested(book_response))
})

client_expect = api.model('User Expect', {
    'username' : fields.String(readOnly=True, description="Ini adalah username client"),
    'password' : fields.String(readOnly=True, description="Ini adalah password client"),
    'type' : fields.String(readOnly=True, description="Ini adalah tipe akun client"),
})

client_response = api.inherit('User Response', client_expect, {
    'id' : fields.Integer(readOnly=True, description="Ini adalah id client")
})

# client_with_books = api.inherit('Client with Books', client_response, {
#     'books' : fields.List(fields.Nested(book_response))
# })
