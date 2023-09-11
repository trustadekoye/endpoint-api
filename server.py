from flask import Flask, request, jsonify
from flask_cors import CORS
import datetime
import pytz

app = Flask(__name__)
CORS(app)


@app.route('/api', methods=['GET'])
def get_info():
    slack_name = request.args.get('slack_name')
    track = request.args.get('track')

    if not slack_name or not track:
        return jsonify({'error': 'slack_name and track parameters are required'}), 400

    current_day = datetime.datetime.now(pytz.utc).strftime('%A')
    current_time = datetime.datetime.now(pytz.utc)
    delta = datetime.timedelta(minutes=2)
    time_minus_two = current_time - delta
    time_plus_two = current_time + delta
    utc_time = current_time.strftime('%Y-%m-%dT%H:%M:%SZ')

    github_file_url = "https://github.com/trustadekoye/Python_calculator/blob/main/README.md"
    github_repo_url = "https://github.com/trustadekoye/Python_calculator"

    response_data = {
        "slack_name": slack_name,
        "current_day": current_day,
        "utc_time": utc_time,
        "track": track,
        "github_file_url": github_file_url,
        "github_repo_url": github_repo_url,
        "status_code": 200
    }

    return jsonify(response_data)


if __name__ == '__main__':
    app.run(debug=True)
