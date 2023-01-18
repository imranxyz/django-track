from django import forms 
from . import models

# class PizzaForm(forms.Form):
    # CHOICES = (
    #     ('Small', 'Small'),
    #     ('Medium', 'Medium'),
    #     ('Large', 'Large')
    # )
    # topping1 = forms.CharField(label='Topping 1', max_length=100)
    # topping2 = forms.CharField(label='Topping 2', max_length=100)
    # size = forms.ChoiceField(label='Size', choices=CHOICES)

class PizzaForm(forms.ModelForm):
    # size = forms.ModelChoiceField(queryset=models.Size.objects, empty_label=None, widget=forms.RadioSelect)
    # image = forms.ImageField() 

    class Meta:
        model = models.Pizza
        fields = ['topping1', 'topping2', 'size']
        labels = {
            "topping1": "Topping 1",
            "topping2": "Topping 2",
        }


class MultiplePizzaForm(forms.Form):
    number = forms.IntegerField(min_value=2, max_value=6)
    