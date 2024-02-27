'''
accounts/factories.py
'''
import factory
from django.contrib.auth import get_user_model

class CustomUserFactory(factory.django.DjangoModelFactory):
    '''
    This class handles the custom user factory.
    '''
    class Meta:
        '''
        This class handles the meta data of the custom user factory.
        '''
        model = get_user_model()  # Use get_user_model() to get the User model

    username = factory.Faker('user_name')
    email = factory.Faker('email')
    age = factory.Faker('random_int', min=18, max=99)
    gender = factory.Faker('random_element', elements=('Male', 'Female'))
