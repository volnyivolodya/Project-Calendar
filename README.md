# запуск приложения

./venv/bin/flask --app ./acme-api/server.py run

## cURL тестирование

### добавление нового события
curl http://127.0.0.1:5000/api/v1/calendar/ -X POST -d "date|title|text"

### получение всего списка событий
curl http://127.0.0.1:5000/api/v1/calendar/

### получение события по идентификатору / ID == 1
curl http://127.0.0.1:5000/api/v1/calendar/1/

### обновление описания события по идентификатору / ID == 1 /  новый текст == "new text"
curl http://127.0.0.1:5000/api/v1/calendar/1/ -X PUT -d "date|title|new text"

## пример исполнения команд с выводом

## для календаря

$ curl http://127.0.0.1:5000/api/v1/calendar/ -X POST -d "2022-08-21|title|text"
new id: 1

$ curl http://127.0.0.1:5000/api/v1/calendar/
2022-08-21|title|text

$ curl http://127.0.0.1:5000/api/v1/calendar/1/
2022-08-21|title|text

$ curl http://127.0.0.1:5000/api/v1/calendar/1/ -X PUT -d "2023-08-21|new title|new text"
updated

$ curl http://127.0.0.1:5000/api/v1/calendar/1/
2023-08-21|new title|new text