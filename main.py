from requests_html import HTMLSession

__author__ = 'Yu Chun, Lin'

url = 'http://course-query.acad.ncku.edu.tw/qry/'

def get():
    session = HTMLSession()
    response = session.get(url)
    print(response)
    elements = response.html.find('body')


    


if __name__ == '__main__':
    get()