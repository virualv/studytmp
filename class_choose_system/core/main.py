# Author : virualv
# Time : 10/21/2018 10:48 PM
from conf import setting
from core import admin

class school:
    def __init__(self,schoolid):
        self.school_name = schoolid['name']
        self.address = schoolid['address']
        self.city = schoolid['city']

#schooldef = school(admin.schoolid)

class course:

    def __init__(self,courseid):
        self.name = courseid['name']
        self.outline = courseid['outline']
        self.price = courseid['price']

#classdef = course(admin.courseid)

class classes:

    def __init__(self,name,semester,course,starttime,teacher):
        self.name = name
        self.semester = semester
        self.course = course
        self.starttime = starttime
        self.teacher = teacher


