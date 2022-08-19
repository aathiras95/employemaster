from django .urls import path
from emastersystem import views
urlpatterns=[
    path("",views.IndexView.as_view(),name='index'),
    path('account/signup',views.SignUpView.as_view(),name='signup'),
    path('account/signin', views.LoginView.as_view(), name='login'),
    path('account/signout',views.SignOut,name='signout'),
    path('users/profiles',views.ViewMyProfileView.as_view(),name='viewprofile'),
    path('bio', views.UserProfileAdd.as_view(), name='addpro'),
    path('user/profile/change/ <str:user_id>', views.UserUpdateView.as_view(), name='changeprofile'),
    path('all',views.EmployeeListView.as_view(),name='emp_list'),

    ]