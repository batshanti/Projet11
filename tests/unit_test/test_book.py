class TestBooking:

    def test_display_valid_competition(self, client):
        response = client.get("book/Spring Festival/Simply Lift")
        data = response.data.decode()
        assert response.status_code == 200
        assert 'Spring Festival' in data
        assert 'Places available: 25' in data

    def test_display_invalid_competition(self, client):
        response = client.get("book/invalidCompetition/invalidClubs")
        data = response.data.decode()
        assert 'Competition or club not found' in data
