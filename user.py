import json

__author__ = 'Yu Chun, Lin'

class user(object):
    def __init__(self,parmeter:list):
        self.__url = 'http://course-query.acad.ncku.edu.tw/qry/qry001.php?dept_no={}'
        self.__courseTime = {}
        self.__urlList = []
        self.__getUserCourseInfo()
        if(type(parmeter) != list):
            raise TypeError('user object needs a list type object parameter')
        
        self.__uWant = parmeter
        self.__composeUrl()

    def __composeUrl(self):
        
        for i in self.__uWant:
            self.__urlList.append(self.__url.format(i))
        
    
    def __getUserCourseInfo(self):
        with open('myCourse.json','r') as f:
            data = json.load(f)
            days = data.keys()
            for i in days:
                timeStr = data[i].keys()
                self.__courseTime[i] = []
                # print(timeStr)
                for j in timeStr:
                    self.__courseTime[i] .append(j.split('-'))
            # print(json.dumps(data,indent=4,ensure_ascii=False))

    def UserCourse(self):
        return self.__courseTime

    def UserInput(self):
        return self.__uWant

    def UserWantURL(self):
        return self.__urlList

if __name__ == '__main__' : 
    u = user(['A9','A0'])
    data = u.UserWantURL()
    for i in data:
        print(i)