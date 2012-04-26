from getfeatured.models import Lead, Contact
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.template import Context, loader
from django.template import RequestContext
from django.shortcuts import render_to_response, get_object_or_404
from django.core.context_processors import csrf

  

def detail(request):
    c = {}
    c.update(csrf(request))
    return render_to_response('testgetfeaturedform.html', c)

def submit(request):
    if request.method == 'POST':
        c = Contact()
        Contact(request.POST)
        c.save()  
        return render_to_response('getfeaturedSubmit.html',{
            'form': form,
            })

"""
def submit(request):
    if request.method == 'POST': # If the form has been submitted...
        form = ContactForm(request.POST) # A form bound to the POST data
        if form.is_valid(): 
            contact = form.save()  # Process the data in form.cleaned_data
            return HttpResponseRedirect('/submit/') # Redirect after POST
    else:
        form = ContactForm() # An unbound form

    return render_to_response('getfeaturedSubmit.html', {
        'form': form,
    })


def submitandnew(request, lead_id):
    l = get_object_or_404(Lead, pk=lead_id)
    try:
        selected_contact = l.contact_set.get(pk=request.POST['contact'])
    except (KeyError, Contact.DoesNotExist):
        # link to submitted page
        return render_to_response('getfeaturedSubmit.html', {
            'lead': l,
            'error_message': "You didn't select a choice.",
        }, context_instance=RequestContext(request))
    else:
        selected_contact.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('getfeatured.views.submit', args=(l.id,)))
"""
