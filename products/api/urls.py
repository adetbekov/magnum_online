from django.urls import path
from .views import ProductsView, CategoriesView, SubCategoriesView, get_post 

app_name = "products"

urlpatterns = [
	# url(r'^messages/(?P<pk>[0-9]+)/$', MessageListAPIView.as_view({'get': 'retrieve'}), name="messages"),
	path('subcategories', SubCategoriesView.as_view()),
	path('categories', CategoriesView.as_view()),
	path('all', ProductsView.as_view()),
	path('<int:pk>/', get_post)
]