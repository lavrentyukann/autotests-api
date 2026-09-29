from faker import Faker

fake = Faker('ru_RU')

print(fake.name())
print(fake.address())
print(fake.email())

data ={
    "name": fake.name(),
    "email": fake.email(),
    "age": fake.random_int(18, 100)
}

print(data)

