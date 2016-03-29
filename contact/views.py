from django.shortcuts import render

from .forms import PostForm

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            
    else:
        form = PostForm()
    return render(request, 'contact/contact.html', {'form': form})




