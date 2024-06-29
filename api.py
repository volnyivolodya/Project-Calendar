from flask import Flask
from flask import request
from datetime import datetime

app = Flask(__name__)


import model
import logic

_calendar_logic = logic.NoteLogic()


class ApiException(Exception):
    pass


def _from_raw(raw_calendar: datetime.date) -> model.Calendar:
    parts = raw_calendar.split('|')
    if len(parts) == 2:
        calendar = model.Calendar()
        calendar.date = None
        calendar.title = str(parts[0])
        calendar.text = str(parts[1])
        return calendar
    elif len(parts) == 3:
        calendar = model.Calendar()
        calendar.date = datetime.date(parts[0])
        calendar.title = str(parts[1])
        calendar.text = str(parts[2])
        return calendar
    else:
        raise ApiException(f"invalid RAW note data {raw_calendar}")


def _to_raw(calendar: model.Calendar) -> datetime.date:
    if calendar.date is None:
        return f"{calendar.date}|{calendar.title}|{calendar.text}"




API_ROOT = "/api/v1"
CALENDAR_API_ROOT = API_ROOT + "/calendar"


@app.route(CALENDAR_API_ROOT + "/", methods=["POST"])
def create():
    try:
        data = request.get_data().decode('utf-8')
        calendar = _from_raw(data)
        _date = _calendar_logic.create(calendar)
        return f"new date: {_date}", 201
    except Exception as ex:
        return f"failed to CREATE with: {ex}", 404


@app.route(CALENDAR_API_ROOT + "/", methods=["GET"])
def list():
    try:
        calendars = _calendar_logic.list()
        raw_calendars = ""
        for calendar in calendars:
            raw_calendars += _to_raw(calendar) + '\n'
        return raw_calendars, 200
    except Exception as ex:
        return f"failed to LIST with: {ex}", 404


@app.route(CALENDAR_API_ROOT + "/<_date>/", methods=["GET"])
def read(_date: datetime.date):
    try:
        calendar = _calendar_logic.read(_date)
        raw_calendar = _to_raw(calendar)
        return raw_calendar, 200
    except Exception as ex:
        return f"failed to READ with: {ex}", 404


@app.route(CALENDAR_API_ROOT + "/<_date>/", methods=["PUT"])
def update(_date: datetime.date):
    try:
        data = request.get_data().decode('utf-8')
        calendar = _from_raw(data)
        _calendar_logic.update(_date, calendar)
        return "updated", 200
    except Exception as ex:
        return f"failed to UPDATE with: {ex}", 404


@app.route(CALENDAR_API_ROOT + "/<_date>/", methods=["DELETE"])
def delete(_date: datetime.date):
    try:
        _calendar_logic.delete(_date)
        return "deleted", 200
    except Exception as ex:
        return f"failed to DELETE with: {ex}", 404
