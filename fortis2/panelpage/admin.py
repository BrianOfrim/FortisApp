from django.contrib import admin

# Register your models here.

from .forms import EnterPanelForm
from .models import EnterPanel

class PanelEnterAdmin(admin.ModelAdmin):
	list_display = ["__str__"]
	form = EnterPanel

admin.site.register(EnterPanel)
# admin.site.register(EnterPanel, EnterPanelForm)