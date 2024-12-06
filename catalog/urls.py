from django.urls import re_path

from . import views

urlpatterns = [
    re_path(r"^$", views.index, name="index"),
    re_path(r"^books/$", views.BookListView.as_view(), name="books"),
    re_path(
        r"^book/(?P<pk>\d+)$",
        views.BookDetailView.as_view(),
        name="book-detail",
    ),
    re_path(r"^authors/$", views.AuthorListView.as_view(), name="authors"),
    re_path(
        r"^author/(?P<pk>\d+)$",
        views.AuthorDetailView.as_view(),
        name="author-detail",
    ),
]

urlpatterns += [
    re_path(
        r"^mybooks/$",
        views.LoanedBooksByUserListView.as_view(),
        name="my-borrowed",
    ),
]

urlpatterns += [
    re_path(
        "book/<uuid:pk>/renew/",
        views.renew_book_librarian,
        name="renew-book-librarian",
    ),
]
