def test_login_exist_email(client):
    response = client.post("/showSummary", data={'email': 'unknow@test.co'}, follow_redirects=True)
    data = response.data.decode()
    assert response.status_code == 200
    assert "Sorry" in data
