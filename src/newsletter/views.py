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
	if form.is_valid():
		for key, value in form.cleaned_data.iteritems():
			print key, value
	context = {
		"form": form
	}
	return render(request,"forms.html", context)

def about(request):
	context={

	}
	return render(request, "about.html", context)

def newsletter(request):
	context={
	
	}
	return render(request, "newsletter.html", context)

def archive(request):
	context={
	
	}
	return render(request, "archive.html", context)

def bookbearletters(request):
	context={
	
	}
	return render(request, "bookbearletters.html", context)