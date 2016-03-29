from django.shortcuts import render

from django.shortcuts import render, get_object_or_404


def me(request):
	return render(request, 'home/me.html', {})


# Create your views here.
