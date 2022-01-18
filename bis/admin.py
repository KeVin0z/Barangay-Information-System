from django.contrib import admin
from .models import Resident
from .models import Official
from .models import Blotter

admin.site.register(Resident)
admin.site.register(Official)
admin.site.register(Blotter)
