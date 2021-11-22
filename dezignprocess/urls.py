from django.urls import path
from dezignprocess import views


urlpatterns = [
    path("search/", views.search, name="search"),
    path("first/", views.StepList.as_view(), name="first"),
    path("next/", views.StepNext.as_view(), name="next"),
    path("<slug:slug>/", views.StepDetail.as_view(), name="step_detail"),
]
