from django.urls import path
from . import views

urlpatterns = [
    path('listings/', views.ListingList.as_view(), name='listing-list'),
    path('listings/<int:pk>/', views.ListingDetail.as_view(), name='listing-detail'),
    path('profile/', views.UserProfileView.as_view(), name='user-profile'),
    path('like/<int:pk>/', views.LikeView.as_view(), name='like-listing'),
    path('unlike/<int:pk>/', views.UnlikeView.as_view(), name='unlike-listing'),
    # Другие маршруты...
]
