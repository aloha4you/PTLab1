from lxml import etree

from Types import DataType
from DataReader import DataReader


class XmlDataReader(DataReader):

    def __init__(self) -> None:
        self.key: str = ""
        self.students: DataType = {}

    def read(self, path: str) -> DataType:
        with open(path, encoding="utf-8") as fobj:
            xml = bytes(bytearray(fobj.read(), encoding='utf-8'))
            root = etree.fromstring(xml)
            for student in root.getchildren():
                for elem in student.getchildren():
                    if elem.tag == "name":
                        name = elem.text
                        self.students[name] = []
                    else:
                        self.students[name].append((elem.tag, int(elem.text)))

        return self.students
