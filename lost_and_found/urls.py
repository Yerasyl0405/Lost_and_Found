"""
URL configuration for lost_and_found project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from items import views
from items.view_api import DeleteFoundItemView, DeleteLostItemView, MarkFoundClaimedAPI, FoundItemListAPI, \
    MarkLostRecoveredAPI, LostItemListView, LostItemCreateAPI
from items.views import mark_lost_recovered, mark_found_claimed, FoundItemCreateAPI
from lost_and_found import settings

from django.contrib import admin
from django.urls import path
from items import views  # Ensure views.py is imported

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.index, name="home"),
    path("admin-items/", views.admin_items_list, name="admin_items_list"),
    path("admin-items/delete-lost/<int:item_id>/", views.delete_lost_item, name="delete_lost_item"),
    path("admin-items/delete-found/<int:item_id>/", views.delete_found_item, name="delete_found_item"),
    path("lost/", views.lost_items_list, name="lost_items_list"),
    path('found/', views.found_items_list, name = "found_items_list"),  # or FoundItemListAPI.as_view()
    path("lost/add/", views.add_lost_item, name="add_lost_item"),
    path("found/add/", views.add_found_item, name="add_found_item"),
    path("register/", views.register, name="register"),
    path("login/", views.user_login, name="login"),
    path("logout/", views.user_logout, name="logout"),
    path("profile/", views.profile, name="profile"),
    path("mark_lost_recovered/<int:item_id>/", mark_lost_recovered, name="mark_lost_recovered"),
    path("mark_found_claimed/<int:item_id>/", mark_found_claimed, name="mark_found_claimed"),
    path('api/lost-items/', LostItemListView.as_view(), name='api_lost_items'),
    path('api/lost-items/create/', LostItemCreateAPI.as_view(), name='create_lost_item'),
    path('api/lost-items/<int:item_id>/recover/', MarkLostRecoveredAPI.as_view(), name='recover_lost_item'),
    path('api/found-items/', FoundItemListAPI.as_view(), name='api_found_items'),
    path('api/found-items/create/', FoundItemCreateAPI.as_view(), name='create_found_item'),
    path('api/found-items/<int:item_id>/claim/', MarkFoundClaimedAPI.as_view(), name='claim_found_item'),
    path('lost-items/<int:item_id>/delete/', DeleteLostItemView.as_view(), name='api_delete_lost_item'),
    path('found-items/<int:item_id>/delete/', DeleteFoundItemView.as_view(), name='api_delete_found_item'),
    path('silk/', include('silk.urls', namespace='silk'))
]

from items.views import FoundItemCreateAPI


