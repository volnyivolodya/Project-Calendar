from typing import List
import re
import model
import db


TITLE_LIMIT = 30
TEXT_LIMIT = 200


class LogicException(Exception):
    pass


class NoteLogic:
    def __init__(self):
        self._note_db = db.NoteDB()


    @staticmethod
    def _validate_note(note: model.Note):
        if note is None:
            raise LogicException("note is None")
        if note.title is None or len(note.title) > TITLE_LIMIT:
            raise LogicException(f"title lenght > MAX: {TITLE_LIMIT}")
        if note.text is None or len(note.text) > TEXT_LIMIT:
            raise LogicException(f"text lenght > MAX: {TEXT_LIMIT}")

    def create(self, note: model.Note) -> str:
        self._validate_note(note)
        try:
            return self._note_db.create(note)
        except Exception as ex:
            raise LogicException(f"failed CREATE operation with: {ex}")

    def list(self) -> List[model.Note]:
        try:
            return self._note_db.list()
        except Exception as ex:
            raise LogicException(f"failed LIST operation with: {ex}")

    def read(self, _id: str) -> model.Note:
        try:
            return self._note_db.read(_id)
        except Exception as ex:
            raise LogicException(f"failed READ operation with: {ex}")

    def update(self, _id: str, note: model.Note):
        self._validate_note(note)
        try:
            return self._note_db.update(_id, note)
        except Exception as ex:
            raise LogicException(f"failed UPDATE operation with: {ex}")

    def delete(self, _id: str):
        try:
            return self._note_db.delete(_id)
        except Exception as ex:
            raise LogicException(f"failed DELETE operation with: {ex}")


class CalendarLogic:
    def __init__(self):
        self._calendar_db = db.CalendarDB()


    @staticmethod
    def _validate_calendar(calendar: model.Calendar):
        if calendar is None:
            raise LogicException("note is None")
        if calendar.date is None or re.fullmatch(r'\d\d\d\d-\d\d-\d\d', calendar.date) is None:
            raise LogicException(f"date is None")
        if calendar.title is None or len(calendar.title) > TITLE_LIMIT:
            raise LogicException(f"title lenght > MAX: {TITLE_LIMIT}")
        if calendar.text is None or len(calendar.text) > TEXT_LIMIT:
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

    def read(self, _id: str) -> model.Calendar:
        try:
            return self._calendar_db.read(_id)
        except Exception as ex:
            raise LogicException(f"failed READ operation with: {ex}")

    def update(self, _id: str, calendar: model.Calendar):
        self._validate_calendar(calendar)
        try:
            return self._calendar_db.update(_id, calendar)
        except Exception as ex:
            raise LogicException(f"failed UPDATE operation with: {ex}")

    def delete(self, _id: str):
        try:
            return self._calendar_db.delete(_id)
        except Exception as ex:
            raise LogicException(f"failed DELETE operation with: {ex}")