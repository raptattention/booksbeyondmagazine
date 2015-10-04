from django.shortcuts import render

from .forms import ContactForm, SignupForm
# Create your views here.
def home(request):
	title = "Welcome"
	form = SignupForm(request.POST or None)
	context = {
		'title': title,
		'form': form
	}

	if form.is_valid():
		# form.save()
		instance = form.save(commit=False)

		if not instance.fullname:
			instance.fullname = "New full name"
		instance.save()
		context = {
			'title': 'Thank you'
		}

	return render(request, "home.html", context)

def contact(request):
	form = ContactForm(request.POST or None)
	context = {
		"form": form
	}
	return render(request,"forms.html", context)