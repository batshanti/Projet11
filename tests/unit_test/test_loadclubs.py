import server


def test_loadclubs_should_return_clubs_list():

    expected_result = [
        {
            "name": "Simply Lift",
            "email": "john@simplylift.co",
            "points": "25"
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
        }]
    assert server.loadClubs() == expected_result
