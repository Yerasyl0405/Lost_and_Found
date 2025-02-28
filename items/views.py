from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, get_object_or_404, redirect
from .models import LostItem, FoundItem
from .forms import LostItemForm, FoundItemForm


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

def add_lost_item(request):
    if request.method == "POST":
        form = LostItemForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("lost_items_list")
    else:
        form = LostItemForm()
    return render(request, "items/item_form.html", {"form": form})

def add_found_item(request):
    if request.method == "POST":
        form = FoundItemForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("found_items_list")
    else:
        form = FoundItemForm()
    return render(request, "items/item_form.html", {"form": form})


@user_passes_test(is_staff_user)
def admin_items_list(request):
    lost_items = LostItem.objects.all()
    found_items = FoundItem.objects.all()
    return render(request, "items/admin_items_list.html", {"lost_items": lost_items, "found_items": found_items})
