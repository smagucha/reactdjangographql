from django.shortcuts import render
from django.http import HttpResponse
from .forms import  ticketform
from .models import Ticket


def home(request, id):
	ticketid = Ticket.objects.get(id=id)
	if request.method == 'POST':
		form = ticketform(request.POST, instance=ticketid or None)
		if form.is_valid:
			form.save()
	else:
		form = ticketform(instance=ticketid or None)


	context = {
		'form': form
	}
	return render(request, 'rctdj/home.html', context)






