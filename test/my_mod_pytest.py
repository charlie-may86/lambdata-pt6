'''
This testing method allows to remove the __init__.py file from the 
test folder

Also allows me to make the change to my setup.py file back to 
packages=find_packages() 

But, I can't do that until I go test all the other files with same
style, which I will wait for because the exam wants the other style
of testing.


NEED TO ADD a conftest.py file into the folder
'''


from my_lambdata6.my_mod import enlarge

def test_enlarge():
    assert enlarge(7) == 700

