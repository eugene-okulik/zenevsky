import allure


class Endpoint:
    url = 'http://167.172.172.115:52353/object'
    response = None
    json = None
    headers = {'Content-type': 'application/json'}

    @allure.step('Check that response is 200')
    def check_that_status_is_200(self):
        assert self.response.status_code == 200

    @allure.step('Check that 400 error received')
    def check_that_status_is_400(self):
        assert self.response.status_code == 400

    @allure.step('Check that 404 error received')
    def check_that_status_is_404(self):
        assert self.response.status_code == 404
