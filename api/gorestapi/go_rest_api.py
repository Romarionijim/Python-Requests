from api.api_requests.api_requests import ApiRequests
from api.urls.api_urls import ApiUrls
from api.endpoints.api_endpoints import ApiEndpoints
from utils.faker import Randomizer


class GoRestApi(ApiRequests):
    __base_url = ApiUrls.GOREST_API_URL.value
    __users_end_point = ApiEndpoints.USERS.value

    def get_users(self):
        response = self.get(f"{self.__base_url}/{self.__users_end_point}")
        return response

    def __get_gender_count(self, gender):
        users_response = self.get_users()
        response_json = users_response.json()
        gender_filter = lambda g: g.get("gender") == gender
        gender_count = len(list(filter(gender_filter, response_json)))
        return gender_count

    def get_male_count(self):
        return self.__get_gender_count("male")

    def get_female_count(self):
        return self.__get_gender_count("female")

    def create_even_genders(self):
        responses = []
        male_count = self.get_male_count()
        female_count = self.get_female_count()
        difference = abs(male_count - female_count)
        if male_count == female_count:
            print("both genders are equal")
            return
        elif male_count > female_count:
            female_data = {
                "id": Randomizer.generate_random_numbers(),
                "name": Randomizer.generate_Random_name(),
                "email": Randomizer.generate_random_email(),
                "gender": "female",
                "status": "active",
            }
            for i in range(difference):
                response = self.post(f"{self.__base_url}/{self.__users_end_point}", female_data, True)
                responses.append(response)

        elif male_count < female_count:
            male_data = {
                "id": Randomizer.generate_random_numbers(),
                "name": Randomizer.generate_Random_name(),
                "email": Randomizer.generate_random_email(),
                "gender": "male",
                "status": "active",
            }
            for i in range(difference):
                response = self.post(f"{self.__base_url}/{self.__users_end_point}", male_data, True)
                responses.append(response)

        return responses

    def get_inactive_users(self):
        users_list = self.get_users()
        response_json = users_list.json()
        inactive_status_filter = lambda s: s.get("status") == "inactive"
        inactive_users = list(filter(inactive_status_filter, response_json))
        return inactive_users

    def delete_inactive_users(self):
        responses = []
        inactive_users = self.get_inactive_users()
        inactive_users_id = lambda usrId: usrId.get("id")
        users_id_filtering = list(map(inactive_users_id, inactive_users))
        for user_id in users_id_filtering:
            response = self.delete(f"{self.__base_url}/{self.__users_end_point}/{user_id}", True)
            responses.append(response)

        return responses

    def __extract_email_extension(self, email: str):
        email_domain = email.split('@').pop()
        email_extension = email_domain.split('.')[-1]
        print(email_extension)
        return email_extension

    # filters all the email that do not have the .co.il extension
    def replace_email_extension(self):
        responses = []
        users_list = self.get_users()
        json_list = users_list.json()
        for users in json_list:
            emails = users.get("email")
            current_extension = self.__extract_email_extension(emails)
            if current_extension != 'co.il':
                new_extension = emails.replace(current_extension, 'co.il')
                new_email = {
                    "email": new_extension
                }
                response = self.patch(f"{self.__base_url}/{self.__users_end_point}/{users.get('id')}", new_email, True)
                responses.append(response)

        return responses

        # email_filter = lambda mail: mail.get("email")
        # emails_list = list(map(email_filter, json_list))
        # for email in emails_list:
        #     mail_extension = self.__extract_email_extension(email)
        #     if mail_extension != 'co.il':
        #         response = self.patch(f"{self.__base_url}/{self.__users_end_point}/{}")

    # check if email extension are != .co.il - and replace them all with the .co.il extension