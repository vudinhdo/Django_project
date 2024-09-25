from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from .models import Tour, Blogs, BookTour, City, Comments, User
from django.contrib.auth.decorators import login_required


# Create your views here.
def index(req):
    return render(req, "Pages/index.html")


def hotel(req):
    return render(req, "Pages/hotel.html")


def destination(req):
    destination = Tour.objects.all()
    return render(req, "Pages/destination.html", {"destination": destination})


def dSingle(req, id):
    dSingle = Tour.objects.get(id=id)
    return render(req, "Pages/destination_single.html", {"dSingle": dSingle})


def contact(req):
    return render(req, "Pages/contact.html")


def about(req):
    return render(req, "Pages/about.html")


def blogs(req):
    tus = Blogs.objects.all()
    return render(req, "Pages/blog.html", {"tus": tus})


def blog_single(req, blog_id):
    blog = Blogs.objects.get(id=blog_id)

    return render(req, "Pages/blog_single.html", {"blog": blog})


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            request.session["username"] = username
            return redirect('index')
        else:
            return render(request, 'Pages/login.html', {'error_message': 'Invalid username or password.'})
    else:
        return render(request, 'Pages/login.html')


def logout_view(request):
    logout(request)
    return redirect("/")


def register_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        try:
            User.objects.get(username=username)
        except User.DoesNotExist:
            user = User.objects.create_user(username, email, password)
            user.save()
            return redirect('login_view')
        return redirect("index")

    else:
        return render(request, 'Pages/register.html')


# def add_Author(request):
#     if request.method == 'POST':

@login_required
def profile(request):
    if request.session.get("is_logged_in", True):
        return render(request, "Pages/profile.html")
    else:
        return redirect("login_view")


def add_Comment(request, blog_id, user_id):
    blog = Blogs.objects.get(id=blog_id)
    user = User.objects.get(id=user_id)
    if request.method == 'POST':

        body_comment = request.POST["body_comment"]
        comment = Comments(blog=blog, user_comment=user, body_comment=body_comment)
        comment.save()
        return render(request, "Pages/blog_single.html", {"blog": blog})
    else:
        return render(request, "Pages/blog.html")
