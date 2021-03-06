#!/usr/bin/env python
# encoding: utf-8

# 这个文件用于记录课程要求的条件
# 这个文件可以开放给用户编辑，或者是使用代码生成

# 某门课想要在某段时间上
# ID -> 时间 id 列表（从 0 开始)
COURSE_PREFER_TIME = {
    'gjhwysybx' : [0,1,2,3,4],

                      }

# 某门课像要在某一天上
# id -> 日期 id 列表(从 0 开始）
COURSE_PREFER_DAY = {
    'gjhwysybx' : [0,1],
                     }

# 教师想要在某段时间上课的要求可以转化为课程
# 对时间的要求
TEACHER_PREFER_DAY = {
    'crh' : [0, 1],

}

TEACHER_PREFER_TIME = {
    'crh' : [0,1,2,3,4],
}
