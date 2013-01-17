#!/usr/bin/env python
# encoding: utf-8

# �γ̳أ����ڴ�������йؿγ̵Ĳ���

import configure as cfg
from course_table import CourseTable
import debug

d = debug.Debug('course_pool')

class CoursePool:
    def __init__(self, all_courses):
        # ���еĿγ�
        self._all_courses = all_courses
        # ÿ��courseid��Ӧ�Ŀγ�
        self._courseid_course_dict = self._get_courseid_course_dict()
        # ����group�Ŀγ̱�
        self._tables = self._get_all_tables()
        # group ��Ӧ�Ŀγ̱�
        self._group_table_dict = self._get_group_table_dict()
        # ÿ���γ̶�Ӧ�Ŀγ̱�
        self._courseid_table_dict = self._get_courseid_table_dict()

        self._sorted_course = self._sort_course()

    def _sort_course(self):
        "�����еĿγ̽�������"

        return self._all_courses

    def _get_courseid_course_dict(self):
        ccd = {}
        for c in self._all_courses:
            ccd[c.cid] = c
        return ccd

    def _get_group_table_dict(self):
        "ÿ�� group ��Ӧһ�� table"
        gtd = {}
        for table in self._tables:
            gtd[table.title] = table
        return gtd

    def _get_all_groups(self):
        "�õ����е�group����"
        groups = []
        for c in self._all_courses:
            groups.extend(c.groups)
        return set(groups)

    def _get_courseid_table_dict(self):
        """���ؿγ���γ̶�Ӧ��group��table"""
        ctd = {}
        for c in self._all_courses:
            for g in c.groups:
                try:
                    # ȥ�أ���Ϊ�� _all_courses ������ܻ��������
                    # һ���Ŀγ̣�e.g.һ������������2��2ѧ�ֵ�X�Σ�
                    if self._group_table_dict[g] not in ctd[c.cid]:
                        ctd[c.cid].append(self._group_table_dict[g])
                except KeyError:
                    ctd[c.cid] = [self._group_table_dict[g]]
        return ctd

    def _get_all_tables(self):
        #�õ��꼶����Ӧ�γ̵�ӳ��
        groups = self._get_all_groups()

        # ��ʼ���γ̱�
        tables = []
        for k in groups:
            tables.append(CourseTable(k))
        return tables

    #------ ����ӿ� ------
    def id_to_course(self, courseid):
        return self._courseid_course_dict[courseid]
    def course_to_table(self, courseid):
        return self._courseid_table_dict[courseid]
    def find_max_course_num(self, tables):
        return max(tables, key=lambda x: x.course_num)

    
if __name__ == '__main__':
    import reader
    r = reader.Reader('test.csv')
    cp = CoursePool(r.courses)
    # ��ӡ���еĿγ�
    for c in cp._all_courses:
        print c.cid, c.name, c.credit, c.groups, c.teachers

    print 'ALL GROUPS: %s' % cp._get_all_groups()

    print '============='
    for i in cp._tables:
        print i
    print '-------------'
    for i in cp._group_table_dict:
        print 'GROUP: %s' % i
        print cp._group_table_dict[i]
    print 'ÿ���γ̶�Ӧ�Ŀγ̱�'
    for i in cp._courseid_table_dict:
        c = cp.id_to_course(i)
        print 'COURSE: %s %s %s' % (c.name, c.groups, c.teachers)
        for k in cp._courseid_table_dict[i]:
            print k
