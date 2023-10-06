import requests
from metaphor_python import Metaphor
from flask import Flask, render_template


metaphor = Metaphor("c3c7a2d0-ca7e-454d-86f1-5dc3a88f9043")

response = metaphor.search(
"list of movies",
  num_results=10,
  use_autoprompt=True,
)

data = response

# print(data)
print(data["title"])

# for result in data:
#         title = result["title"]
#         url = result["url"]
#         published_date = result["publishedDate"]
#         author = result["author"]
#         id = result["id"]
#         score = result["score"]

#         print(f"Title: {title}")
#         print(f"URL: {url}")
#         print(f"Published Date: {published_date}")
#         print(f"Author: {author}")
#         print(f"ID: {id}")
#         print(f"Score: {score}")
#         print()


# print(response)

app = Flask(__name__, static_url_path='/static')

@app.route('/')
def index():
    return render_template('index.html', data=response)

if __name__ == '__main__':
    app.run(debug=True)
