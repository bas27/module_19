перенос данны из sqlite в postgresql

```commandline
python -Xutf8 manage.py dumpdata -o data.json
или
python -Xutf8 ./manage.py dumpdata --exclude auth.permission --exclude contenttypes > data.json
```
далее комментируем настройку sqlite в settings
```
# DATABASES = {
#     "default": {
#         "ENGINE": "django.db.backends.sqlite3",
#         "NAME": BASE_DIR / 'db.sqlite3',
#     }
# }
```
и включаем настройку для БД postgresql.

Выполняем синхронизацию баз данных:
```commandline
python manage.py migrate --run-syncdb
```

Заливка данных выполняется коммандой:

```commandline
python manage.py loaddata data.json
```