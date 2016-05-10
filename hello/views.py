from django.shortcuts import render
from django.http import HttpResponse

from .models import Greeting

# Create your views here.
def index(request):
    # return HttpResponse('Hello from Python!')
    return render(request, 'index.html')


def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, 'db.html', {'greetings': greetings})
    
def home(request):
	news = Registration.objects.all()
	newsdetail = {
		"newsinfo" : news
	}
	print newsdetail
	return render_to_response('index.html',
	newsdetail, context_instance=RequestContext(request))

