import body as body
import requests
import send_email
api_key = "ef43dbe603f046899dd7ecf77756d658"
url = "https://newsapi.org/v2/everything?q=tesla&from=2023-06-19&sortBy=publishedAt&language=en\
&apiKey=ef43dbe603f046899dd7ecf77756d658"
req = requests.get(url)
content = req.json()
news_body=""
for article in content['articles'][:5]:


    if article["title"] is not None:

        news_body=news_body + article["title"]+"\n"+article["description"]+"\n"+article["url"]+"\n\n"

news_body_subject="Subject:News of tody\n"
news_body=news_body_subject+news_body
news_body=news_body.encode("utf8")

send_email.send_email(news_body)
print("email sent")




