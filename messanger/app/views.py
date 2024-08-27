
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.core.mail import send_mail
from django.db.models import Q
from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from .models import User, Message, Chat
from django.contrib.auth.hashers import make_password, check_password
import random


def index(request):
    return render(request, 'index.html')
def generateToken():
    s = 'asdfklewjtw;ogkassdklgfnmsdklgnwjklegnweklfg'
    return ''.join([s[random.randint(0, len(s) - 1)] for i in range(32)])

def ajaxReg(request):
    email = request.POST['email']
    password = request.POST['password']
    if User.objects.filter(login=email).exists():
        return HttpResponse('1')
    token = generateToken()
    user = User()
    user.login = email
    user.password = make_password(password)
    user.token = token
    user.save()
    url = f'http://127.0.0.1:8000/suc/{token}'
    send_mail(subject='Активация учетной записи', message=url, from_email=settings.EMAIL_HOST_USER,
              recipient_list=[email])

    #request.session['user'] = email
    return HttpResponse('2')

def sucuser(request, token):
    if User.objects.filter(token=token).exists():
        User.objects.filter(token=token).update(suc=1, token='')
        return HttpResponse('Вы успешно активировали свою учетную запись! <a href="/">Перейти на сайт</a>')
    else:
        return HttpResponse('Token не верный!')

def ajaxAuth(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        if User.objects.filter(login=email).exists():
            if User.objects.filter(login=email, suc=1).exists():
                user = User.objects.filter(login=email).first()
                if check_password(password, user.password) and email == user.login:
                    request.session['user'] = email
                    return HttpResponse('3')
                else:
                    return HttpResponse('2')
            else:
                return HttpResponse('1')
        else:
            return  HttpResponse('4')
    else:
        return HttpResponse('5')

def profile(request):
    current_user = User.objects.filter(login=request.session['user']).first()
    return render(request, 'chat/profile.html', {'chats': getChatUser(current_user)})

def chat(request):
    all_users = User.objects.all()
    curent_user = User.objects.filter(login=request.session['user']).first()
    messages = Message.objects.filter(user=curent_user).order_by('created_at')

    return render(request, 'chat/chat.html', {'all_users': all_users,'messages':messages, 'chats': getChatUser(curent_user)})

def get_chat(request, id):
    from django.utils import timezone
    from datetime import datetime
    all_users = User.objects.all()
    current_chat = get_object_or_404(Chat, id=id)
    messages = Message.objects.filter(chat=current_chat).order_by('created_at')

    curent_user = User.objects.filter(login=request.session['user']).first()
    curent_user.update_at = timezone.localtime()
    curent_user.save()

    current_date = datetime.now().date().strftime('%Y-%m-%d')
    current_time = datetime.now().time().strftime('%H:%M')

    return render(request, 'chat/chat.html', {'current_time': current_time, 'current_date': current_date, 'all_users':all_users,'current_chat': current_chat, 'curent_user': curent_user, 'messages':messages, 'chats': getChatUser(curent_user)})


def settings(request):
    curent_user = User.objects.filter(login=request.session['user']).first()
    return render(request, 'chat/settings.html', {'chats': getChatUser(curent_user)})

def create_chat(request):
    if 'user' in request.session:
        if request.method == 'POST':
            title = request.POST['title']
            description = request.POST['description']
            curent_user = User.objects.filter(login=request.session['user']).first()
            #get_object_or_404(User)
            new_chat = Chat(title=title, description=description, creator=curent_user)
            new_chat.save()

    return redirect('/chat')


def getChatUser(user):
    ch = Chat.objects.filter(
        Q(creator=user) | Q(users__in=[user])
    )
    return ch


def add_user(request, id_chat, id_user):
    chat = get_object_or_404(Chat, id=id_chat)
    user = get_object_or_404(User, id=id_user)
    current_user = get_object_or_404(User, login=request.session['user'])
    if chat.creator.id == current_user.id:
        chat.users.add(user)
    return redirect(f'/chat/{id_chat}')


def settings_chat(request):
    if request.method == 'POST' and 'user' in request.session:
        path = ''
        id_chat = request.POST['id_chat']
        title = request.POST['title']
        description = request.POST['description']
        if 'avatar_chat' in request.FILES:
            if request.FILES['avatar_chat']:
                file = request.FILES['avatar_chat']
                fs = FileSystemStorage()
                fs.save('avatar_chat/' + file.name, file)
                path = 'avatar_chat/' + file.name

        chat = Chat.objects.filter(id=id_chat).first()
        chat.title = title
        chat.description = description

        if path != '':
            chat.avatar = path
        else:
            chat.avatar = None
        chat.save()

        return redirect(f'/chat/{id_chat}')


def deletemessage(request, id_message, id_chat):
    message = Message.objects.filter(id=id_message).first()
    current_user = User.objects.filter(login=request.session['user']).first()
    if current_user == message.user:
        Message.objects.filter(id=id_message).delete()
    return redirect('/chat/'+str(id_chat))

