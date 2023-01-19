import server


expected_clubs_result = [
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

expected_competition_result = [
    {
            "name": "Spring Festival",
            "date": "2023-03-27 10:00:00",
            "numberOfPlaces": "25"
        },
        {
            "name": "Fall Classic",
            "date": "2023-10-22 13:30:00",
            "numberOfPlaces": "3"
        },
        {
            "name": "test past",
            "date": "2020-10-22 13:30:00",
            "numberOfPlaces": "13"
        },
        {
            "name": "test competition",
            "date": "2024-10-22 13:30:00",
            "numberOfPlaces": "20"
    }
]


class TestServer:

    def test_server(self, client):

        assert server.loadCompetitions("tests/test_competitions.json") == expected_competition_result
        assert server.loadClubs("tests/test_clubs.json") == expected_clubs_result

        response = client.get("/")
        data = response.data.decode()
        assert response.status_code == 200
        assert "Welcome to the GUDLFT Registration Portal" in data

        response = client.post("/showSummary", data={'email': 'john@simplylift.co'}, follow_redirects=True)
        data = response.data.decode()
        assert response.status_code == 200
        assert "Welcome, john@simplylift.co" in data

        response = client.get("book/Spring Festival/Simply Lift")
        data = response.data.decode()
        assert response.status_code == 200
        assert 'Spring Festival' in data
        assert 'Places available: 25' in data

        response = client.get("/logout", follow_redirects=True)
        data = response.data.decode()
        assert response.status_code == 200
        assert "Welcome to the GUDLFT Registration Portal" in data








