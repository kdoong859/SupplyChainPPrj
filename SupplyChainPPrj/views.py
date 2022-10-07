from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm, PasswordResetForm, PasswordChangeForm, SetPasswordForm
from django.contrib.auth.models import User
from django.contrib.auth.tokens import default_token_generator, PasswordResetTokenGenerator
from django.core.exceptions import ValidationError
from django.core.mail import send_mail, BadHeaderError
from django.db.models import Q
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse


# Create your views here.
from django.template.loader import render_to_string
from django.urls import reverse
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode

from disaster import settings


def login_page(request):
    if request.user.is_authenticated:
        return redirect("dashboard")

    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.data['username'].lower()
            password = form.data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                # starting session for the given user so the server
                # remembers the user next time
                return redirect("dashboard")

    form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})


def logout_page(request):
    logout(request)
    return redirect('login')


@login_required(login_url='/login')
def dashboard(request):
    return render(request, "dashboard.html")


def password_reset(request):
    if request.method == "POST":
        domain = request.headers['Host']
        password_reset_form = PasswordResetForm(request.POST)
        if password_reset_form.is_valid():
            data = password_reset_form.cleaned_data['email']
            associated_users = User.objects.filter(Q(email=data) | Q(username=data))

            if associated_users.exists():
                subject = "Password Reset Requested"
                email_template_name = "email/email.html"
                for user in associated_users:
                    token=default_token_generator.make_token(user)
                    uid=urlsafe_base64_encode(force_bytes(user.pk))
                    c = {
                        "email": user.email,
                        'domain': domain,
                        'site_name': 'Interface',
                        "uid": uid,
                        "user": user,
                        'token': token,
                        'protocol': 'http',
                        'link': 'http://'+domain+"/password-reset/"+uid+"/"+token,

                    }
                    email = render_to_string(email_template_name, c)
                    try:
                        send_mail(subject, email, settings.EMAIL_HOST_USER, [user.email], fail_silently=False)
                    except BadHeaderError:
                        return HttpResponse('Invalid header found.')
                    messages.info(request, 'Email Sent')
                    return redirect("login")

    form = PasswordResetForm()
    return render(request, 'password_reset.html', context={"form": form})


def password_change(request, uid, token):
    try:
        # urlsafe_base64_decode() decodes to bytestring
        uid = urlsafe_base64_decode(uid).decode()
        user = User.objects.get(pk=uid)
    except (
            TypeError,
            ValueError,
            OverflowError,
            User.DoesNotExist,
            ValidationError,
    ):
        user = None
        return HttpResponse("Invalid link")
    if not PasswordResetTokenGenerator().check_token(user, token):
        messages.warning(request, 'Invalid Link')
        print("I am here")
        return redirect('login')
    if request.method == "POST":
        form=SetPasswordForm(user, request.POST)
        if not form.is_valid():
            messages.warning(request, 'Invalid Password')
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        password = form.cleaned_data['new_password1']
        user.set_password(password)
        user.save()
        login(request, user)
        return redirect('dashboard')

    form = SetPasswordForm(user)
    context = {
        'form': form
    }
    return render(request, 'password_change.html', context=context)

