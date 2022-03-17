from django.urls import path
from .views import CategoryCreateListView, CategoryRetrieveView,PostCreateListView,PostRetrieveView, \
    PostList,PostDestroyView,CategoryDestroyView

urlpatterns = [
    path('category-list-create/', CategoryCreateListView.as_view()),
    path('category-retrive-update/<int:pk>', CategoryRetrieveView.as_view()),
    path('category-destroy/<int:pk>', CategoryDestroyView.as_view()),
    path('post-list/', PostList.as_view()),
    path('post-list-create/', PostCreateListView.as_view()),
    path('post-retrive-update/<int:pk>', PostRetrieveView.as_view()),
    path('post-destroy/<int:pk>', PostDestroyView.as_view())
]
