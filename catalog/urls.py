from django.urls import path, re_path

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
        r"^book/(?P<pk>[-\w]+)/renew/$",
        views.renew_book_librarian,
        name="renew-book-librarian",
    ),
]

urlpatterns += [
    path("author/create/", views.AuthorCreate.as_view(), name="author-create"),
    path(
        "author/<int:pk>/update/",
        views.AuthorUpdate.as_view(),
        name="author-update",
    ),
    path(
        "author/<int:pk>/delete/",
        views.AuthorDelete.as_view(),
        name="author-delete",
    ),
]
