from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.db.utils import IntegrityError
from django.contrib.auth.models import User, Group
from rest_framework import viewsets, permissions

from userauth.serializers import UserSerializer, GroupSerializer

def huef():
    def start(request):
        if request.user.is_authenticated:
            return render(request, 'index.html')
        else:
            return redirect('login')

    def login(request):
        if request.method == "POST":
            user = authenticate(username=request.POST['username'], password=request.POST['password'])
            if user is not None:
                login(request, user)
                messages.info(request, 'Welcome =)')
                return redirect('start')
            else:
                messages.info(request, 'User is not exists')
                return redirect('registration')
        if request.user.is_authenticated:
            return redirect('logout')
        args = {
            'type': 'login',
        }
        return render(request, 'login.html', args)

    def registration(request):
        if request.method == 'POST':
            username = request.POST['username']
            email = request.POST['email']
            password = request.POST['password']
            password2 = request.POST['password2']
            if password == password2:
                try:
                    User.objects.create_user(username, email, password)
                    messages.info(request, 'Good. Now login pleace')
                    return redirect('start')
                except IntegrityError as ex:
                    messages.info(request, ex)
                    return redirect('start')
            else:
                messages.info(request, 'passwords are not equal')
                return redirect('registration')
        if request.user.is_authenticated:
            return redirect('logout')
        return render(request, 'registration.html')

    def user_logout(request):
        logout(request)
        messages.info(request, 'Good bye')
        return redirect('login')
    return 'bolt'



class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]