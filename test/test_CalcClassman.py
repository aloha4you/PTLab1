# -*- coding: utf-8 -*-
from CalcClassman import CalcClassman
from src.Types import DataType
import pytest

ClassmanResType = (list[str], int)


class TestCalcClassman:

    @pytest.fixture()
    def input_data(self) -> tuple[DataType, ClassmanResType]:

        data: DataType = {
            "Абрамов Петр Сергеевич":
                [
                    ("математика", 80),
                    ("русский язык", 76),
                    ("программирование", 100)
                ],

            "Петров Игорь Владимирович":
                [
                    ("математика", 61),
                    ("русский язык", 80),
                    ("программирование", 78),
                    ("литература", 97)
                ]
        }

        # Без split мой список будет не из строк, а из символов...
        classman_output: ClassmanResType = (
            list("Абрамов Петр Сергеевич".split(sep="dummyseparator")), 1
        )

        return data, classman_output

    def test_init_calc_rating(self, input_data: tuple[DataType,
                                                      ClassmanResType]) -> None:

        calc_classman = CalcClassman(input_data[0])
        assert input_data[0] == calc_classman.data

    def test_calc(self, input_data: tuple[DataType, ClassmanResType]) -> None:

        classman = CalcClassman(input_data[0]).calc()
        assert pytest.approx(classman) == input_data[1]
