from django.shortcuts import render
from django.utils import timezone
from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect

from .models import Site, Contact
from .forms import ContactForm

def site_list(request):
	sites = Site.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
	return render(request, 'work/site_list.html', {'sites': sites})
	
def site_detail(request, pk):
	site = get_object_or_404(Site, pk=pk)
	return render(request, 'work/site_detail.html', {'site': site})
	
def contact_new(request):
	if request.method == "POST":
		form = ContactForm(request.POST)
		if form.is_valid():
			post = form.save(commit=False)
			post.sent_date = timezone.now()
			post.save()
			return redirect('contact_detail', pk=post.pk)
	else:
		form = ContactForm()
	return render(request, 'work/contact_edit.html', {'form': form})
	
def contact_detail(request, pk):
	contact = get_object_or_404(Contact, pk=pk)
	return render(request, 'work/contact_detail.html', {'contact': contact})
	
def contact_edit(request, pk):
	contact = get_object_or_404(Contact, pk=pk)
	if request.method == "POST":
		form = ContactForm(request.POST)
		if form.is_valid():
			post = form.save(commit=False)
			post.sent_date = timezone.now()
			post.save()
			return redirect('contact_detail', pk=post.pk)
	else:
		form = ContactForm(instance=contact)
	return render(request, 'work/contact_edit.html', {'form': form})