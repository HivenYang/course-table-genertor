#!/usr/bin/env python
# encoding: utf-8

# ����ļ��������ſγ����п��ܳ��ֵĴ���

class Error(Exception):
    "��������"
    pass

# ��ȡ�����г��ֵĴ���
class TimeFormatError(Error):
    """ʱ���ʽ����

    Attributes:
        msg -- �����ʱ���ʽ
    """
    def __init__(self, msg):
        self.msg = msg
    def __str__(self):
        return self.msg

class MissingColumnError(Error):
    """CSV �ļ������еĴ���

    Attributes:
        line -- ���ִ������
    """
    def __init__(self, line)
        self.line = line
    def __str__(self):
        return self.line
