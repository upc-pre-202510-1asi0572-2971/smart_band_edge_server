"""

"""
from flask import Flask

from iam.infrastructure.repositories import get_or_create_test_device
from shared.infrastructure.database import init_db

app = Flask(__name__)

init_db()
get_or_create_test_device()

if __name__ == '__main__':
    app.run(host="localhost", port=3000, debug=True)