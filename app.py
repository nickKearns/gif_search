from flask import Flask, render_template, request
import requests
import json

app = Flask(__name__, static_url_path='/static')


apikey = "XFF92IL8UZZG"
limit = 10


@app.route('/')
def index():
    """Return homepage."""
    # TODO: Extract the query term from url using request.args.get()
    # GET THE SEARCH TERM FROM THE SEARCH BOX IN THE HOME PAGE
    search_term = request.args.get('user_input')
    #print('search_term=', search_term)
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



    show_trending = request.args.get('show_trending')

    if show_trending:
        r = requests.get("https://api.tenor.com/v1/trending?key=XFF92IL8UZZG")

        json_gifs = json.loads(r.content)
        gifs = json_gifs['results']
        return render_template(
            'index.html',
            gifs = gifs
        )





    # get the data from the api using the apikey, the limit and the search term that the user has supplied
    elif search_term:

        r = requests.get("https://api.tenor.com/v1/search?", params=params)


        if r.status_code == 200:
            # TODO: Use the '.json()' function to get the JSON of the returned response
            # object
            json_gifs = json.loads(r.content)

            # TODO: Using dictionary notation, get the 'results' field of the JSON,
            # which contains the GIFs as a list
            gifs = json_gifs['results']

            print(gifs)

            # TODO: Render the 'index.html' template, passing the list of gifs as a
            # named parameter called 'gifs'

            return render_template(
                'index.html',
                gifs=gifs,
                search_term = search_term
            )
    else:
        r = requests.get("https://api.tenor.com/v1/search?", params=params)
        json_gifs = json.loads(r.content)
        gifs = json_gifs['results']
        return render_template(
            'index.html',
            gifs=gifs
        )
    


if __name__ == '__main__':
    app.run(debug=True)
