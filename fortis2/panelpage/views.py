from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from .forms import EnterPanelForm, PageOptionsForm
from .models import EnterPanel, PageOptions
# Create your views here.

def home(request):
	form = PageOptionsForm(request.POST or None)
	context = {
	"form":form,
	}

	if 'enter' in request.POST:
		print(request.POST)
		selected_choice = request.POST["pageChoice"]
		print(selected_choice)

		# instance = form.save(commit = False)
		print(selected_choice)
		return HttpResponseRedirect(selected_choice)
	return render(request,"home.html", context)



def office(request):

	form = EnterPanelForm(request.POST or None)
	panel_info = EnterPanel.objects.all()
	context = {
	"form": form,
	"panel_detail": panel_info
	}
	if 'enter' in request.POST:
		if form.is_valid():
			instance = form.save(commit = False)
			if (instance.panelSublocation != "") and (instance.panelLocation[0] == "R"):
				instance.panelLocation += "-"+instance.panelSublocation
			instance.save()
			# print("ID = {}".format(instance.id))

	if 'delete' in request.POST:
	 	panelsToRemove = request.POST.getlist("choices")
	 	for panel in panelsToRemove:
	 		panel_info.filter(id = panel).delete()
	 		# print(panel)

	# print("Request = {}".format(request.POST.getlist("choices")))
	return render(request, "office.html", context)

def worker(request):

	return render(request,"worker.html",[])