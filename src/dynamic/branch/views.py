from django.shortcuts import render, HttpResponse

from dynamic.branch.models import Branch


def branch(request):
    branchs = Branch.objects.all()

    ctx = {'branchs': branchs}
    return render(request, 'branch.html', ctx)
