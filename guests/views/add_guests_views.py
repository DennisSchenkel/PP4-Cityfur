from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from ..models import Guest
from ..forms import AddGuest

# Function for adding guest to database including an image upload.
def add_guest_view(request):

    if request.method == 'POST':
        form = AddGuest(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
        
    else:
        form = AddGuest()
            
    return render(request, 'guests/add_guest_temp.html', {'form': form})
    
# Function for updating guest information
def update_guest_view(request, id):
    guest = get_object_or_404(Guest, id=id)
    
    if request.method == 'POST':
        form = AddGuest(request.POST, request.FILES, instance=guest)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
        
    else:
        form = AddGuest(instance=guest)
    
    return render(request, 'guests/update_guest_temp.html', {'form': form})