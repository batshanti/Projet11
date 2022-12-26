class TestPurchasePlaces:

    def test_detucted_points_and_places(self, client):
        response = client.post(
            "/purchasePlaces",
            data={
                "competition": "Spring Festival",
                "club": "Simply Lift",
                "places": 10
            },
            follow_redirects=True
        )
        data = response.data.decode()
        assert "Great-booking complete!" in data
        assert "Points available: 15" in data
        assert "Number of Places: 15" in data

    def test_book_more_12_places(self, client):
        response = client.post(
            "/purchasePlaces",
            data={
                "competition": "Spring Festival",
                "club": "Simply Lift",
                "places": 13
            },
            follow_redirects=True
        )
        data = response.data.decode()
        assert "book more than 12 places in a competition" in data

    def test_book_more_places_than_points(self, client):
        response = client.post(
            "/purchasePlaces",
            data={
                "competition": "Spring Festival",
                "club": "Iron Temple",
                "places": 5
            },
            follow_redirects=True
        )
        data = response.data.decode()
        assert "You don&#39;t have enough points." in data