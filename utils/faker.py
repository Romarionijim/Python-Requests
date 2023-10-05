from faker import Faker


class Randomizer:
    fake = Faker()

    @staticmethod
    def generate_Random_name():
        fake_name = Randomizer.fake.first_name()
        return fake_name

    @staticmethod
    def generate_random_lastname():
        fake_lastname = Randomizer.fake.last_name()
        return fake_lastname

    @staticmethod
    def generate_random_address():
        fake_address = Randomizer.fake.address()
        return fake_address

    @staticmethod
    def generate_random_numbers():
        faker_numbers = Randomizer.fake.random_int(min=100, max=1000)
        return faker_numbers

    @staticmethod
    def generate_random_email():
        fake_email = Randomizer.fake.email()
        return fake_email

    @staticmethod
    def generate_female_name():
        faker_name = Randomizer.first_name_female()
        return faker_name

    @staticmethod
    def generate_male_name():
        faker_name = Randomizer.first_name_male()
        return faker_name
