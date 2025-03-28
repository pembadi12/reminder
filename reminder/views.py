from django.shortcuts import get_object_or_404, render, redirect


from .models import Event
from .forms import EventForm

def event_list(request):
    events = Event.objects.all()
    form = EventForm()
    return render(request, 'event_list.html', {'events': events, 'form': form})

def add_event(request):
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            form.save()
            
    return redirect('event_list')

def delete_event(request, event_id):
    event = Event.objects.get(id=event_id)
    event.delete()
    return redirect('event_list')

def event_edit(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    if request.method == "POST":
        event.title = request.POST['title']
        event.date = request.POST['date']
        event.description = request.POST['description']
        event.save()
        return redirect('event_list')
    return render(request, 'event_edit.html', {'event': event})

