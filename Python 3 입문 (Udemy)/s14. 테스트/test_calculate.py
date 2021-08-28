import pytest
import os

import calculate

# nose python test https://nose.readthedocs.io/en/latest/

# https://docs.pytest.org/en/6.2.x/
# pip install pytest
# >>> pytest -v -rs --os-name=windows -s

# 
# pip install pytest-cov pytest-xdist
# >>> pytest test_calculate.py --cov=calculate --cov-report term-missing
# ...
# ---------- coverage: platform darwin, python 3.9.6-final-0 -----------
# Name           Stmts   Miss  Cover   Missing
# --------------------------------------------
# calculate.py      14      0   100%
# --------------------------------------------
# TOTAL             14      0   100%
# ...

# def test_add_num_and_double():
#     cal = calculate.Cal()
#     assert cal.add_num_and_double(1,1) == 4

is_release = True

class TestCal(object):
    
    @classmethod
    def setup_class(cls):
        print('setup_class')
        cls.cal = calculate.Cal()
        cls.test_dir = '/tmp/test_dir'
        cls.test_file_name = 'test.txt'
        
    @classmethod
    def teardown_class(cls):
        print('teardown_class')
        
        import shutil
        if os.path.exists(cls.test_dir):
            shutil.rmtree(cls.test_dir)
        del cls.cal
    
    def setup_method(self, method):
        print('method={}'.format(method.__name__))
#         self.cal = calculate.Cal()
        
    def teardown_method(self, method):
        print('method={}'.format(method.__name__))
#         del self.cal

#     def test_add_num_and_double(self, request):
#         os_name = request.config.getoption('--os-name')
#         print(os_name)
#         if os_name == 'mac':
#             print('ls')
#         elif os_name == 'windows':
#             print('dir')
#         assert self.cal.add_num_and_double(1,1) == 4

    def test_save_no_dir(self):
        self.cal.save(self.test_dir, self.test_file_name)
        test_file_path = os.path.join(
            self.test_dir, self.test_file_name
        )
        assert os.path.exists(test_file_path) is True

    def test_add_num_and_double(self, csv_file):
        print(csv_file)
        assert self.cal.add_num_and_double(1,1) == 4
        
    def test_save(self, tmpdir):
        self.cal.save(tmpdir, self.test_file_name)
        test_file_path = os.path.join(
            tmpdir, self.test_file_name
        )
        assert os.path.exists(test_file_path) is True
        
#    @pytest.mark.skip(reason='skip!')
#    @pytest.mark.skipif(is_release == True, reason='skip!')
    def test_add_num_and_double_raise(self):
        with pytest.raises(ValueError):
            self.cal.add_num_and_double('1', '1')
