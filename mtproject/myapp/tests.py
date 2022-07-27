import imp
from django.test import TestCase
from myapp.forms.email import Email
from myapp.forms.boardform import BoardForm


# Create your tests here.
class FormTests(TestCase):
    
    def test_form(self):
        print((BoardForm({'title':'ssgnaverdafdaadafdadfadadadfadfafd'}).errors.as_text()))

