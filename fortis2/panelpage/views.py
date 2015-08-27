from django.shortcuts import render
from .forms import EnterPanelForm
from .models import EnterPanel
# Create your views here.


def home(request):

	form = EnterPanelForm(request.POST or None)
	panel_info = EnterPanel.objects.all()
	context = {
	"form": form,
	"panel_detail": panel_info
	}
	if 'enter' in request.POST:
		if form.is_valid():
			instance = form.save(commit = False)
			if instance.panelSublocation != "":
				instance.panelLocation += "-"+instance.panelSublocation
			instance.save()
			# print("ID = {}".format(instance.id))

	if 'delete' in request.POST:
	 	panelsToRemove = request.POST.getlist("choices")
	 	for panel in panelsToRemove:
	 		panel_info.filter(id = panel).delete()
	 		# print(panel)

	# print("Request = {}".format(request.POST.getlist("choices")))
	return render(request, "home.html", context)