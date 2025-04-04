from django.contrib.auth.decorators import user_passes_test, login_required
from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, get_object_or_404, redirect
from .forms import LostItemForm, FoundItemForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.shortcuts import render, redirect
from django.contrib import messages

from .models import LostItem, FoundItem


def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Account created! You can now log in.")
            return redirect("login")
    else:
        form = UserCreationForm()
    return render(request, "register.html", {"form": form})

def user_login(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                return redirect("home")
        messages.error(request, "Invalid username or password")
    else:
        form = AuthenticationForm()
    return render(request, "login.html", {"form": form})

# User Logout
def user_logout(request):
    logout(request)
    return redirect("login")

@login_required
def profile(request):
    lost_items = LostItem.objects.filter(user=request.user)
    found_items = FoundItem.objects.filter(user=request.user)

    context = {
        "user": request.user,
        "lost_items": lost_items,
        "found_items": found_items,
    }
    return render(request, "profile.html", context)

def index(request):
    return render(request,  "base.html" )

def is_staff_user(user):
    return user.is_staff


@user_passes_test(is_staff_user)
def delete_lost_item(request, item_id):
    item = get_object_or_404(LostItem, id=item_id)
    item.delete()
    return redirect("admin_items_list")

@user_passes_test(is_staff_user)
def delete_found_item(request, item_id):
    item = get_object_or_404(FoundItem, id=item_id)
    item.delete()
    return redirect("admin_items_list")

def lost_items_list(request):
    items = LostItem.objects.all()
    return render(request, "items/lost_items_list.html", {"items": items})

def found_items_list(request):
    items = FoundItem.objects.all()
    return render(request, "items/found_items_list.html", {"items": items})

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import LostItemForm, FoundItemForm

@login_required
def add_lost_item(request):
    if request.method == "POST":
        form = LostItemForm(request.POST, request.FILES)
        if form.is_valid():
            lost_item = form.save(commit=False)
            lost_item.user = request.user
            lost_item.save()  # Now save
            return redirect("lost_items_list")
    else:
        form = LostItemForm()
    return render(request, "items/item_form.html", {"form": form})

@login_required
def add_found_item(request):
    if request.method == "POST":
        form = FoundItemForm(request.POST, request.FILES)
        if form.is_valid():
            found_item = form.save(commit=False)
            found_item.user = request.user
            found_item.save()
            return redirect("found_items_list")
    else:
        form = FoundItemForm()
    return render(request, "items/item_form.html", {"form": form})


@user_passes_test(is_staff_user)
def admin_items_list(request):
    lost_items = LostItem.objects.all()
    found_items = FoundItem.objects.all()
    return render(request, "items/admin_items_list.html", {"lost_items": lost_items, "found_items": found_items})


@login_required
def mark_lost_recovered(request, item_id):
    item = get_object_or_404(LostItem, id=item_id)

    if request.user == item.user or request.user.is_superuser:
        item.is_recovered = True
        item.status = "recovered"
        item.save()
        messages.success(request, "Lost item marked as recovered.")
    else:
        messages.error(request, "You are not allowed to modify this item.")

    return redirect("profile")

@login_required
def mark_found_claimed(request, item_id):
    item = get_object_or_404(FoundItem, id=item_id)

    if request.user == item.user or request.user.is_superuser:
        item.is_claimed = True
        item.status = "claimed"
        item.save()
        messages.success(request, "Found item marked as claimed.")
    else:
        messages.error(request, "You are not allowed to modify this item.")

    return redirect("profile")
