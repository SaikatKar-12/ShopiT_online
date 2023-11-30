from django.shortcuts import render, redirect

from items.models import Category, Item

from .forms import SignupForm

from django.contrib.auth import logout

from django.urls import reverse
# Create your views here.
def index(request):
    item = Item.objects.filter(is_sold=False)[0:6]
    categories = Category.objects.all()
    return render(request,'core/index.html',{
        'categories': categories,
        'items':item,
    })
def contact(request):
    return render(request, 'core/contact.html')
def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect('/login/')
    else:
        form = SignupForm()
    return render(request,'core/signup.html',{
        'form': form
    })

def logout_view(request):
    logout(request)
    #return redirect(reverse('/login/'))  # Replace 'home' with the name of your homepage URL pattern
    return redirect('/login/')
