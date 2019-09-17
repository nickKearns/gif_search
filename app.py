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
    #GET THE SEARCH TERM FROM THE SEARCH BOX IN THE HOME PAGE
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
    
    #get the data from the api using the apikey, the limit and the search term that the user has supplied
    

    r = requests.get("https://api.tenor.com/v1/search?", params = params)




    if r.status_code == 200:
        # TODO: Use the '.json()' function to get the JSON of the returned response
        # object
        json_gifs = json.loads(r.content)
        gifs = json_gifs['results']



        print(gifs)
        return render_template(
            'index.html',
            gifs=gifs,
            #search_term = search_term
        )









    

    
    #convert that data into json data


    # TODO: Using dictionary notation, get the 'results' field of the JSON,
    # which contains the GIFs as a list



    
    #assign the "results" portion of the json data to a variable called gifs, which should be a list of objects
    
    # TODO: Render the 'index.html' template, passing the list of gifs as a
    # named parameter called 'gifs'



    
    #Pass index.html the list of gifs and the search term that was used to get those gifs.
    






if __name__ == '__main__':
    app.run(debug=True)
