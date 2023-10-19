echo Run migrage
python3 manage.py migrate
echo Run application
python3 manage.py runserver 0.0.0.0:8080
