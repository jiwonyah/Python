"""
Request
리퀘스트를 하는 모듈을 인스톨 해보자.
--> import requests
--> 이는 standard library에 속하는 모듈이 아니므로 설치 없이 import가 불가능하다.
--> pypi에서 install 커맨드를 찾아 로컬 cmd에서 설치하자. (나는 replit에서 함)
"""

from requests import get    #request 모듈에서 get 메소드(함수)를 가져옴

websites = (
    "google.com",
    "facebook.com",
    "instagram.com"
)

def get_response(website, results) -> dict:
    response = get(website)
    status = response.status_code
    if 100 <= status < 200:
        results[website]="Informational"
    elif 200 <= status < 300:
        results[website]="Success"
    elif 300 <= status < 400:
        results[website]="Redirection"
    elif 400 <= status < 500:
        results[website]="Client Error"
    elif 500 <= status < 600:
        results[website]="Server Error"
    return results
        
results = {}
for website in websites:
    if not website.startswith("https://"):
        website = f"https://{website}"
        get_response(website, results)
    else:
        get_response(website, results)
        
print(results)