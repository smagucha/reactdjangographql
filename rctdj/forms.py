from .models import Ticket
from django.forms import ModelForm


class ticketform(ModelForm):
	class Meta:
		model = Ticket
		fields = '__all__'