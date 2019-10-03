from flask import Flask, render_template, request
import requests
import json
import os
from dotenv import load_dotenv
load_dotenv()

app = Flask(__name__, static_url_path='/static')

apikey = os.getenv("TENOR_API_KEY")


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
    show_random = request.args.get('show_random')

    
    #this if statement checks to see if the show trending button has been pressed, if it has been pressed then it will take the trending reequest
    #from the api and hand it to index to display those gifs
    

    if show_trending:
        r = requests.get("https://api.tenor.com/v1/trending?key=XFF92IL8UZZG")

        json_gifs = json.loads(r.content)
        gifs = json_gifs['results']
        return render_template(
            'index.html',
            gifs=gifs
        )

    # this if statement checks if the show random button has been pressed
    # if it has then it will make a call to the random portion of the tenor api
    # then pass that json data to index to display the random gifs

    elif show_random:
        r = requests.get("https://api.tenor.com/v1/random?", params=params)
        json_gifs = json.loads(r.content)
        gifs = json_gifs['results']
        return render_template(
            'index.html',
            gifs=gifs
        )

    # this portion of the function will place the given search term into the api request
    # and hand the json data associated with the search term to index to display
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
                search_term=search_term
            )
        elif r.status_code != 200:
            return render_template('index.html',
            error = "Could not find any gifs"
            )


        else:
            return render_template(
                'error.html'
            )
        

    # this else statement will run anytime the page is freshly loaded
    # it will load gifs based on an empty search term, which the api will use to display some gifs anyway
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
