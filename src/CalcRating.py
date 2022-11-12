# -*- coding: utf-8 -*-
from Types import DataType

RatingType = dict[str, bool]

class CalcRating:

    def __init__(self, data: DataType) -> None:
        self.data: DataType = data
        self.tmp_rating: RatingType = {}
        self.res_names: list[str] = []

    # Возвращает список хорошистов и их количество
    def calc(self) -> (list[str], int):
        # Временный словарь, Имя студента -> Является ли хорошистом
        for key in self.data:
            self.tmp_rating[key] = True
            for (subject_name, subject_score) in self.data[key]:
                self.tmp_rating[key] = self.tmp_rating[key] and subject_score >= 76

        # Результирующий словарь, оставляющий только студентов хорошистов (я не умею в лямбды на питоне)
        for (key, value) in self.tmp_rating.items():
            if value:
                self.res_names.append(key)
        return self.res_names, len(self.res_names)
