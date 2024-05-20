from django.shortcuts import render
from django.http import HttpResponseRedirect
from ..models import Guest
from ..forms import AddGuest

# View class for guest list
def add_guest(request):

    request.method == 'Post'
    form = AddGuest(request.POST)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect('/')
        
    form = AddGuest
    return render(request, 'guests/add_guest.html', {'form': form})
    

