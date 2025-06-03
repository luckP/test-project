# Change from clone1 - new change
# Change from clone2 - new change
# Change from clone2
# Change from clone1

# test change 1asdlfalsdkjf

import asyncio
import aiohttp
from utils import test_function
from test2 import test2
import requests
from UserClass import User


def main():
    values = [x ** 2 for x in range(10)]
    a = 1
    values2 = [x + a for x in values]
    print(values2)

    b = 1
    values3 = [x + b for x in values]
    print(values3)

    # TEST NEW UTILS FILE
    print(test_function())

    test2()

    print("bla bla bla")

    # print(asyncio.run(fetchAsync()))

    # function3()

    # function2()

    # fucntion1()

    users = create_new_data(10)
    for u in users:
        print(u)


def fucntion1():
    my_list = [x for x in range(10)]

    for x in my_list:
        print(x)


def new_function():
    pass


def function2():
    print('asdf1')
    print('asdf2')
    print('asdf3')
    print('asdf4')
    print('asdf5')


def function3() -> None:
    url = 'https://en.wikipedia.org/wiki/Black_hole'
    r = requests.get(url)
    print(r.text)


async def fetchAsync():
    async with aiohttp.ClientSession() as session:
        async with session.get("https://en.wikipedia.org/wiki/Black_hole") as response:
            return await response.text()


def create_new_data(x):
    users = [User(f'name-{i}', i+20) for i in range(x)]
    return users


if __name__ == '__main__':
    main()
