import server


def test_loadclubs_should_return_clubs_list():
    expected_result = [
        {
            "name": "Simply Lift",
            "email": "john@simplylift.co",
            "points": "13"
        },
        {
            "name": "Iron Temple",
            "email": "admin@irontemple.com",
            "points": "4"
        },
        {
            "name": "She Lifts",
            "email": "kate@shelifts.co.uk",
            "points": "12"
        },
        {
            "name": "test club",
            "email": "testclub@gmail.com",
            "points": "20"
        }
    ]
    assert server.loadClubs("tests/test_clubs.json") == expected_result
