#!/usr/bin/env python3

import sys
from collections import Counter

class Person(object):
    """
    返回具有给定名称的 Person 对象
    """
    def __init__(self, grade):
        self.grade = grade

    def get_grade(self, grade):
        c = Counter(grade)
        return c


class Student(Person):
    """
    返回 Student 对象，采用 name, branch, year 3 个参数
    """
    def __init__(self, grade):
        self.grade = grade

    def get_grade(self,grade):
        c = Counter(grade)
        total_num = sum(c.values())
        fail_num = c['D']
        pass_num = total_num - fail_num
        print("Pass: {}, Fail: {}".format(pass_num, fail_num))


class Teacher(Person):
    """
    返回 Teacher 对象，采用字符串列表作为参数
    """
    def __init__(self, grade):
        self.grade = grade

    def get_grade(self, grade):
        s = Counter(grade).most_common()
        for k, v in s:
            print("{}: {},".format(k, v),end =' ')
      

student1 = Student('Amy')
teacher1 = Teacher('John')


if __name__ == '__main__':
    if sys.argv[1] == "teacher":
        teacher1.get_grade(sys.argv[2])
    elif sys.argv[1] == "student":
        student1.get_grade(sys.argv[2])
