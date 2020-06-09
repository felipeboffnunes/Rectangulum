import random
from faker import Faker


def create_table() -> list: 
    """Generates a matrix table with random random
    
    Returns:
        list: table
    """    
    
    # Table size
    columns = range(random.randint(2,8))
    rows = range(random.randint(2,8))
    
    table = [[generate_data() for row in rows] 
                             for column in columns]
    
    for i in table:
        print(i)
    return table

def generate_data() -> str:
    """Generates random data

    Returns:
        str: Random string
    """    
    
    # Data generator
    fake = Faker()
    fake_types = [fake.file_path, fake.license_plate, fake.color]
    
    # Select type 
    index = random.choice(fake_types)
    fake_data = index()

    return fake_data

create_table()