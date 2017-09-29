from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect, Http404

from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView

from .forms import UserCreateForm, RefugeForm, PostForm, NeedForm, UserForm
from .serializers import RefugeCreateSerializer, PostCreateSerializer
from .models import Refuge, Need, Post


def index(request):

    refuges_objects = Refuge.objects.all()
    refuges = []

    for refuge_object in refuges_objects:
        needs = Need.objects.filter(post=refuge_object.post)
        refuges.append({'refuge': refuge_object, 'needs': needs})

    return render(request, 'inventories/home.html', {'refuges': refuges})


def sign_in(request):

    if request.user.is_authenticated():
        return redirect('/')

    if request.method == 'POST':
        form = UserForm(request.POST or None)

        if form.is_valid():
            email = request.POST['email']
            password = request.POST['password']

            user = authenticate(username=email, password=password)

            if user is not None:
                login(request, user)
                return redirect('/')
            else:
                message = 'Correo o contraseña inválidas'
                return render(request, 'inventories/sign_in.html', {'form': form, 'message': message})
        else:
            return render(request, 'inventories/sign_in.html', {'form': form})

    form = UserForm(None)
    return render(request, 'inventories/sign_in.html', {'form': form})


def sign_out(request):
    if not request.user.is_authenticated():
        raise Http404

    logout(request)
    return redirect('/')


def sign_up(request):

    if request.user.is_authenticated():
        return redirect('/')

    if request.method == 'POST':
        form = UserCreateForm(request.POST or None)

        if form.is_valid():
            instance = form.save(commit=False)
            password = form.cleaned_data['password']
            email = form.cleaned_data['email']
            instance.set_password(password)
            instance.username = email
            instance.is_active = True
            instance.save()
            login(request, instance)

            return redirect('/registrar/')
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

    forms = [refuge_form, post_form]

    return render(request, 'inventories/create_refuge.html', {'forms': forms, 'need_form': need_form})


class CreateRefugeAPIView(CreateAPIView):
    queryset = Refuge.objects.all()
    serializer_class = RefugeCreateSerializer


class CreatePostAPIView(CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostCreateSerializer