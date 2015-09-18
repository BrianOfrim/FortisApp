from django import forms
from .models import EnterPanel, PageOptions


class EnterPanelForm(forms.ModelForm):
	class Meta:
		model = EnterPanel
		fields =  ['shipment','panelName','panelLocation','panelSublocation','generalNotes','crewInfo']
		widgets = {
		'shipment' : forms.Select(attrs={'class': 'inputClass' }),
		'panelName' : forms.TextInput(attrs={'class': 'inputClass' }),
		'panelLocation' : forms.Select(attrs={'class': 'inputClassDD' }),
		'panelSublocation' : forms.Select(attrs={'class': 'inputClass' }),
		'generalNotes': forms.TextInput(attrs={'class': 'inputClass' }),
		'crewInfo': forms.TextInput(attrs={'class': 'inputClass' }),

		}

	def clean_shipment(self):
		shipment = self.cleaned_data.get('shipment')
		return shipment

	def clean_panelName(self):
		panelName = self.cleaned_data.get('panelName')
		return panelName

	def clean_panelLocation(self):
		panelLocation = self.cleaned_data.get('panelLocation')
		return panelLocation

	def clean_panelSublocation(self):
		panelSublocation = self.cleaned_data.get('panelSublocation')
		return panelSublocation

	def clean_generalNotes(self):
		generalNotes = self.cleaned_data.get('generalNotes')
		return generalNotes

	def clean_crewInfo(self):
		crewInfo = self.cleaned_data.get('crewInfo')
		return crewInfo




class PageOptionsForm(forms.ModelForm):
	class Meta:
		model = PageOptions
		fields = ["pageChoice"]

	def clean_pageChoice(self):
		pageChoice = self.cleaned_data.get('pageChoice')



# class UnknownForm(forms.Form):
#     choices = forms.MultipleChoiceField(
#         choices = panel_list, # this is optional
#         widget  = forms.CheckboxSelectMultiple,
#     )


