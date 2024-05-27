from django.shortcuts import render
from django.http import HttpResponseRedirect
# from ..models import Guest
from ..forms import AddGuest

# Function for adding guest to database including an image upload.
def add_guest_form(request):

    request.method == 'Post'
    form = AddGuest(request.POST, request.FILES)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect('/')
        
    return render(request, 'guests/add_guest.html', {'form': form})
    