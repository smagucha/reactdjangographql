from django.contrib import admin
from django.apps import apps
from .models import Movie, Customer, Buses, Routes, Ticket


admin.site.register(Movie)

app= apps.get_app_config('graphql_auth')

for model_name, model in app.models.items():
	admin.site.register(model)


admin.site.register(Customer)
admin.site.register(Buses)
admin.site.register(Routes)
admin.site.register(Ticket)



