#from .views import PostList, PostDetail, UserDetail, UserList
from rest_framework.routers import SimpleRouter
from .views import PostViewSet, UserViewSet
from django.urls import path


"""urlpatterns = [
    path('<int:pk>/', PostDetail.as_view()),
    path('', PostList.as_view()),
    path('users/', UserList.as_view()),
    path('users/<int:pk>/', UserDetail.as_view()),
   
]"""

router = SimpleRouter()
router.register('users', UserViewSet, basename='users')
router.register('', PostViewSet, basename='posts')

urlpatterns = router.urls