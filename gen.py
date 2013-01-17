#!/usr/bin/env python
# encoding: utf-8

import configure as cfg
import debug
import sys

d = debug.Debug('generator')

class Generator:
    """�ſγ̵���

    Attributes:
    """
    def __init__(self, course_pool):
        self.course_pool = course_pool
        self.sorted_course = course_pool.sort_course()
        self.tables = tables

    def set_course(self, courseid):
        "����Ӧ�Ŀα��������λ�ðڷ�"
        # 1. �õ���֮��ص����пα�
        tables = self.course_to_table(courseid)
        # 2. ����صļ����α��ϣ��ҵ�һ�� *�����ŵ�* *���* λ��
        # 2.1 ���ȼ����α��е������еĿա��ȴ����Ŀ�ʼ��λ�ã�����Ƚ�
        #     ���Ŀα��Ҳ���λ�ã��Ϳ϶��Ҳ���λ����
        max_table = self.find_max_course_num(tables)
        # 2.2 �ҵ��������ĿΣ���ʼ��һ�����λ��

        # 3. �ŵ����λ����

    #-----------��������------------

    #-----------�� course_pool ���а�װ -----------------
    def course_to_table(self, courseid):
        return self.course_pool.course_to_table(courseid)
    def find_max_course_num(self, tables):
        return self.course_pool.find_max_course_num(tables)
    ## ��Ҫ���� ##
    def gen(self):
        for course in self.sorted_course:
            self.set_course(course.cid)

if __name__=='__main__':
    from reader import Reader
    from course_table import CourseTable
    from course_pool import CoursePool

    reader = Reader('test.csv')
    course_pool = CoursePool(reader.courses)

    generator = Generator(course_pool)

    new_tables = generator.gen()

    print new_tables[0].pretty_str()
