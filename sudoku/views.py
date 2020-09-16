from django.shortcuts import render, redirect
from sudoku.solver import Solver


def index(request):
    if request.GET:
        valid = True
        values = dict()

        for l in "012345678":
            for n in "012345678":
                if l + n not in request.GET:
                    valid = False
                else:
                    if len(request.GET[l + n]) > 1:
                        valid = False
                    elif len(request.GET[l + n]) == 1:
                        if request.GET[l + n] not in "012345678":
                            valid = False
                        else:
                            values[l + n] = request.GET[l + n]

        if valid:
            values = Solver(values).values
            if values:
                return render(request, 'index.html', {'values': values})
        return redirect('index')
    else:
        return render(request, 'index.html')
