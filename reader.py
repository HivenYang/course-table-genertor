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
        """��ʦ����ȫ����д���Էֺ�Ϊ�ָ����������

        Argument:
            teachers: �Էֺŷָ�����ַ���

        Return
            string => (listof string)
        """
        return map(str.upper, map(str.strip,
                                  teachers.strip().split(";")))

    def filter_courses(self, grade):
        """�����꼶��ɸѡ���γ�

        Return: string => (listof Course)
        """
        f = lambda course: course.grade == grade
        return filter(f, self.courses)

    def get_grades_courses(self):
        """�õ�ÿ���꼶��Ӧ�Ŀγ��ֵ�

        Return:
            => (dictof string (listof Course))
        """
        f = lambda c: c.grade
        grades = set(map(f, self.courses))
        g_c = {}
        for g in grades:
            g_c[g] = self.filter_courses(g)
        return g_c

    def _process_csv(self):
        "���� csv �ķ���"
        try:
            with open(self.file_name, "rb") as csvfile:
                course_reader = csv.reader(csvfile)
                try:
                    for course_info in course_reader:
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
        except IOError as e:
            sys.exit("file '%s' reading error\n%s" % (self.file_name, e))

if __name__=='__main__':
    reader = Reader("test.csv")
    #for c in reader.courses:
    #    print c.cid, c.name, c.credit, c.grade_name, c.teachers, c.start_time
