import os
import pytest

# pytest args에 인수 추가

@pytest.fixture
def csv_file(tmpdir):
    with open(os.path.join(tmpdir, 'test.csv'), 'w+') as c:
        print('before test')
        yield c
        print('after test')

def pytest_addoption(parser):
    parser.addoption('--os-name', default='linux', help='os_name')
