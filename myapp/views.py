from django.http import HttpResponse
from django.shortcuts import render
from .forms import UserFormFields
from .forms import UserFormData

def simple_view(request):
    data = {
        "header": "Привет, Django!",
        "message": "Это страница для демонстрации передачи простых данных"
    }
    return render(request, "simple.html", context=data)

def complex_view(request):
    data = {
        "header": "lанные пользователя",
        "langs": ["питон", "java", "C#", "javascript"],
        "user": {"name": "Tom", "age": 23},
        "address": ("Пушкина", 23, 45) # кортеж
    }
    return render(request, "complex.html", context=data)

def static_files_view(request):
    return render(request, "static.html")

# myapp/views.py
def index_view(request):
    return render(request, "index.html")

def about_view(request):
    return render(request, "about.html")

def contacts_view(request):
    return render(request, "contacts.html")


def form_html_view(request):
    if request.method == "POST":
        familia = request.POST.get("familia", "Не указана")
        imy = request.POST.get("imy", "Не указано")
        otchestvo = request.POST.get("otchestvo", "Не указано")
        age = request.POST.get("age", "Не указан")
        address = request.POST.get("address", "Не указан")
        group = request.POST.get("group", "Не указана")
        subjects = request.POST.getlist("subjects")

        return HttpResponse(f"""
            <h2>Полученные данные:</h2>
            <p><strong>Фамилия:</strong> {familia}</p>
            <p><strong>Имя:</strong> {imy}</p>
            <p><strong>Отчество:</strong> {otchestvo}</p>
            <p><strong>Возраст:</strong> {age}</p>
            <p><strong>Адрес:</strong> {address}</p>
            <p><strong>Группа:</strong> {group}</p>
            <p><strong>Список предметов:</strong> {', '.join(subjects) if subjects else 'не выбраны'}</p>
        """)
    else:
        return render(request, "form_html.html")


def fields_view(request):
    form = UserFormFields()
    return render(request, "fields.html", {"form": form})




def userdata_view(request):
    if request.method == 'POST':
        form = UserFormData(request.POST)

        if form.is_valid():
            fio = form.cleaned_data['fio']
            age = form.cleaned_data['age']

            return HttpResponse(f"<h2>Привет, {fio}!</h2><p>данные успешно отправлены</p>")
    else:
        form = UserFormData()

    return render(request, 'userdata.html', {'form': form})

def user_profile(request, username):
    output = f"<h1>Профиль пользователя</h1><p>Имя пользователя: {username}</p>"
    return HttpResponse(output)

def archive(request, year, month):
    output = f"<h1>Архив</h1><p>Год: {year}</p><p>Месяц: {month}</p>"
    return HttpResponse(output)

def index(request):
    return HttpResponse("<h1>Главная страница</h1><p>Перейдите на /user/ваше_имя/ или /archive/2023/04/</p>")


def search(request):
    search_query = request.GET.get('q', 'Ничего не найдено')
    category = request.GET.get('category', 'Все категории')

    output = f"<h1>Результаты поиска</h1>"
    output += f"<p>Вы искали: '{search_query}'</p>"
    output += f"<p>В категории: '{category}'</p>"

    return HttpResponse(output)