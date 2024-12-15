from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse
from django.db.models import Q

from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

from .models import Room, Topic, Message
from .forms import RoomForm, UserForm


# Auth:
def login_page(request):
    if request.user.is_authenticated:
        return redirect("home")

    if request.method == "POST":
        username = request.POST.get("username").lower()
        password = request.POST.get("password")
        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, "User dose not exist")

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("home")
        else:
            messages.error(request, "Username or password dose not exist")

    context = {"page": "login"}
    return render(request, "login_signup.html", context)


@login_required(login_url="login")
def logout_user(request):
    logout(request)
    return redirect("home")


def signup_user(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request, user)
            return redirect("home")
        else:
            messages.error(
                request, "Something went wrong during signup, please try again later."
            )

    context = {"page": "signup", "form": form}
    return render(request, "login_signup.html", context)


# Home:
def home(request):
    q = request.GET.get("q") if request.GET.get("q") != None else ""

    rooms = Room.objects.filter(
        Q(topic__name__icontains=q)
        | Q(name__icontains=q)
        | Q(description__icontains=q)
        | Q(host__username__icontains=q)
    )[:10]
    topics = Topic.objects.all()[:5]
    room_count = rooms.count()
    activity = Message.objects.filter(Q(room__topic__name__icontains=q))[:5]

    context = {
        "rooms": rooms,
        "topics": topics,
        "room_count": room_count,
        "activity": activity,
    }
    return render(request, "home.html", context)


# Rooms:
def room(request, pk):
    try:
        room = Room.objects.get(id=pk)
        room_messages = room.message_set.all().order_by("-created")
        participants = room.participants.all()

        if request.method == "POST":
            message = Message.objects.create(
                user=request.user, room=room, body=request.POST.get("body")
            )
            room.participants.add(request.user)
            return redirect("room", pk=room.id)

        context = {
            "room": room,
            "room_messages": room_messages,
            "participants": participants,
        }
        return render(request, "room.html", context)
    except Room.DoesNotExist:
        return redirect("/")


def topics_page(request):
    q = request.GET.get("q") if request.GET.get("q") != None else ""
    topics = Topic.objects.filter(name__icontains=q)
    topics_sum = Topic.objects.count()

    context = {"topics": topics, "topics_sum": topics_sum}
    return render(request, "topics.html", context)


def activity_page(request):
    room_messages = Message.objects.all()[:5]

    context = {"activity": room_messages}
    return render(request, "activity.html", context)


@login_required(login_url="login")
def create_room(request):
    form = RoomForm()
    topics = Topic.objects.all()

    if request.method == "POST":
        topic_name = request.POST.get("topic")
        topic, created = Topic.objects.get_or_create(name=topic_name)

        Room.objects.create(
            host=request.user,
            topic=topic,
            name=request.POST.get("name"),
            description=request.POST.get("description"),
        )
        return redirect("home")

    context = {"form": form, "topics": topics, "head": "Create"}
    return render(request, "room_form.html", context)


@login_required(login_url="login")
def update_room(request, pk):
    room = Room.objects.get(id=pk)
    form = RoomForm(instance=room)
    topics = Topic.objects.all()

    if request.user != room.host:
        return HttpResponse(
            "You don't have the necessary permissions to perform this action"
        )

    if request.method == "POST":
        topic_name = request.POST.get("topic")
        topic, created = Topic.objects.get_or_create(name=topic_name)

        room.topic = topic
        room.name = request.POST.get("name")
        room.description = request.POST.get("description")
        room.save()

        return redirect(reverse("room", args=[pk]))

    context = {"form": form, "topics": topics, "room": room, "head": "Update"}

    return render(request, "room_form.html", context)


@login_required(login_url="login")
def delete_room(request, pk):
    room = Room.objects.get(id=pk)
    context = {"obj": room}

    if request.user != room.host:
        return HttpResponse(
            "You don't have the necessary permissions to perform this action"
        )

    if request.method == "POST":
        room.delete()
        return redirect("home")

    return render(request, "delete.html", context)


# Users:
def user_profile(request, pk):
    user = User.objects.get(id=pk)
    rooms = user.room_set.all()
    room_messages = user.message_set.all()[:5]
    topics = Topic.objects.all()[:5]

    context = {
        "user": user,
        "rooms": rooms,
        "activity": room_messages,
        "topics": topics,
    }
    return render(request, "profile.html", context)


@login_required(login_url="login")
def update_user(request):
    user = request.user
    form = UserForm(instance=user)

    if request.method == "POST":
        form = UserForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect("user-profile", pk=user.id)

    context = {"form": form}
    return render(request, "update_user.html", context)


@login_required(login_url="login")
def delete_message(request, pk):
    message = Message.objects.get(id=pk)
    context = {"obj": message}

    if request.user != message.user:
        return HttpResponse(
            "You don't have the necessary permissions to perform this action"
        )

    if request.method == "POST":
        message.delete()
        return redirect("room", pk=message.room.id)

    return render(request, "delete.html", context)
