"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from core.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('categories/', CategoryView.as_view(), name='categories'),
    path('categories/<int:category_id>', CategoryView.as_view(), name='category'),
    path('categories_name/<str:category_name>', CategoryNameView.as_view(), name='categories_name'),
    path('authors/', AuthorView.as_view(), name='authors'),
    path('authors/<int:author_id>', AuthorView.as_view(), name='author'),
    path('authors_last_name/<str:author_last_name>', AuthorLastnameView.as_view(), name='author_last_name'),
    path('partners/', PartnerView.as_view(), name='partners'),
    path('partners/<int:partner_id>', PartnerView.as_view(), name='partner'),
    path('partners_dni/<str:partner_dni>', PartnerDniView.as_view(), name='partner_dni'),
    path('books/', BookView.as_view(), name='books'),
    path('books/<int:book_id>', BookView.as_view(), name='book'),
    path('books_author/<int:author_id>', BookAuthorView.as_view(), name='book_author'),
    path('bookloans/', BookLoanView.as_view(), name='bookloans'),
    path('bookloans/<int:bookloan_id>', BookLoanView.as_view(), name='bookloan'),
    path('bookloans_status/<str:status>', BookLoanStatusView.as_view(), name='bookloan_status'),
    path('bookloans_partner/<str:partner_dni>', BookLoanPartnerView.as_view(), name='bookloan_partner'),
]


