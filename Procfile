release: sh -c 'python manage.py migrate && python manage.py loaddata */fixtures/*.json'
web: gunicorn pbp_e_03.wsgi --log-file -