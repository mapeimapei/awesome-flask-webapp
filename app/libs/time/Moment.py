import re
import calendar
import time as _time
import datetime as _datetime
# from dateutil import rrule,relativedelta

class Moment:

    def __init__(self):
        pass

    def timeStamp(self):
        '''
        获取时间戳
        :return: 时间戳（1629294055.8056374）
        '''
        return _time.time()

    def stamp_to_struct_time(self, now=None):
        '''
        时间戳转换为 struct_time
        :param now:
        :return:struct_time
        '''
        if not now:
            now = _time.time()

        return _time.localtime(float(now))

    def struct_time_to_stamp(self, struct_time=None):
        '''
        struct_time 转换为时间戳
        :param struct_time:
        :return:时间戳
        '''

        if not struct_time:
            struct_time = self.stamp_to_struct_time()
        return _time.mktime(struct_time)

    def struct_time_to_datetime(self, struct_time=None):
        '''
        struct_time 转换为标准时间datetime
        :param struct_time:
        :return:datetime
        '''

        if not struct_time:
            struct_time = self.stamp_to_struct_time()
        return _time.strftime("%Y-%m-%d %H:%M:%S", struct_time)

    def datetime_to_struct_time(self, datetime=None):
        '''
        标准格式的time转换为struct_time
        :param datetime:
        :return: struct_time
        '''
        if not datetime:
            datetime = self.struct_time_to_datetime()
        return _time.strptime(datetime, "%Y-%m-%d %H:%M:%S")

    def stamp_to_datetime(self, now=None):
        '''
        时间戳转换为年月日时分秒
        :param now: 时间戳
        :return: datetime
        '''
        return _time.strftime("%Y-%m-%d %H:%M:%S", self.stamp_to_struct_time(now))

    def datetime_to_stamp(self, datetime=None):
        '''
        标准时间转换为时间错
        :param datetime:
        :return: 时间错
        '''

        struct_time = self.datetime_to_struct_time(datetime)
        return self.struct_time_to_stamp(struct_time)
















