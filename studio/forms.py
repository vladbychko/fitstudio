from django import forms

class BookingForm(forms.Form):
    name = forms.CharField(label="Ім’я", max_length=100)
    phone = forms.CharField(label="Телефон", max_length=30)
    goal = forms.ChoiceField(
        label="Ціль",
        choices=[
            ('lose_weight', "Похудіння"),
            ('mass', "Маса"),
            ('health', "Здоров’я"),
        ]
    )
    message = forms.CharField(
        label="Коментар",
        widget=forms.Textarea(attrs={'rows': 3}),
        required=False,
    )
