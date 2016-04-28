from requests import get
from bs4 import BeautifulSoup
from IPython.core.display import display, HTML


def leet_puzzle(problem):
    
    html = '<a href="https://leetcode.com/problems/' + problem
    html += '">Source : https://leetcode.com/problems/' + problem + '</a>'
    
    response = get('https://leetcode.com/problems/' + problem)
    soup = BeautifulSoup(response.content)
    content = soup.select('.question-content')[0]
    
    for a in content.select('a'):
        if a['href'] == '/subscribe/':
            a.nextSibling.extract()
            a.extract()
        else:
            a['href'] = 'https://leetcode.com' + a['href']

    for tags in content.select('#tags'):
        tags.extract()
        
    for similar in content.select('#similar'):
        similar.extract()
        
    html += str(content)
    
    display(HTML(html))