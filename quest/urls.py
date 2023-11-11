from django.urls import path

from .views import (
    FirstQuestions,
    SecondQuestions,
    ThirdQuestions,
    FourthQuestions,
    FifthQuestions,
    SixthQuestions,
    SeventhQuestions,
    EighthQuestions,
    NinthQuestions,
    TenthQuestions,
    WishesView
)


urlpatterns = [
    path("", FirstQuestions.as_view(), name="first"),
    path("second/", SecondQuestions.as_view(), name="second"),
    path("third/", ThirdQuestions.as_view(), name="third"),
    path("fourth/", FourthQuestions.as_view(), name="fourth"),
    path("fifth/", FifthQuestions.as_view(), name="fifth"),
    path("sixth/", SixthQuestions.as_view(), name="sixth"),
    path("seventh/", SeventhQuestions.as_view(), name="seventh"),
    path("eighth/", EighthQuestions.as_view(), name="eighth"),
    path("ninth/", NinthQuestions.as_view(), name="ninth"),
    path("tenth/", TenthQuestions.as_view(), name="tenth"),
    path("final/", WishesView.as_view(), name="final"),
]