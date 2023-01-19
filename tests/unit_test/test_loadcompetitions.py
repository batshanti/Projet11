import server


def test_loadcompetition_should_return_competitions_list():
    expected_result = [
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
    assert server.loadCompetitions("tests/test_competitions.json") == expected_result
