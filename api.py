from flask import Flask
from flask import request

app = Flask(__name__)


import model
import logic

_calendar_logic = logic.CalendarLogic()

class ApiException(Exception):
    pass


def _from_raw_c(raw_calendar: str) -> model.Calendar:
    parts = raw_calendar.split('|')
    if len(parts) == 3:
        calendar = model.Calendar()
        calendar.id = None
        calendar.date = parts[0]
        calendar.title = parts[1]
        calendar.text = parts[2]
        return calendar
    elif len(parts) == 4:
        calendar = model.Calendar()
        calendar.id = parts[0]
        calendar.date = parts[1]
        calendar.title = parts[2]
        calendar.text = parts[3]
        return calendar
    else:
        raise ApiException(f"invalid RAW note data {raw_calendar}")


def _to_raw_c(calendar: model.Calendar) -> str:
    if calendar.id is None:
        return f"{calendar.date}|{calendar.title}|{calendar.text}"
    else:
        return f"{calendar.id}|{calendar.date}|{calendar.title}|{calendar.text}"


API_ROOT = "/api/v1"
CALENDAR_API_ROOT = API_ROOT + "/calendar"


@app.route(CALENDAR_API_ROOT + "/", methods=["POST"])
def create_calendar():
    try:
        data = request.get_data().decode('utf-8')
        calendar = _from_raw_c(data)
        _id = _calendar_logic.create(calendar)
        return f"new id: {_id}", 201
    except Exception as ex:
        return f"failed to CREATE with: {ex}", 404


@app.route(CALENDAR_API_ROOT + "/", methods=["GET"])
def list_calendar():
    try:
        calendars = _calendar_logic.list()
        raw_calendars = ""
        for calendar in calendars:
            raw_calendars += _to_raw_c(calendar) + '\n'
        return raw_calendars, 200
    except Exception as ex:
        return f"failed to LIST with: {ex}", 404


@app.route(CALENDAR_API_ROOT + "/<_id>/", methods=["GET"])
def read_calendar(_id: str):
    try:
        calendar = _calendar_logic.read(_id)
        raw_calendar = _to_raw_c(calendar)
        return raw_calendar, 200
    except Exception as ex:
        return f"failed to READ with: {ex}", 404


@app.route(CALENDAR_API_ROOT + "/<_id>/", methods=["PUT"])
def update_calendar(_id: str):
    try:
        data = request.get_data().decode('utf-8')
        calendar = _from_raw_c(data)
        _calendar_logic.update(_id, calendar)
        return "updated", 200
    except Exception as ex:
        return f"failed to UPDATE with: {ex}", 404


@app.route(CALENDAR_API_ROOT + "/<_id>/", methods=["DELETE"])
def delete_calendar(_id: str):
    try:
        _calendar_logic.delete(_id)
        return "deleted", 200
    except Exception as ex:
        return f"failed to DELETE with: {ex}", 404