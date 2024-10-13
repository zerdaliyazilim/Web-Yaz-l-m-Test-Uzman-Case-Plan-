from locust import HttpUser, TaskSet, task, between

class UserBehavior(TaskSet):
    @task(1)
    def view(self):
        """Ana sayfayı görüntüle."""
        self.client.get("/tr/")

    @task(2)
    def view_jobs(self):
        """Açık pozisyonlar sayfasını görüntüle."""
        self.client.get("/tr/#acik-pozisyonlar")

    @task(3)
    def search_job(self):
        """Belirli bir pozisyon için arama yap."""
        search_term = "Mühendis"  # Aramak istediğiniz pozisyonu değiştirin
        self.client.get(f"/tr/open-positions/?type=1&page=1&search={search_term}")

class WebsiteUser(HttpUser):
    """Locust kullanıcısı."""
    tasks = [UserBehavior]
    wait_time = between(1, 5)  # Kullanıcılar arasında 1 ila 5 saniye bekle
