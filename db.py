from typing import List

import model
import storage
import datetime

class DBException(Exception):
    pass

class CalendarDB:
    def __init__(self):
        self._storage = storage.LocalStorage()

    def create(self, calendar: model.Calendar) -> datetime.date:
        try:
            return self._storage.create(calendar)
        except Exception as ex:
            raise DBException(f"failed CREATE operation with: {ex}")

    def list(self) -> List[model.Calendar]:
        try:
            return self._storage.list()
        except Exception as ex:
            raise DBException(f"failed LIST operation with: {ex}")

    def read(self, _date: datetime.date) -> model.Calendar:
        try:
            return self._storage.read(_date)
        except Exception as ex:
            raise DBException(f"failed READ operation with: {ex}")

    def update(self, _date: datetime.date, calendar: model.Calendar):
        try:
            return self._storage.update(_date, calendar)
        except Exception as ex:
            raise DBException(f"failed UPDATE operation with: {ex}")

    def delete(self, _date: datetime.date):
        try:
            return self._storage.delete(_date)
        except Exception as ex:
            raise DBException(f"failed DELETE operation with: {ex}")
