1) Clone project on GitHub: https://github.com/FireSwami/Park
2) Install virtual environment: $ python -m venv venv (for windows) in your sources root directory
3) Activate virtual environment: $ .\venv\scripts\activate (for windows) in your sources root directory
4) Install libs: $ pip install -r requirements.txt (for windows) in your sources root directory
5) Create DB: $ python .\manage.py makemigrations
              $ python .\manage.py migrate
6) Load fixtures into DB: $ python .\manage.py loaddata db.json
   (if you need create dump: $python .\manage.py dumpdata cars.driver cars.vehicle --indent 2 > db.json)
7) Great superuser if you need: $ python .\manage.py createsuperuser
8) Start server: $ python .\manage.py runserver
9) Go to http://127.0.0.1:8000/swagger/ (for default) and get info