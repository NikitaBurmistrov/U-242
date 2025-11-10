import datetime
from django import forms


class UserFormFields(forms.Form):

    name = forms.CharField(min_length=2, max_length=20, label="Имя")

    age = forms.IntegerField(min_value=1, max_value=100, label="В"
                                                               "озраст")

    is_student = forms.BooleanField(required=False, label="Является студентом")


    email = forms.EmailField(label="Электронная почта")


    course = forms.ChoiceField(choices=((1, "Python"), (2, "Java"), (3, "C#")), label="Курс")



    hobbies = forms.MultipleChoiceField(
        choices=(("sport", "Спорт"), ("music", "Музыка"), ("travel", "Путешествия")),
        widget=forms.CheckboxSelectMultiple,
        label="Хобби"
    )

    birth_date = forms.DateField(widget=forms.SelectDateWidget, label="Дата рождения")





class UserFormData(forms.Form):
    fio = forms.CharField(
        label="ФИО",
        min_length=5,
        max_length=100,
        help_text="Введите полные фамилию, имя и отчество"
    )

    age = forms.IntegerField(
        label="Возраст",
        min_value=16,
        max_value=100
    )



    group = forms.ChoiceField(
        label="Номер группы",
        choices=(("У-242", "У-242"), ("У-243", "У-243"), ("У-244", "У-244"))
    )
    birth_date = forms.DateField(
        label="Дата рождения",
        widget=forms.SelectDateWidget(years=range(1980, datetime.date.today().year - 15)),
        help_text="Укажите вашу дату рождения"
    )

    language = forms.ChoiceField(
        label="Любимый язык программирования",
        choices=(("python", "Python"), ("java", "Java"), ("csharp", "C#"), ("js", "JavaScript")),
        widget=forms.RadioSelect
    )

    email = forms.EmailField(
        label="E-mail",
        required=False
    )