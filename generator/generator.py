import random

from data.data import Person
from faker import Faker

faker_ru = Faker('ru_RU')
fake_en = Faker('En')
Faker.seed()


def generated_person():
    yield Person(
        first_name=fake_en.first_name(),
        last_name=fake_en.last_name(),
        login=fake_en.first_name(),
        password="qwerT1@#$",
        name=fake_en.first_name(),
        description=fake_en.text(max_nb_chars=20),
        email=fake_en.email(),
        phone=fake_en.phone_number(),
        telegram=fake_en.text(max_nb_chars=6),
        core_limit=random.randint(1, 8),
        run_job_limit=random.randint(1, 8),
        ram_limit=random.randint(1, 16),
        total_core_limit=random.randint(2, 16),
        total_ram_limit=random.randint(2, 16)
    )
