
from flask import Flask, render_template
import requests

app = Flask(__name__) # set Flask app instance
    # __name__ help Flask locate resources

api_key ='' # replace your actual api key
headers = {'X-Auth-Token': api_key}
url = "http://api.football-data.org/v4/matches"

def fetch_scores():
    """
    fetch live football match scores from external API

    Returns:
        list: list of dict match data for top 5 matches, return empty list if not matches 
        str: an error message if exception occurs
    """
    response = requests.get(url, headers=headers)
    try:
        data = response.json()
        if 'matches' in data and len(data['matches']) > 0:
            matches = data['matches'][:5]
            return matches
        else:
            return []
    except Exception as e:
        return f"Error fetching data: {e}"

@app.route('/')
def load_index_page():
    """
    render index.html
    
    Returns:
        str: rendered html page
    """
    return render_template('index.html')

@app.route('/scores')
def load_scores_page():
    """
    renders scores.html with current live scores
    
    Returns:
        str: rendered html content of scores page 
    """
    live_scores = fetch_scores()
    return render_template('scores.html')


# debug provide detailed error message, server auto reload etc
if __name__ == "__main__":
    app.run(debug=True)