from django.urls import path
from ask import views

urlpatterns = [
    path('register/',views.register,name='register'),
    path('login/',views.login_user,name='login'),
    path('home/',views.home,name='home'),
    path('detail/<int:question_id>/',views.detail,name='detail'),
    path('addcomment/<int:answer_id>/',views.comment,name='comment'),
    path('postQuery',views.post_query,name="postQuery")
]