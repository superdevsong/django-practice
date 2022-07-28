from django.forms import ModelForm
from myapp.models import Board

#boardform
class BoardForm(ModelForm):
    class Meta:
        model = Board
        fields = ['board_title','board_text']
        
