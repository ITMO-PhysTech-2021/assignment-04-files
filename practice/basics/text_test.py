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
    except Exception as e:
        pytest.fail(str(e))
    finally:
        if os.path.exists(data[0]):
            os.remove(data[0])


sum_two_data = [
    (('nums.txt', '1 2'), 3),
    (('nums.txt', '1 2 3'), 3),
    (('nums.txt', '20000 450'), 20450),
    (('numbers.txt', '-1 3 5 22 100 251 400 416'), 2)
]


@pytest.mark.parametrize('data', sum_two_data)
def test_sum_two(data):
    # noinspection PyArgumentList
    try:
        with open(data[0][0], 'w') as file:
            file.write(data[0][1])
        assert text.sum_two(data[0][0]) == data[1]
    except Exception as e:
        pytest.fail(str(e))
    finally:
        if os.path.exists(data[0][0]):
            os.remove(data[0][0])
