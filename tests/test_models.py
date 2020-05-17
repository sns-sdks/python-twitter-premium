"""
    data model tests
"""

import twitter.models as models


def test_user(helpers):
    user_data = helpers.load_json_data("testdata/models/user_data.json")

    user = models.User.new_from_json_dict(user_data)

    assert user.id == 6253282
