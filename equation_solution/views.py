from django.shortcuts import render
from .forms import Equation
from .services import solution

def equation_solution(request):
    submitbutton = request.POST.get("submit")
    a, b, c, x1, x2 = '', '', '', '', ''

    form = Equation(request.POST or None)
    if form.is_valid():
        a = form.cleaned_data.get("a")
        b = form.cleaned_data.get("b")
        c = form.cleaned_data.get("c")
        x1, x2 = solution(a, b, c)

    context = {'form': form, 'a': a, 'b': b, 'c': c, 'x1': x1, 'x2': x2,
               'submitbutton': submitbutton}

    return render(request, 'equation_solution/solution.html', context)