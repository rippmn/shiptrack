from flask import Flask, jsonify
import json

app = Flask(__name__)

def load_packages():
    """Loads package data from the packages.json file."""
    try:
        with open('packages.json', 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        return []

@app.route('/packages/<string:packageId>', methods=['GET'])
def get_package(packageId):
    """Retrieves package information by packageId."""
    packages = load_packages()
    if not packages:
        return jsonify({'error': 'No packages found or error loading data'}), 500

    for package in packages:
        if package.get('packageId') == packageId:
            return jsonify(package), 200

    return jsonify({'error': 'Package not found'}), 404

@app.errorhandler(404)
def not_found(error):
    return jsonify({'error': 'Not found'}), 404

@app.errorhandler(500)
def internal_error(error):
    return jsonify({'error': 'Internal Server Error'}), 500

@app.route('/discovery', methods=['GET'])
def discovery():
    """Implements the discovery endpoint."""
    return jsonify({
        "name": "shiptrack",
        "version": "1.0",
        "owner": "lonestar",
        "team": "N/A"
    })

#Generate the liveness and readiness routes
@app.route('/liveness', methods=['GET'])

def liveness():
    """Implements the liveness endpoint."""
    return jsonify({"status": "live", "code": 200})

@app.route('/readiness', methods=['GET'])

def readiness():
    """Implements the readiness endpoint."""
    return jsonify({"status": "ready", "code": 200})



if __name__ == '__main__':
    app.run(debug=True)
