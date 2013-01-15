#!/usr/bin/env python
# encoding: utf-8

import utils

class Course:
    def __init__(self, cid, name, credit, grade, teachers, week, time):
        """�γ�

        Attributes:
                cid -- ÿ���γ���Ψһ��һ�� id
               name -- �γ�����
             credit -- ѧ��
              grade -- �꼶����
           teachers -- ���ſε���ʦ�����ܶ��
         start_time -- ���ſε��Ͽ�ʱ�䡣
                       ���û��Ԥ���ϿΣ������� None
                       ���Ԥ���Ͽ�ʱ�䣬��(ʱ�䣬����)�� tuple
        """
        self.cid = cid
        self.name = name
        self.credit = int(credit)
        self.grade = grade
        self.teachers = teachers
        #�� week, time ת��Ϊ��ά���������[time, week]
        self.start_time = utils.to_pos(week, time)

    def __str__(self):
        return self.name

    def need_allocate_p(self):
        return self.start_time == None
