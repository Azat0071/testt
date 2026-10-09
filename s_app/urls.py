from django.urls import path
from s_app.views import TaskList, TaskCreate, ContactDetail, ContactDelete, ContactUpdate, ContactPatch

urlpatterns = [
    path('task/', TaskList.as_view()),
    path('task/create/', TaskCreate.as_view()),
    path('task/<int:pk>/', ContactDetail.as_view()),
    path('task/<int:pk>/delete/', ContactDelete.as_view()),
    path('task/<int:pk>/update/', ContactUpdate.as_view()),
    path('task/<int:pk>/patch', ContactPatch.as_view()),
]