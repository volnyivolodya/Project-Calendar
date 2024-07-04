from typing import List
from datetime import datetime

import model


class StorageException(Exception):
    pass

class LocalStorage:
    def __init__(self):
        self._date_counter = 0
        self._storage = {}

    def create(self, calendar: model.Calendar) -> str:
        self._date_counter += 1
        calendar.date = str(self._date_counter)
        self._storage[calendar.date] = calendar
        return calendar.date

    def list(self) -> List[model.Calendar]:
        return list(self._storage.values())

    def read(self, _date: str) -> model.Calendar:
        if _date not in self._storage:
            raise StorageException(f"{_date} not found in storage")
        return self._storage[_date]

    def update(self, _date: str, calendar: model.Calendar):
        if _date not in self._storage:
            raise StorageException(f"{_date} not found in storage")
        calendar.date = _date
        self._storage[calendar.date] = calendar

    def delete(self, _date: str):
        if _date not in self._storage:
            raise StorageException(f"{_date} not found in storage")
        del self._storage[_date]
