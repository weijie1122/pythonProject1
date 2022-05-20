import pytest
from comm import Email
import os

if __name__=='__main__':
    #pytest.main(['-v'])
    os.system('allure generate ../allure-result  -o ../report --clean')

    #email=Email.send_email()

