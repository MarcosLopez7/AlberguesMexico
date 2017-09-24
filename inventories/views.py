from django.shortcuts import render, redirect

from .forms import UserCreateForm, RefugeForm, PostForm, NeedForm


def index(request):
    return render(request, 'inventories/home.html')


def sign_up(request):

    if request.user.is_authenticated():
        return redirect('/')

    if request.method == 'POST':
        form = UserCreateForm(request.POST or None)

        if form.is_valid():
            instance = form.save(commit=False)
            password = form.cleaned_data['password']
            instance.set_password(password)
            instance.username = form.cleaned_data['email']
            instance.is_active = True
            instance.save()

            return redirect('/shop/success-sign-up')
        else:
            return render(request, 'inventories/sign_up.html', {'form': form})

    form = UserCreateForm(None)

    return render(request, 'inventories/sign_up.html', {'form': form})


def create_refuge(request):

    #if not request.user.is_authenticated():
    #    return redirect('/')

    refuge_form = RefugeForm(None)
    post_form = PostForm(None)
    need_form = NeedForm(None)

    forms = [refuge_form, post_form, need_form]

    return render(request, 'inventories/create_refuge.html', {'forms': forms})
