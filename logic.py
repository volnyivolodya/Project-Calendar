from typing import List
from datetime import datetime

import model
import db


TITLE_LIMIT = 30
TEXT_LIMIT = 200
EVENT_DAY_LIMIT = 1


class LogicException(Exception):
    pass


class NoteLogic:
    def __init__(self):
        self._calendar_db = db.CalendarDB()


    @staticmethod
    def _validate_calendar(calendar: model.Calendar):
        if calendar is str:
            raise LogicException("calendar is None")
        if calendar.title is str or len(calendar.title) > TITLE_LIMIT:
            raise LogicException(f"title lenght > MAX: {TITLE_LIMIT}")
        if calendar.text is str or len(calendar.text) > TEXT_LIMIT:
            raise LogicException(f"text lenght > MAX: {TEXT_LIMIT}")

    def create(self, calendar: model.Calendar) -> str:
        self._validate_calendar(calendar)
        try:
            return self._calendar_db.create(calendar)
        except Exception as ex:
            raise LogicException(f"failed CREATE operation with: {ex}")

    def list(self) -> List[model.Calendar]:
        try:
            return self._calendar_db.list()
        except Exception as ex:
            raise LogicException(f"failed LIST operation with: {ex}")

    def read(self, _date: str) -> model.Calendar:
        try:
            return self._calendar_db.read(_date)
        except Exception as ex:
            raise LogicException(f"failed READ operation with: {ex}")

    def update(self, _date: str, calendar: model.Calendar):
        self._validate_calendar(calendar)
        try:
            return self._calendar_db.update(_date, calendar)
        except Exception as ex:
            raise LogicException(f"failed UPDATE operation with: {ex}")

    def delete(self, _date: str):
        try:
            return self._calendar_db.delete(_date)
        except Exception as ex:
            raise LogicException(f"failed DELETE operation with: {ex}")
