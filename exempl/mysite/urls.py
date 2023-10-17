from django.urls import path

from mysite.views import *

urlpatterns = [
    path('', PostView.as_view(), name='home'),
    path('<int:pk>/', PostDetail.as_view()),
    path('review/<int:pk>/', AddComments.as_view(), name='add_comment'),
    path('<int:pk>/add_like/', AddLike.as_view(), name='add_like'),
    path('<int:pk>/del_like/', DelLike.as_view(), name='del_like'),
    path('cats/<int:cat_id>/', categories),
]