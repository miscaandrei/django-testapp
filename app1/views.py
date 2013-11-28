from django.http import *
import datetime
from django.shortcuts import *
from ayuda import *
# Create your views here.
#return render_to_response('sometemplate.html')

def basic(request):
    return HttpResponse("Hello world")

def data_hora(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)

def clients(request):
    return render_to_response('clients.html')


def contact(request):
    if request.method == 'POST': # If the form has been submitted...
        form = ContactForm(request.POST) # A form bound to the POST data
        if form.is_valid(): # All validation rules pass
            # Process the data in form.cleaned_data
            # ...
            return HttpResponseRedirect('/thanks/') # Redirect after POST
    else:
        form = ContactForm() # An unbound form

    return render(request, 'contact.html', {
        'form': form,
    })