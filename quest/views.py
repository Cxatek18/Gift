from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib import messages

from .service.enum_question import EnumQuestion
from .service.enum_response import EnumResponse
from .service.enum_hint import EnumHint

from .forms import AnswerForm


class FirstQuestions(View):

    def get(self, request):
        form = AnswerForm()
        context = {
            "question": EnumQuestion.FIRST_QUESTION.value,
            "form": form,
            "title": "Первый вопрос"
        }
        return render(request, "first.html", context)
    
    def post(self, request, *args, **kwargs):
        form = AnswerForm(request.POST)
        if form.is_valid():
            response = EnumResponse.FIRST_ANSWER.value.lower()
            response_user = form.cleaned_data["text"].lower()
            if response == response_user:
                context = {
                    "hint": EnumHint.FIRST_HINT.value
                }
                return render(request, "hints/first_h.html", context)
            else:
                messages.error(request, "Не правильный ответ, пробуем по новой")
                return redirect("first")
            

class SecondQuestions(View):

    def get(self, request):
        form = AnswerForm()
        context = {
            "question": EnumQuestion.SECOND_QUESTION.value,
            "form": form,
            "title": "Второй вопрос"
        }
        return render(request, "second.html", context)
    
    def post(self, request, *args, **kwargs):
        form = AnswerForm(request.POST)
        if form.is_valid():
            response = EnumResponse.SECOND_ANSWER.value.lower()
            response_user = form.cleaned_data["text"].lower()
            if response == response_user:
                context = {
                    "hint": EnumHint.SECOND_HINT.value
                }
                return render(request, "hints/second_h.html", context)
            else:
                messages.error(request, "Не правильный ответ, пробуем по новой")
                return redirect("second")
            

class ThirdQuestions(View):

    def get(self, request):
        form = AnswerForm()
        context = {
            "question": EnumQuestion.THIRD_QUESTION.value,
            "form": form,
            "title": "Третий вопрос"
        }
        return render(request, "third.html", context)
    
    def post(self, request, *args, **kwargs):
        form = AnswerForm(request.POST)
        if form.is_valid():
            response = EnumResponse.THIRD_ANSWER.value.lower()
            response_user = form.cleaned_data["text"].lower()
            if response == response_user:
                context = {
                    "hint": EnumHint.THIRD_HINT.value
                }
                return render(request, "hints/third_h.html", context)
            else:
                messages.error(request, "Не правильный ответ, пробуем по новой")
                return redirect("third")
            

class FourthQuestions(View):

    def get(self, request):
        form = AnswerForm()
        context = {
            "question": EnumQuestion.FOURTH_QUESTION.value,
            "form": form,
            "title": "Четвёртый вопрос"
        }
        return render(request, "fourth.html", context)
    
    def post(self, request, *args, **kwargs):
        form = AnswerForm(request.POST)
        if form.is_valid():
            response = EnumResponse.FOURTH_ANSWER.value.lower()
            response_user = form.cleaned_data["text"].lower()
            if response == response_user:
                context = {
                    "hint": EnumHint.FOURTH_HINT.value
                }
                return render(request, "hints/fourth_h.html", context)
            else:
                messages.error(request, "Не правильный ответ, пробуем по новой")
                return redirect("fourth")
            

class FifthQuestions(View):

    def get(self, request):
        form = AnswerForm()
        context = {
            "question": EnumQuestion.FIFTH_QUESTION.value,
            "form": form,
            "title": "Пятый вопрос"
        }
        return render(request, "fifth.html", context)
    
    def post(self, request, *args, **kwargs):
        form = AnswerForm(request.POST)
        if form.is_valid():
            response = EnumResponse.FIFTH_ANSWER.value.lower()
            response_user = form.cleaned_data["text"].lower()
            if response == response_user:
                context = {
                    "hint": EnumHint.FIFTH_HINT.value
                }
                return render(request, "hints/fifth_h.html", context)
            else:
                messages.error(request, "Не правильный ответ, пробуем по новой")
                return redirect("fifth")

        
class SixthQuestions(View):

    def get(self, request):
        form = AnswerForm()
        context = {
            "question": EnumQuestion.SIXTH_QUESTION.value,
            "form": form,
            "title": "Шестой вопрос"
        }
        return render(request, "sixth.html", context)
    
    def post(self, request, *args, **kwargs):
        form = AnswerForm(request.POST)
        if form.is_valid():
            response = EnumResponse.SIXTH_ANSWER.value.lower()
            response_user = form.cleaned_data["text"].lower()
            if response == response_user:
                context = {
                    "hint": EnumHint.SIXTH_HINT.value
                }
                return render(request, "hints/sixth_h.html", context)
            else:
                messages.error(request, "Не правильный ответ, пробуем по новой")
                return redirect("sixth")

        
class SeventhQuestions(View):

    def get(self, request):
        form = AnswerForm()
        context = {
            "question": EnumQuestion.SEVENTH_QUESTION.value,
            "form": form,
            "title": "Седьмой вопрос"
        }
        return render(request, "seventh.html", context)
    
    def post(self, request, *args, **kwargs):
        form = AnswerForm(request.POST)
        if form.is_valid():
            response = EnumResponse.SEVENTH_ANSWER.value.lower()
            response_user = form.cleaned_data["text"].lower()
            if response == response_user:
                context = {
                    "hint": EnumHint.SEVENTH_HINT.value
                }
                return render(request, "hints/seventh_h.html", context)
            else:
                messages.error(request, "Не правильный ответ, пробуем по новой")
                return redirect("seventh")
            

class EighthQuestions(View):

    def get(self, request):
        form = AnswerForm()
        context = {
            "question": EnumQuestion.EIGHTH_QUESTION.value,
            "form": form,
            "title": "Восьмой вопрос"
        }
        return render(request, "eighth.html", context)
    
    def post(self, request, *args, **kwargs):
        form = AnswerForm(request.POST)
        if form.is_valid():
            response = EnumResponse.EIGHTH_ANSWER.value.lower()
            response_user = form.cleaned_data["text"].lower()
            if response == response_user:
                context = {
                    "hint": EnumHint.EIGHTH_HINT.value
                }
                return render(request, "hints/eighth_h.html", context)
            else:
                messages.error(request, "Не правильный ответ, пробуем по новой")
                return redirect("eighth")
            

class NinthQuestions(View):

    def get(self, request):
        form = AnswerForm()
        context = {
            "question": EnumQuestion.NINTH_QUESTION.value,
            "form": form,
            "title": "Девятый вопрос"
        }
        return render(request, "ninth.html", context)
    
    def post(self, request, *args, **kwargs):
        form = AnswerForm(request.POST)
        if form.is_valid():
            response = EnumResponse.NINTH_ANSWER.value.lower()
            response_user = form.cleaned_data["text"].lower()
            if response == response_user:
                context = {
                    "hint": EnumHint.NINTH_HINT.value
                }
                return render(request, "hints/ninth_h.html", context)
            else:
                messages.error(request, "Не правильный ответ, пробуем по новой")
                return redirect("ninth")
            
class TenthQuestions(View):

    def get(self, request):
        form = AnswerForm()
        context = {
            "question": EnumQuestion.TENTH_QUESTION.value,
            "form": form,
            "title": "Десятый вопрос"
        }
        return render(request, "tenth.html", context)
    
    def post(self, request, *args, **kwargs):
        form = AnswerForm(request.POST)
        if form.is_valid():
            response = EnumResponse.TENTH_ANSWER.value.lower()
            response_user = form.cleaned_data["text"].lower()
            if response == response_user:
                context = {
                    "hint": EnumHint.TENTH_HINT.value
                }
                return render(request, "hints/tenth_h.html", context)
            else:
                messages.error(request, "Не правильный ответ, пробуем по новой")
                return redirect("tenth")
            

class WishesView(View):

    def get(self, request):
        context = {
            "title": "Заключение"
        }
        return render(request, "wishes.html", context)
