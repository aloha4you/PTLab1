# -*- coding: utf-8 -*-
import pytest
from src.Types import DataType
from src.XmlDataReader import XmlDataReader


class TestXmlDataReader:

    @pytest.fixture()
    def file_and_data_content(self) -> tuple[str, DataType]:
        text = """
            <root>
                <student>
                    <name>Иванов Константин Дмитриевич</name>
                    <математика>91</математика>
                    <химия>100</химия>
                </student>
                <student>
                    <name>Петров Петр Семенович</name>>
                    <математика>78</математика>
                    <социология>78</социология>
                </student>
            </root>
        """

        data = {
            "Иванов Константин Дмитриевич": [
                ("математика", 91), ("химия", 100)
            ],
            "Петров Петр Семенович": [
                ("математика", 78), ("социология", 78)
            ]
        }
        return text, data

    @pytest.fixture()
    def filepath_and_data(self,
                          file_and_data_content: tuple[str, DataType],
                          tmpdir) -> tuple[str, DataType]:
        p = tmpdir.mkdir("datadir").join("my_data.xml")
        p.write_text(file_and_data_content[0], encoding='utf-8')
        return str(p), file_and_data_content[1]

    def test_read(self, filepath_and_data: tuple[str, DataType]) -> None:
        file_content = XmlDataReader().read(filepath_and_data[0])
        assert file_content == filepath_and_data[1]
