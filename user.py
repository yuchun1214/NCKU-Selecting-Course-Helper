import json
import re
import csv
import sys
from requests_html import HTMLSession

__author__ = 'Yu Chun, Lin'

class user(object):
    def __init__(self):
        """
        open the courses daya
        """
        self.__course = list()
        with open('./myCourse.json','r') as f:
            data = json.load(f)
            self.__course = data
            # print(json.dumps(data,indent=4))

        self.__url = ''

    
    def setUrl(self, url):
        self.__url = url
    
    def getCourseWithOutClash(self):
        session = HTMLSession()
        response = session.get(self.__url)
        print(response)
        blocks = response.html.find('.course_y0')
        data = list()
        for i in blocks:
            sec = i.find('td')
            temp = {}
            temp['num'] = sec[2].text

            temp['name'] = sec[10].text
            temp['time'] = sec[16].text
            temp['discription'] = sec[19].text
            data.append(temp)
        data = self.__findCourseWithoutClashing(data)
        f = csv.writer(open('./course.csv','w'))
        keys = temp.keys()
        f.writerow(temp.keys())
        for i in data:
            f.writerow([i[x] for x in keys])
        # f.close()
        # with open('./course.json','w') as f:
        #     json.dump(data,f,indent=4,ensure_ascii=False)        
        
    def __findCourseWithoutClashing(self,data):
        withoutClash = []
        noneDecide = r'未定'
        noon = r'N'
        for i in data:
            if re.search(noneDecide,i['time']) == None:
                day = i['time'][1]
                if re.search(noon,i['time']) != None:
                    pass
                else:
                    time = []
                    try:

                        time.append(int(i['time'][3]))
                        time.append(int(i['time'][5]))
                        if self.__judgeClash(self.__course[day],time):
                            withoutClash.append(i)
                    except IndexError:
                        if not int(i['time'][3]) in self.__course[day]:
                            withoutClash.append(i)
            else:
                pass
                # withoutClash.append(i)
            pass
        return withoutClash
    
    def __judgeClash(self, data:list, target_course:list):
        for i in data:
            if i in range(target_course[0],target_course[1] + 1):
                return False
        return True

if __name__ == '__main__' : 
    url = 'http://course-query.acad.ncku.edu.tw/qry/qry001.php?dept_no=A9'
    if len(sys.argv) > 1:
        url = sys.argv[1]
    u = user()
    u.setUrl(url)
    u.getCourseWithOutClash()