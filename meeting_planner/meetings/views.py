from django.shortcuts import render, get_object_or_404, redirect

from .models import Meeting, Room
from .forms import MeetingForm


def detail(request, id):
    meeting = get_object_or_404(Meeting, pk=id)
    return render(request, "meetings/detail.html", {"meeting": meeting})


def rooms_list(request):
    rooms = Room.objects.all()
    return render(request, "meetings/room_list.html", {"rooms": rooms} )


def new(request):
    if request.method == "POST":
        form = MeetingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        form = MeetingForm()
    return render(request, "meetings/new.html", {"form": form})
