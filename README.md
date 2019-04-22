API Buku - Flask Restplus
======================================

Ini adalah api buku sederhana yang mana menggunakan JWT untuk autentikasi dalam mengonsumsi API.
Ada 4 api yang diberikan, yaitu :
1. API Internal, digunakan oleh client Internal untuk mengolah semua data buku(create, read, update, delete). Api ini hanya bisa dipakai dengan menggunakan token JWT dari client yang bertipe internal saja.
2. API Penerbit, digunakan oleh client penerbit untuk mengolah data buku(crud) sesuai dengan penerbit nya saja. Api ini hanya bisa dipakai dengan menggunakan token JWT dari client yang bertipe internal saja.
3. API Public, digunakan oleh client public tanpa menggunakan token JWT. Hanya bisa menampilkan daftar buku yang berstatus "show" saja. Juga bisa menampilkan item(satu) buku berdasarkan id.
4. API Token, digunakan untuk mengclaim/generate token.

Tutorial untuk mencoba di local
-------------------------------



Untuk dokumentasi (demo)-nya dapat dicoba di sini :
http://reinhard-rest-api.herokuapp.com/api/
