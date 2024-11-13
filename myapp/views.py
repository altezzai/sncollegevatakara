from django.shortcuts import render, redirect ,get_object_or_404
from .models import Employee
from .models import Event
from .models import News,NewsImage
from .models import Notification
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from datetime import date
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth import login, authenticate
#home
def index(request):
    # employees = Employee.objects.all()
    evt = Event.objects.all().order_by('-date')[:3]

    nws = News.objects.all().order_by('-id')[:3]
    return render(request, 'index.html',{'events': evt,'news': nws})

def news(request,nw_id):
    nw = get_object_or_404(News, pk=nw_id)
    nws = News.objects.all().order_by('-id')[:3]
    return render(request, 'news.html',{'news': nw,'newses': nws})
def allnews(request):
    nws = News.objects.all().order_by('-id')
    return render(request, 'morenews.html',{'newses': nws})

def events(request,ev_id):
    ev = get_object_or_404(Event, pk=ev_id)
    evt = Event.objects.all().order_by('-date')[:3]
    return render(request, 'events.html',{'events': evt,'evt': ev})

def allevents(request):
    evt = Event.objects.all().order_by('-date')
    return render(request, 'allevents.html',{'events': evt})

def faculty(request,dept):
    employees = Employee.objects.filter(department=dept)
    # print(type(employees[0].qualification))
    return render(request, 'faculty.html',{'employees':employees,'depart':dept})

def club(request):
    # employees = Employee.objects.all()
    return render(request, 'nss.html')
def fitness(request):
    # employees = Employee.objects.all()
    return render(request, 'fitness.html')
def bhoomi(request):
    # employees = Employee.objects.all()
    return render(request, 'bhoomi.html')
def courses(request):
    # employees = Employee.objects.all()
    return render(request, 'courses.html')

def FYUGP(request):
    return render(request, 'FYUGP.html')
def iqac(request):
    # employees = Employee.objects.all()
    return render(request, 'iqac.html')
def staffcouncil(request):
    # employees = Employee.objects.all()
    return render(request, 'staffcouncil.html')
def about(request):
    # employees = Employee.objects.all()
    return render(request, 'about.html')
def applicatonforms(request):
    # employees = Employee.objects.all()
    return render(request, 'applicatonforms.html')
def placement(request):
    # employees = Employee.objects.all()
    return render(request, 'placement.html')
def scholarship(request):
    # employees = Employee.objects.all()
    return render(request, 'scholarship.html')
def universityinfo(request):
    # employees = Employee.objects.all()
    return render(request, 'universityinfo.html')
def notification(request):
    noti = Notification.objects.all().order_by('-id')
    return render(request, 'notification2.html',{'notifications':noti,'cat':"all"})
def notificationfilter(request,upg):
    noti = Notification.objects.filter(category=upg).order_by('-id')
    return render(request, 'notification2.html',{'notifications':noti,'cat':upg})
def notification2(request ,noti_id):
    notification = get_object_or_404(Notification, pk=noti_id)

    return render(request, 'notifications.html', {'notification': notification})
    # return render(request, 'notifications.html',{'notification':noti2})

def manager(request):
    return render(request, "manager.html")
def principal(request):
    return render(request, "principal.html")

#Employee
def create_employee(request):
    if 'username' in request.session:
        if request.method == 'POST':
            # Extract data from the request
            name = request.POST.get('name')
            position = request.POST.get('position')
            department = request.POST.get('department')
            photo = request.FILES['photo']
            qualification = request.POST.get('qualification')

            # Create and save a new Employee instance
            employee = Employee(name=name, position=position, photo=photo, qualification=qualification,department=department)
            employee.save()

            return redirect('employee_list')  # Redirect to the list view

        return render(request, 'create_employee.html')
    return redirect('login')
def employee_list(request):
    if 'username' in request.session:
        employees = Employee.objects.all().order_by('-id')
        return render(request, 'employee_list.html', {'employees': employees})
    return redirect('login')
def update_employee(request, employee_id):
    if 'username' in request.session:
        employee = get_object_or_404(Employee, pk=employee_id)

        if request.method == 'POST':
            name = request.POST.get('name')
            position = request.POST.get('position')
            photo = request.FILES.get('photo')
            qualification = request.POST.get('qualification')
            department = request.POST.get('department')
            employee.name = name
            employee.position = position
            employee.department = department
            if photo:
                employee.photo = photo

            employee.qualification = qualification
            employee.save()
            return redirect('employee_list')

        return render(request, 'update_employee.html', {'employee': employee})
    return redirect('login')
def delete_employee(request, employee_id):
    if 'username' in request.session:
        employee = get_object_or_404(Employee, pk=employee_id)
        employee.delete()
        return redirect('employee_list')
    return redirect('login')
#Event

def event_list(request):

    if 'username' in request.session:
        events = Event.objects.all().order_by('-id')
        return render(request, 'event_list.html', {'events': events})
    return redirect('login')
def event_create(request):
    if 'username' in request.session:
        if request.method == 'POST':
            title = request.POST.get('title')
            time = request.POST.get('time')
            date = request.POST.get('date')
            description = request.POST.get('description')
            venue = request.POST.get('venue')
            url = request.POST.get('url')

            event = Event(title=title, time=time, date=date, description=description, venue=venue, url=url)
            event.save()
            return redirect('event_list')
        return render(request, 'event_create.html')
    return redirect('login')
def event_update(request, event_id):
    if 'username' in request.session:
        event = get_object_or_404(Event, pk=event_id)
        if request.method == 'POST':
            event.title = request.POST.get('title')
            event.time = request.POST.get('time')
            event.date = request.POST.get('date')
            event.description = request.POST.get('description')
            event.venue = request.POST.get('venue')
            event.url = request.POST.get('url')
            event.save()
            return redirect('event_list')
        return render(request, 'event_update.html', {'event': event})
    return redirect('login')
def event_delete(request, event_id):
    if 'username' in request.session:
        event = get_object_or_404(Event, pk=event_id)
        event.delete()
        return redirect('event_list')
    return redirect('login')
#News
def news_list(request):
    if 'username' in request.session:
        news_articles = News.objects.all().order_by('-id')
        return render(request, 'news_list.html', {'news_articles': news_articles})
    return redirect('login')

def create_news(request):
    if 'username' in request.session:
        if request.method == 'POST':
            title = request.POST['title']
            description = request.POST['description']
            d = request.POST['date']
            photo = request.FILES['photos']
            # Create the news article
            # News.objects.create(title=title, description=description, date=d, image=photo)
            news_article = News.objects.create(title=title, description=description,date=d)

            # Handle multiple image uploads
            for image_file in request.FILES.getlist('photos'):
                NewsImage.objects.create(news_article=news_article, image=image_file)

            return redirect('news_list')

        return render(request, 'create_news.html')
    return redirect('login')

def update_news(request, pk):
    if 'username' in request.session:
        article = get_object_or_404(News, pk=pk)

        if request.method == 'POST':
            # Update the text fields (title and description)
            article.title = request.POST['title']
            article.description = request.POST['description']
            # photos = request.FILES.get('file')
            # if photos:
            #     article.image = photos
            article.save()
            for image_file in request.FILES.getlist('photos'):
                NewsImage.objects.create(news_article=article, image=image_file)

            return redirect('news_list')

        return render(request, 'update_news.html', {'article': article})
    return redirect('login')

# news/views.py


def delete_news(request, pk):
    if 'username' in request.session:
        event = get_object_or_404(News, pk=pk)
        event.delete()
        return redirect('news_list')
    return redirect('login')
#Notificationreturn redirect('news_list')
def create_notification(request):
    if 'username' in request.session:
        if request.method == 'POST':
            category = request.POST.get('category')
            title = request.POST.get('title')
            description = request.POST.get('description')
            file = request.FILES.get('file')

            notification = Notification(category=category, title=title, description=description, file=file)
            notification.save()
            return redirect('list_notifications')
            return JsonResponse({'message': 'Notification created successfully'})
        return render(request, 'notification_create.html')
    return redirect('login')
@csrf_exempt
def update_notification(request, notification_id):
    if 'username' in request.session:
        notification = get_object_or_404(Notification, pk=notification_id)

        if request.method == 'POST':
            category = request.POST.get('category')
            title = request.POST.get('title')
            description = request.POST.get('description')
            file = request.FILES.get('file')

            # Update the notification attributes
            notification.category = category
            notification.title = title
            notification.description = description

            if file:
                notification.file = file

            # Save the updated notification
            notification.save()

            # Redirect to the list of notifications
            return redirect('list_notifications')

        return render(request, 'notification_update.html', {'notification': notification})
    return redirect('login')
@csrf_exempt
def delete_notification(request, notification_id):
    if 'username' in request.session:
        notification = Notification.objects.get(id=notification_id)
        notification.delete()
        return redirect('list_notifications')
        # return JsonResponse({'message': 'Notification deleted successfully'})
    return redirect('login')
def list_notifications(request):
    if 'username' in request.session:
        notifications = Notification.objects.all().order_by('-id')
        return render(request, 'notification_list.html', {'notifications': notifications})
    return redirect('login')
def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            request.session['username']= username
            return redirect('list_notifications')
        else:
            print('Invalid username or password.')
            return redirect('login')
    return render(request, 'login.html')

def logout(request):
    if 'username' in request.session:
        request.session.flush()
    return redirect('login')