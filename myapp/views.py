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
from PIL import Image
from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile
import sys
import os
from django.conf import settings
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
            try:
                # First check if a file was uploaded
                if 'photo' not in request.FILES:
                    return render(request, 'create_employee.html', 
                                {'error': 'Please upload a photo'})
                
                photo = request.FILES['photo']
                
                # Validate file type
                if not photo.content_type.startswith('image/'):
                    return render(request, 'create_employee.html', 
                                {'error': 'Please upload a valid image file'})
                
                # Check file size (e.g., max 5MB)
                if photo.size > 5 * 1024 * 1024:  # 5MB in bytes
                    return render(request, 'create_employee.html', 
                                {'error': 'Photo size should be less than 5MB'})
                
                # If all checks pass, compress the photo
                try:
                    compressed_photo = compress_image(photo)
                except Exception as e:
                    return render(request, 'create_employee.html', 
                                {'error': f'Error processing photo: {str(e)}'})
                
                # Continue with creating employee...
                employee = Employee(
                    name=request.POST.get('name'),
                    position=request.POST.get('position'),
                    photo=compressed_photo,
                    qualification=request.POST.get('qualification'),
                    department=request.POST.get('department')
                )
                employee.save()
                
                return redirect('employee_list')
                
            except Exception as e:
                return render(request, 'create_employee.html', 
                            {'error': f'Error creating employee: {str(e)}'})
                
        return render(request, 'create_employee.html')
    return redirect('login')
def employee_list(request):
    if 'username' in request.session:
        employees = Employee.objects.all().order_by('-id')
        return render(request, 'employee_list.html', {'employees': employees})
    return redirect('login')
def delete_old_photo(employee):
    """
    Safely delete the old photo file from storage
    """
    if employee.photo:
        if os.path.isfile(employee.photo.path):
            try:
                os.remove(employee.photo.path)
            except Exception as e:
                print(f"Error deleting old photo: {e}")
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
            employee.qualification = qualification
            if 'photo' in request.FILES:
                        photo = request.FILES['photo']
                        
                        # Validate file type
                        if not photo.content_type.startswith('image/'):
                            return render(request, 'update_employee.html', 
                                        {'employee': employee, 
                                        'error': 'Please upload a valid image file'})
                        
                        # Check file size (max 5MB)
                        if photo.size > 5 * 1024 * 1024:
                            return render(request, 'update_employee.html', 
                                        {'employee': employee, 
                                        'error': 'Photo size should be less than 5MB'})
                        
                        try:
                            # Delete old photo first
                            delete_old_photo(employee)
                            # Compress and save new photo
                            compressed_photo = compress_image(photo)
                            employee.photo = compressed_photo
                        except Exception as e:
                            return render(request, 'update_employee.html', 
                                        {'employee': employee, 
                                        'error': f'Error processing photo: {str(e)}'})
                    

            employee.save()
            return redirect('employee_list')

        return render(request, 'update_employee.html', {'employee': employee})
    return redirect('login')
def delete_employee(request, employee_id):
    if 'username' in request.session:
        employee = get_object_or_404(Employee, pk=employee_id)
        employee.delete()
        delete_old_photo(employee)
        return redirect('employee_list')
    return redirect('login')
#Event

def compress_image(image_file):
    """
    Compress the input image file while maintaining aspect ratio
    Returns a compressed InMemoryUploadedFile object
    """
    img = Image.open(image_file)
    
    # Convert to RGB if image is in RGBA mode
    if img.mode == 'RGBA':
        img = img.convert('RGB')
    
    # Set maximum dimensions
    max_width = 800
    max_height = 800
    
    # Calculate new dimensions while maintaining aspect ratio
    ratio = min(max_width/img.width, max_height/img.height)
    new_width = int(img.width * ratio)
    new_height = int(img.height * ratio)
    
    # Resize image
    img = img.resize((new_width, new_height), Image.Resampling.LANCZOS)
    
    # Save the compressed image
    output = BytesIO()
    img.save(output, format='JPEG', quality=75, optimize=True)
    output.seek(0)
    
    return InMemoryUploadedFile(
        output,
        'ImageField',
        f"{image_file.name.split('.')[0]}.jpg",
        'image/jpeg',
        sys.getsizeof(output),
        None
    )
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
            
            # Create the news article first
            news_article = News.objects.create(
                title=title,
                description=description,
                date=d
            )
            
            # Process and save each uploaded image
            for image_file in request.FILES.getlist('photos'):
                # Compress the image
                compressed_image = compress_image(image_file)
                
                # Create NewsImage object with compressed image
                NewsImage.objects.create(
                    news_article=news_article,
                    image=compressed_image
                )
            
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
            
            # Handle new images
            if request.FILES:
                for image_file in request.FILES.getlist('photos'):
                    # Compress each new image
                    compressed_image = compress_image(image_file)
                    
                    # Create new NewsImage object with compressed image
                    NewsImage.objects.create(
                        news_article=article,
                        image=compressed_image
                    )
            
            article.save()
            # for image_file in request.FILES.getlist('photos'):
            #     NewsImage.objects.create(news_article=article, image=image_file)

            return redirect('news_list')

        return render(request, 'update_news.html', {'article': article})
    return redirect('login')

# news/views.py


def delete_news(request, pk):
    """
    Delete a news article and all its associated images
    """
    if 'username' in request.session:
        try:
            # Get the news article
            article = get_object_or_404(News, pk=pk)
            
            # Get all associated images before deleting the article
            images = NewsImage.objects.filter(news_article=article)
            
            # Delete each image file from storage
            for image in images:
                if image.image:
                    # Get the full path of the image
                    image_path = os.path.join(settings.MEDIA_ROOT, str(image.image))
                    try:
                        # Check if file exists before attempting deletion
                        if os.path.isfile(image_path):
                            os.remove(image_path)
                    except Exception as e:
                        print(f"Error deleting image file {image_path}: {e}")
            
            # Delete the news article (this will also delete associated NewsImage objects
            # due to CASCADE deletion in the database)
            article.delete()
            
            return redirect('news_list')
            
        except Exception as e:
            # Log the error and redirect
            print(f"Error deleting news article {pk}: {e}")
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