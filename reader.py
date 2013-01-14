#!/usr/bin/env python
# encoding: utf-8

from course import Course
import csv
import sys

class Reader:
    """��ȡ�γ���Ϣ����

    Attributes:
        file_name -- �γ���Ϣ���ļ���
        delimiter -- ÿһ�еķָ���
        comment   -- ע�ͷ��ţ�����ÿ�е���ǰ�棩
        courses   -- �γ̶�������
    """
    def __init__(self, file_name, delimiter=",", comment="#"):
        self.file_name = file_name
        self.delimiter = delimiter
        self.comment   = comment
        self.courses = []
        self._process_csv()

    def _is_comment_p(self, line):
        "(listof string) => boolean"
        empty_line = line == []
        if not empty_line:
            return line[0] == '' or line[0].startswith(self.comment)
        return True

    def _get_teachers(self, teachers):
        "��ʦ����ȫ����д���Էֺ�Ϊ�ָ����������"
        return map(str.upper, map(str.strip,
                                  teachers.strip().split(";")))
    def _process_csv(self):
        "���� csv �ķ���"
        with open(self.file_name, "rb") as csvfile:
            course_reader = csv.reader(csvfile)
            try:
                for course_info in course_reader:
                    print course_info
                    if self._is_comment_p(course_info):
                        continue
                    cid, name, credit, grade, teachers, week, time = course_info
                    teachers = self._get_teachers(teachers)
                    course = Course(cid, name, credit, grade,
                                    teachers, week, time)
                    self.courses.append(course)
            except Exception as e:
                # TODO: ��Ӹ��ִ���� Exception
                sys.exit('line %d: "%s"\nError: %s' %
                         (course_reader.line_num, ",".join(course_info), e))

if __name__=='__main__':
    reader = Reader("test.csv")
    for c in reader.courses:
        print c.cid, c.name, c.credit, c.grade_name, c.teachers, c.start_time
