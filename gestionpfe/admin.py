from django.contrib import admin
from .models import *
# Register your models here.

admin.site.site_header = "Departement Administration"
admin.site.site_title = "Your Admin site"
admin.site.index_title = "WELCOME"

admin.site.register(DemandeStageMonome)
admin.site.register(DemandeStageBinome)
