import pytest
import os
import text

read_all_data = [
    ('test.txt', 'Lalala'),
    ('hello.txt', 'Hello world!'),
    ('hello.txt', 'Some other text!  '),
    ('multiline', 'One\nTwo\nThree')
]

@pytest.mark.parametrize('data', read_all_data)
def test_read_all(data):
    # noinspection PyArgumentList
    try:
        with open(data[0], 'w') as file:
            file.write(data[1])
        assert text.read_all(data[0]) == data[1]
    except:
        pytest.fail()
    finally:
        if os.path.exists(data[0]):
            os.remove(data[0])
