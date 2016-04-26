from requests import get
from bs4 import BeautifulSoup
from IPython.core.display import display, HTML


def leet_puzzle(problem):
    response = get('https://leetcode.com/problems/' + problem)
    soup = BeautifulSoup(response.content)
    content = str(soup.select('.question-content')[0])
    html = '<a href="https://leetcode.com/problems/' + problem
    html += '">Source : https://leetcode.com/problems/' + problem + '</a>'
    html += content
    display(HTML(html))