from django.forms import ModelForm, DateInput, Form
from course.models import Calendar

class Html5DateInput(DateInput):
    input_type = 'date'

class CalendarForm(ModelForm):
    class Meta:
        model = Calendar
        fields = [ 'subject', 'date', 'body' ]
        widgets = {
            'date': Html5DateInput(),
        }