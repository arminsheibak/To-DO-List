from django.urls import path
from django.contrib.auth.views import LogoutView
from . import views


urlpatterns = [
    path("", views.TaskList.as_view(), name="task_list"),
    path("task/<int:pk>/", views.TaskDetail.as_view(), name="task_detail"),
    path("task=create/", views.TaskCreate.as_view(), name="task_create"),
    path("task-update/<int:pk>/", views.TaskUpdate.as_view(), name="task_update"),
    path("task-delete/<int:pk>/", views.TaskDelete.as_view(), name="task_delete"),
    path("accounts/login/", views.LoginView.as_view(), name="login"),
    path("accounts/logout/", LogoutView.as_view(next_page='login'), name="logout"),
    path("accounts/signup/", views.SignUpView.as_view(), name="signup"),

]

