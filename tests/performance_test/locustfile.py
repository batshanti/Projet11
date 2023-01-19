from locust import HttpUser, task


class PerfTest(HttpUser):

    @task
    def index(self):
        self.client.get('/')

    @task
    def points(self):
        self.client.get("/clubs_points")

    @task
    def login(self):
        self.client.post("/showSummary", data={"email": "john@simplylift.co"})

    @task
    def purchase(self):
        self.client.post(
            "/purchasePlaces",
            data={
                "competition": "Spring Festival",
                "club": "Simply Lift",
                "places": 1
            }
        )

    @task
    def logout(self):
        self.client.get("/logout")
