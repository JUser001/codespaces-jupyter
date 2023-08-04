#%%
from faker import Faker

#%%
faker = Faker('ko_KR')  # 한국어 데이터를 생성하기 위해 'ko_KR' locale을 설정합니다

name = faker.name()
job = faker.job()

#%%
address = faker.address()

#%%
print(name, job, address)
print(f'name: {name}, job: {job}, address: {address}')
# %%
