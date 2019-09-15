from flask import Flask, render_template, request
import requests
import json

app = Flask(__name__)


apikey = "XFF92IL8UZZG"
limit = 10

@app.route('/')
def index():
    """Return homepage."""
    # TODO: Extract the query term from url using request.args.get()
    search_term = request.args.get('user_input')
    # TODO: Make 'params' dictionary containing:
    # a) the query term, 'q'
    # b) your API key, 'key'
    # c) how many GIFs to return, 'limit'
    params = {
        'q': search_term,
        'key': apikey,
        'limit': limit
    }




    # TODO: Make an API call to Tenor using the 'requests' library. For 
    # reference on how to use Tenor, see: 
    # https://tenor.com/gifapi/documentation

    r = requests.args.get("https://api.tenor.com/v1/search?", params = params)
    gif_json = r.json()
   

    # TODO: Use the '.json()' function to get the JSON of the returned response
    # object
    gif_json = r.json()
    # TODO: Using dictionary notation, get the 'results' field of the JSON,
    # which contains the GIFs as a list
    gifs = gif_json['results']
    # TODO: Render the 'index.html' template, passing the list of gifs as a
    # named parameter called 'gifs'

    return render_template("index.html", gifs, search_term)

if __name__ == '__main__':
    app.run(debug=True)
