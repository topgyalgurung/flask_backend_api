from flask import Blueprint, request, jsonify
from extensions import db
from models.team import Team

team_bp = Blueprint("team", __name__)




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


# @team_bp.route("/teams", methods=["POST"])
# def create_team():
#     data = request.json
#     team = Team(name=data["name"], contact=data["contact"])

#     db.session.add(team)
#     db.session.commit()

#     return jsonify({"message": "Team created"}), 201

    # create new Team
    # new_team = Team(name="city", contact="city@gmail.com")
    # db.session.add(new_team)
    # db.session.commit()

    # # query for a team
    # team = Team.query.filter_by(name='city').first()

    # #update a team
    # team.contact = "new_name@gmail.com"
    # db.session.commit()