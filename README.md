
API Buku - Flask Restplus + JWT
====================

Ini adalah api buku sederhana yang mana menggunakan JWT untuk autentikasi dalam mengonsumsi API.
Ada 4 api yang diberikan, yaitu :
1. API Internal, digunakan oleh client Internal untuk mengolah semua data buku(create, read, update, delete). Api ini hanya bisa dipakai dengan menggunakan token JWT dari client yang bertipe internal saja.
2. API Penerbit, digunakan oleh client penerbit untuk mengolah data buku(crud) sesuai dengan penerbit nya saja. Api ini hanya bisa dipakai dengan menggunakan token JWT dari client yang bertipe internal saja.
3. API Public, digunakan oleh client public tanpa menggunakan token JWT. Hanya bisa menampilkan daftar buku yang berstatus "show" saja. Juga bisa menampilkan item(satu) buku berdasarkan id.
4. API Token, digunakan untuk mengclaim/generate token.


## Struktur Tabel
Database di sini menggunakan sqlite sqlalchemy, terletak di rest_api/db.sqlite.
 - **Client** : id, username(unique), password, type("penerbit" atau "internal")
 - **Buku** : id, isbn, title, penerbit, pengarang, status("show" atau "not show"), client, client_id

Pada file db.sqlite sudah ada row yang didefinisikan, yaitu :
Pada client ada 4 client, 2 client internal dan 2 client penerbit
Pada buku ada 6, yaitu 4 untuk status yang bernilai string, dan 2 yang bernilai show, sehingga client public hanya bisa melihat yang 2 buku show saja.

Untuk melihat data row client dan buku, bisa diakses melalui demo dokumentasi di http://reinhard-rest-api.herokuapp.com/api/, pada bagian :
- get : /internal/buku
- get : /internal/client

Untuk password client di sini masih belum dienkripsi

## Token
Token yang digenerate pada api ini menggunakan identitas objek dari client yang memiliki atribut id, username, password, dan type. Jadi dari token key bisa didapatkan informasi berupa atribut id, username, password, dan type. Untuk enkripsi dan dekripsi token key nya menggunakan secret key yang diberikan pada flask_app.config['JWT_SECRET_KEY'].

## Testing di local (ubuntu)
Untuk melakukan testing, silakan ikuti dan jalankan perintah-perintah di bawah secara berurutan. Saya menggunakan ubuntu dan virtualenv. Tanda (venv) berarti perintah tersebut dijalankan dalam virtual environment. **Jangan ikutsertakan tulisan (venv) di terminal, copas yang setelahnya ($)**

	$ git clone https://github.com/Reinhardjs/my_flask_api
	$ cd my_flask_api
	$ virtualenv -p python3 venv
	$ source venv/bin/activate
	(venv) $ pip install -r requirements.txt
	(venv) $ python setup.py develop

Untuk menjalankannya :

    $ (venv) python app.py

## Deployment ke heroku

    $ heroku login
    $ create heroku <nama-app>
    Creating app... done, ⬢ nama-app
    https://nama-app.herokuapp.com/ | https://git.heroku.com/nama-app.git
    $ git init
    $ git add .
    $ git commit -m "ready to deploy"
    $ git remote add myheroku https://git.heroku.com/nama-app.git
    $ git push myheroku master

Untuk dokumentasi (demo)-nya dapat dicoba di sini :
http://reinhard-rest-api.herokuapp.com/api/

Online Mark Editor :
https://stackedit.io
