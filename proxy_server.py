from flask import Flask, Response, request
import requests

app = Flask(__name__)

@app.route('/proxy')

def proxy():
    target_url = "https://afr.score808.tv/football/2738334-club-brugge-vs-aston-villa.html"

    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(target_url, headers=headers, stream=True)

    return Response(response.iter_content(chunk_size=1024), content_type=response.headers["Content-Type"])

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
