from django.shortcuts import render
from . import forms, models
from django.forms import formset_factory

def home(request):
    return render(request, 'pizza/home.html')


def order(request):
    pizzaform = forms.PizzaForm()
    MultiplePizzaForm = forms.MultiplePizzaForm()
    
    if request.method == 'POST':
        pizzaform = forms.PizzaForm(request.POST, request.FILES)
        if pizzaform.is_valid():
            topping1 = pizzaform.cleaned_data['topping1']
            topping2 = pizzaform.cleaned_data['topping2']
            size = pizzaform.cleaned_data['size']
            note = f'Thanks for ordering! Your {size} {topping1} and {topping2} pizza is on its way'
            crearted_pizza = pizzaform.save()
            crearted_pizza_pk = crearted_pizza.id
        else:
            crearted_pizza_pk = None
            note = 'Pizza order has failed. Try again'
            
        return render(request, 'pizza/order.html', context={
                'pizzaform': pizzaform,
                'note': note,
                'multiple_form': MultiplePizzaForm,
                'created_pizza_pk': crearted_pizza_pk,
            })

    return render(request, 'pizza/order.html', context={'pizzaform': pizzaform, 'multiple_form': MultiplePizzaForm})

def edit_order(request, pk):
    pizza = models.Pizza.objects.get(pk=pk)
    form = forms.PizzaForm(instance=pizza)
    if request.method == 'POST':
        filled_form = forms.PizzaForm(request.POST, instance=pizza)
        if filled_form.is_valid():
            filled_form.save()
            form = filled_form
            note = 'Order has been Updated!'
            return render(request=request, template_name='pizza/edit_order.html', context={
                'pizza': pizza,
                'pizzaform': form,
                'note': note,
            })

    return render(request=request, template_name='pizza/edit_order.html', context={
        'pizza': pizza,
        'pizzaform': form,
    })

def pizzas(request):
    number_of_pizzas = 2
    filled_multiple_pizza_form = forms.MultiplePizzaForm(request.GET)

    if filled_multiple_pizza_form.is_valid():
        number_of_pizzas = filled_multiple_pizza_form.cleaned_data['number']
    
    PizzaFormSet = formset_factory(forms.PizzaForm, extra=number_of_pizzas)
    formset = PizzaFormSet()

    if request.method == 'POST':
        filled_formset = PizzaFormSet(request.POST)
        if filled_formset.is_valid():
            for form in filled_formset:
                print(f"{form.cleaned_data['topping1']}")
            note = 'Pizzas have been ordered'
        else:
            note = 'Order was not created. Please try again!'
        
        return render(request, 'pizza/pizzas.html', context={
            'note': note,
            'formset': formset,
        })
    else:
        return render(request, 'pizza/pizzas.html', context={
            'formset': formset,
        })
