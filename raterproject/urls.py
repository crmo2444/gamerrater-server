from django.contrib import admin
from django.conf.urls import include
from django.urls import path
from gamerraterapi.views import register_user, login_user
from rest_framework import routers
from gamerraterapi.views.category import CategoryView
from gamerraterapi.views.game import GameView
from gamerraterapi.views.gamecategory import GameCategoryView
from gamerraterapi.views.gamereview import GameReviewView

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'games', GameView, 'game')
router.register(r'categories', CategoryView, 'category')
router.register(r'gamecategories', GameCategoryView, 'gamecategories')
router.register(r'gamereviews', GameReviewView, 'gamereview')

urlpatterns = [
    # Requests to http://localhost:8000/register will be routed to the register_user function
    path('register', register_user),
    # Requests to http://localhost:8000/login will be routed to the login_user function
    path('login', login_user),
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]