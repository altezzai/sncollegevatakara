from django.shortcuts import render, redirect ,get_object_or_404
from .models import Employee
from .models import Event
from .models import News,NewsImage
from .models import Notification
from .models import Banner
from .models import AnnualReport
from .models import IQACMember
from .models import GalleryItem
from .models import CampusLifePage
from .models import CampusLifeMember
from .models import CampusLifeGalleryItem
from .models import ScholarshipItem, ClubCommitteeItem
from .models import GalleryImage
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from datetime import date
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth import login, authenticate
from django.template.loader import select_template
from PIL import Image
from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile
import sys
import os
from django.conf import settings
import uuid
from collections import OrderedDict
#home
def index(request):
    # employees = Employee.objects.all()
    evt = Event.objects.all().order_by('-date')[:3]

    nws = News.objects.all().order_by('-id')[:3]
    #send banners list also

    bnr = Banner.objects.all().order_by('-id')[:6]
    return render(request, 'index.html',{'events': evt,'news': nws ,'banners':bnr})


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

def courses(request):
    # employees = Employee.objects.all()
    return render(request, 'courses.html')

def FYUGP(request):
    return render(request, 'FYUGP.html')
def iqac(request):
    members = IQACMember.objects.filter(is_active=True)
    return render(request, 'iqac.html', {"members": members})

def about(request):
    # employees = Employee.objects.all()
    return render(request, 'about.html')
def applicatonforms(request):
    # employees = Employee.objects.all()
    return render(request, 'applicatonforms.html')

def campus_life(request):
    pages = CampusLifePage.objects.filter(is_published=True)
    return render(request, 'campus_life_list.html', {'pages': pages})


def campus_life_page(request, slug):
    page = get_object_or_404(CampusLifePage, slug=slug, is_published=True)
    members = page.members.filter(is_active=True)
    gallery_items = page.gallery_items.filter(is_active=True)

    scholarships = None
    scholarships_payload = None
    clubs = None
    if slug == 'scholarships':
        scholarships = ScholarshipItem.objects.filter(page=page, is_active=True)
        scholarships_payload = [
            {
                'id': s.id,
                'name': s.name,
                'image': (s.image.url if s.image else ''),
                'description': s.description or '',
                'link_url': s.link_url or '',
            }
            for s in scholarships
        ]
    if slug == 'other-clubs-committees':
        clubs = ClubCommitteeItem.objects.filter(page=page, is_active=True)

    nss_gallery_groups = None
    if slug == 'nss':
        image_qs = gallery_items.filter(media_type=CampusLifeGalleryItem.TYPE_IMAGE).exclude(image='').exclude(image__isnull=True).order_by('-created_at', '-id')
        video_qs = gallery_items.filter(media_type=CampusLifeGalleryItem.TYPE_VIDEO).exclude(video_file='').exclude(video_file__isnull=True).order_by('-created_at', '-id')

        def build_groups(qs, kind):
            groups = OrderedDict()
            for it in qs:
                batch = str(getattr(it, 'upload_batch', None) or it.id)
                key = f"{kind}:{batch}"
                if key not in groups:
                    groups[key] = {
                        'key': key,
                        'type': kind,
                        'caption': it.caption or '',
                        'items': [],
                    }

                if kind == 'image' and it.image:
                    groups[key]['items'].append(it.image.url)
                if kind == 'video' and it.video_file:
                    groups[key]['items'].append(it.video_file.url)

                # Prefer a non-empty caption from any item in the batch
                if not groups[key]['caption'] and it.caption:
                    groups[key]['caption'] = it.caption
            return list(groups.values())

        nss_gallery_groups = build_groups(image_qs, 'image') + build_groups(video_qs, 'video')

    # Separate template per Campus Life page (falls back to the generic template).
    template_candidates = [
        f"campus_life/{slug}.html",
        "campus_life_detail.html",
    ]
    template = select_template(template_candidates)
    return render(
        request,
        template.template.name,
        {
            'page': page,
            'members': members,
            'gallery_items': gallery_items,
            'nss_gallery_groups': nss_gallery_groups,
            'scholarships': scholarships,
            'scholarships_payload': scholarships_payload,
            'clubs': clubs,
        },
    )


def scholarship_item_list(request):
    if 'username' in request.session:
        page = get_object_or_404(CampusLifePage, slug='scholarships')
        items = ScholarshipItem.objects.filter(page=page).order_by('-created_at', '-id')
        return render(request, 'scholarship_item_list.html', {'page': page, 'items': items, 'active_slug': page.slug})
    return redirect('login')


def scholarship_item_create(request):
    if 'username' in request.session:
        page = get_object_or_404(CampusLifePage, slug='scholarships')
        if request.method == 'POST':
            name = (request.POST.get('name') or '').strip()
            description = (request.POST.get('description') or '').strip()
            link_url = (request.POST.get('link_url') or '').strip()
            image = request.FILES.get('image')
            is_active = True if request.POST.get('is_active') == 'on' else False

            if not name:
                return render(request, 'scholarship_item_create.html', {'page': page, 'error': 'Scholarship name is required.', 'active_slug': page.slug})

            ScholarshipItem.objects.create(
                page=page,
                name=name,
                description=description,
                link_url=link_url,
                image=image,
                is_active=is_active,
            )
            return redirect('scholarship_item_list')

        return render(request, 'scholarship_item_create.html', {'page': page, 'active_slug': page.slug})
    return redirect('login')


def scholarship_item_update(request, item_id):
    if 'username' in request.session:
        item = get_object_or_404(ScholarshipItem, pk=item_id)
        page = item.page
        if page.slug != 'scholarships':
            return redirect('campus_life_member_list', slug=page.slug)

        if request.method == 'POST':
            item.name = (request.POST.get('name') or '').strip()
            item.description = (request.POST.get('description') or '').strip()
            item.link_url = (request.POST.get('link_url') or '').strip()
            item.is_active = True if request.POST.get('is_active') == 'on' else False
            image = request.FILES.get('image')
            if image:
                item.image = image

            if not item.name:
                return render(request, 'scholarship_item_update.html', {'item': item, 'error': 'Scholarship name is required.', 'active_slug': page.slug})

            item.save()
            return redirect('scholarship_item_list')

        return render(request, 'scholarship_item_update.html', {'item': item, 'active_slug': page.slug})
    return redirect('login')


def scholarship_item_delete(request, item_id):
    if 'username' in request.session:
        item = get_object_or_404(ScholarshipItem, pk=item_id)
        item.delete()
        return redirect('scholarship_item_list')
    return redirect('login')


def club_committee_item_list(request):
    if 'username' in request.session:
        page = get_object_or_404(CampusLifePage, slug='other-clubs-committees')
        items = ClubCommitteeItem.objects.filter(page=page).order_by('-created_at', '-id')
        return render(request, 'club_committee_item_list.html', {'page': page, 'items': items, 'active_slug': page.slug})
    return redirect('login')


def club_committee_item_create(request):
    if 'username' in request.session:
        page = get_object_or_404(CampusLifePage, slug='other-clubs-committees')
        if request.method == 'POST':
            name = (request.POST.get('name') or '').strip()
            description = (request.POST.get('description') or '').strip()
            person_name = (request.POST.get('person_name') or '').strip()
            person_position = (request.POST.get('person_position') or '').strip()
            person_photo = request.FILES.get('person_photo')
            is_active = True if request.POST.get('is_active') == 'on' else False

            if not name or not description or not person_name or not person_position:
                return render(
                    request,
                    'club_committee_item_create.html',
                    {'page': page, 'error': 'Club/Committee name, description, person name and position are required.', 'active_slug': page.slug},
                )

            ClubCommitteeItem.objects.create(
                page=page,
                name=name,
                description=description,
                person_name=person_name,
                person_position=person_position,
                person_photo=person_photo,
                is_active=is_active,
            )
            return redirect('club_committee_item_list')

        return render(request, 'club_committee_item_create.html', {'page': page, 'active_slug': page.slug})
    return redirect('login')


def club_committee_item_update(request, item_id):
    if 'username' in request.session:
        item = get_object_or_404(ClubCommitteeItem, pk=item_id)
        page = item.page
        if page.slug != 'other-clubs-committees':
            return redirect('campus_life_member_list', slug=page.slug)

        if request.method == 'POST':
            item.name = (request.POST.get('name') or '').strip()
            item.description = (request.POST.get('description') or '').strip()
            item.person_name = (request.POST.get('person_name') or '').strip()
            item.person_position = (request.POST.get('person_position') or '').strip()
            item.is_active = True if request.POST.get('is_active') == 'on' else False
            person_photo = request.FILES.get('person_photo')
            if person_photo:
                item.person_photo = person_photo

            if not item.name or not item.description or not item.person_name or not item.person_position:
                return render(
                    request,
                    'club_committee_item_update.html',
                    {'item': item, 'error': 'Club/Committee name, description, person name and position are required.', 'active_slug': page.slug},
                )

            item.save()
            return redirect('club_committee_item_list')

        return render(request, 'club_committee_item_update.html', {'item': item, 'active_slug': page.slug})
    return redirect('login')


def club_committee_item_delete(request, item_id):
    if 'username' in request.session:
        item = get_object_or_404(ClubCommitteeItem, pk=item_id)
        item.delete()
        return redirect('club_committee_item_list')
    return redirect('login')


def campus_life_member_list(request, slug):
    if 'username' in request.session:
        page = get_object_or_404(CampusLifePage, slug=slug)
        members = CampusLifeMember.objects.filter(page=page).order_by('sort_order', 'name', 'id')
        return render(request, 'campus_life_member_list.html', {'page': page, 'members': members, 'active_slug': page.slug})
    return redirect('login')


def campus_life_member_create(request, slug):
    if 'username' in request.session:
        page = get_object_or_404(CampusLifePage, slug=slug)

        if request.method == 'POST':
            name = (request.POST.get('name') or '').strip()
            position = (request.POST.get('position') or '').strip()
            photo = request.FILES.get('photo')

            if not name or not position:
                return render(
                    request,
                    'campus_life_member_create.html',
                    {'error': 'Name and Position are required.', 'page': page},
                )

            CampusLifeMember.objects.create(
                page=page,
                name=name,
                position=position,
                photo=photo,
            )
            return redirect('campus_life_member_list', slug=page.slug)

        return render(request, 'campus_life_member_create.html', {'page': page, 'active_slug': page.slug})
    return redirect('login')


def campus_life_member_update(request, member_id):
    if 'username' in request.session:
        member = get_object_or_404(CampusLifeMember, pk=member_id)

        if request.method == 'POST':
            member.name = (request.POST.get('name') or '').strip()
            member.position = (request.POST.get('position') or '').strip()
            member.is_active = True if request.POST.get('is_active') == 'on' else False
            photo = request.FILES.get('photo')
            if photo:
                member.photo = photo

            if not member.name or not member.position:
                return render(
                    request,
                    'campus_life_member_update.html',
                    {'error': 'Name and Position are required.', 'member': member},
                )

            member.save()
            return redirect('campus_life_member_list', slug=member.page.slug)

        return render(request, 'campus_life_member_update.html', {'member': member, 'active_slug': member.page.slug})
    return redirect('login')


def campus_life_member_delete(request, member_id):
    if 'username' in request.session:
        member = get_object_or_404(CampusLifeMember, pk=member_id)
        slug = member.page.slug
        member.delete()
        return redirect('campus_life_member_list', slug=slug)
    return redirect('login')
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


# About Us (static pages)
def history(request):
    return render(request, "history.html")


def vision_mission(request):
    return render(request, "vision_mission.html")


def funding_agencies(request):
    return render(request, "funding_agencies.html")


def icc(request):
    return render(request, "icc.html")


def statutory_bodies(request):
    return render(request, "statutory_bodies.html")


def administrative_office(request):
    return render(request, "administrative_office.html")


def organogram(request):
    return render(request, "organogram.html")


def rti(request):
    return render(request, "rti.html")


def alumni(request):
    return render(request, "alumni.html")


def contact_us(request):
    return render(request, "contact_us.html")


# Gallery (public)
def gallery(request):
    photos = GalleryItem.objects.filter(
        is_active=True,
        media_type=GalleryItem.TYPE_IMAGE,
    ).prefetch_related('images')
    media = GalleryItem.objects.filter(
        is_active=True,
        media_type=GalleryItem.TYPE_VIDEO,
    )
    return render(request, "gallery.html", {"photos": photos, "media": media})


# Gallery (admin CRUD)
def gallery_item_list(request):
    if 'username' in request.session:
        items = GalleryItem.objects.all()
        return render(request, 'gallery_item_list.html', {'items': items})
    return redirect('login')


def gallery_item_create(request):
    if 'username' in request.session:
        if request.method == 'POST':
            title = (request.POST.get('title') or '').strip()
            media_type = request.POST.get('media_type') or GalleryItem.TYPE_IMAGE
            file = request.FILES.get('file')
            files = request.FILES.getlist('files')
            is_active = True if request.POST.get('is_active') == 'on' else False

            if not title:
                return render(
                    request,
                    'gallery_item_create.html',
                    {'error': 'Title is required.'},
                )

            if media_type == GalleryItem.TYPE_VIDEO and not file:
                return render(
                    request,
                    'gallery_item_create.html',
                    {'error': 'Please upload a video file.'},
                )

            if media_type == GalleryItem.TYPE_IMAGE and not files:
                return render(
                    request,
                    'gallery_item_create.html',
                    {'error': 'Please upload one or more images.'},
                )

            item = GalleryItem.objects.create(
                title=title,
                media_type=media_type,
                file=file if media_type == GalleryItem.TYPE_VIDEO else None,
                is_active=is_active,
            )

            if media_type == GalleryItem.TYPE_IMAGE:
                for f in files:
                    GalleryImage.objects.create(gallery_item=item, image=f)

            return redirect('gallery_item_list')

        return render(request, 'gallery_item_create.html')
    return redirect('login')


def gallery_item_update(request, item_id):
    if 'username' in request.session:
        item = get_object_or_404(GalleryItem, pk=item_id)

        if request.method == 'POST':
            item.title = (request.POST.get('title') or '').strip()
            item.media_type = request.POST.get('media_type') or item.media_type
            item.is_active = True if request.POST.get('is_active') == 'on' else False
            file = request.FILES.get('file')
            files = request.FILES.getlist('files')

            if item.media_type == GalleryItem.TYPE_VIDEO:
                if file:
                    item.file = file
            else:
                # For images: add new uploaded images (if any)
                for f in files:
                    GalleryImage.objects.create(gallery_item=item, image=f)

            if not item.title:
                return render(
                    request,
                    'gallery_item_update.html',
                    {'error': 'Title is required.', 'item': item},
                )

            item.save()
            return redirect('gallery_item_list')

        return render(request, 'gallery_item_update.html', {'item': item})
    return redirect('login')


def gallery_item_delete(request, item_id):
    if 'username' in request.session:
        item = get_object_or_404(GalleryItem, pk=item_id)
        item.delete()
        return redirect('gallery_item_list')
    return redirect('login')


def gallery_image_delete(request, item_id, image_id):
    if 'username' in request.session:
        image = get_object_or_404(GalleryImage, pk=image_id, gallery_item_id=item_id)
        image.delete()
        return redirect('gallery_item_update', item_id=item_id)
    return redirect('login')


# Annual Reports
def annual_reports(request):
    reports = AnnualReport.objects.all()
    return render(request, "annual_reports.html", {"reports": reports})


def annual_report_list(request):
    if 'username' in request.session:
        reports = AnnualReport.objects.all()
        return render(request, "annual_report_list.html", {"reports": reports})
    return redirect('login')


def annual_report_create(request):
    if 'username' in request.session:
        if request.method == 'POST':
            title = request.POST.get('title')
            year = request.POST.get('year')
            file = request.FILES.get('file')

            if not file:
                return render(request, "annual_report_create.html", {"error": "Please upload a file"})

            AnnualReport.objects.create(title=title, year=year or 0, file=file)
            return redirect('annual_report_list')

        return render(request, "annual_report_create.html")
    return redirect('login')


def annual_report_update(request, report_id):
    if 'username' in request.session:
        report = get_object_or_404(AnnualReport, pk=report_id)

        if request.method == 'POST':
            report.title = request.POST.get('title')
            report.year = request.POST.get('year') or report.year
            file = request.FILES.get('file')
            if file:
                report.file = file
            report.save()
            return redirect('annual_report_list')

        return render(request, "annual_report_update.html", {"report": report})
    return redirect('login')


def annual_report_delete(request, report_id):
    if 'username' in request.session:
        report = get_object_or_404(AnnualReport, pk=report_id)
        report.delete()
        return redirect('annual_report_list')
    return redirect('login')


# IQAC (Admin CRUD)
def iqac_member_list(request):
    if 'username' in request.session:
        members = IQACMember.objects.all()
        return render(request, 'iqac_member_list.html', {'members': members})
    return redirect('login')


def iqac_member_create(request):
    if 'username' in request.session:
        if request.method == 'POST':
            name = (request.POST.get('name') or '').strip()
            department = (request.POST.get('department') or '').strip()
            role = request.POST.get('role') or IQACMember.ROLE_MEMBER
            photo = request.FILES.get('photo')

            if not name or not department:
                return render(
                    request,
                    'iqac_member_create.html',
                    {'error': 'Name and Department are required.'},
                )

            IQACMember.objects.create(name=name, department=department, role=role, photo=photo)
            return redirect('iqac_member_list')

        return render(request, 'iqac_member_create.html')
    return redirect('login')


def iqac_member_update(request, member_id):
    if 'username' in request.session:
        member = get_object_or_404(IQACMember, pk=member_id)

        if request.method == 'POST':
            member.name = (request.POST.get('name') or '').strip()
            member.department = (request.POST.get('department') or '').strip()
            member.role = request.POST.get('role') or member.role
            member.is_active = True if request.POST.get('is_active') == 'on' else False
            photo = request.FILES.get('photo')
            if photo:
                member.photo = photo

            if not member.name or not member.department:
                return render(
                    request,
                    'iqac_member_update.html',
                    {'error': 'Name and Department are required.', 'member': member},
                )

            member.save()
            return redirect('iqac_member_list')

        return render(request, 'iqac_member_update.html', {'member': member})
    return redirect('login')


def iqac_member_delete(request, member_id):
    if 'username' in request.session:
        member = get_object_or_404(IQACMember, pk=member_id)
        member.delete()
        return redirect('iqac_member_list')
    return redirect('login')

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

# Banner views
def create_banner(request):
    if 'username' in request.session:
        if request.method == 'POST':
            image = request.FILES.get('image')
            url = request.POST.get('url')

            banner = Banner(image=image, url=url)
            banner.save()
            return redirect('list_banners')
        return render(request, 'banner_create.html')
    return redirect('login')
def update_banner(request, banner_id):
    if 'username' in request.session:
        banner = get_object_or_404(Banner, pk=banner_id)

        if request.method == 'POST':
            url = request.POST.get('url')
            image = request.FILES.get('image')

            banner.url = url
            if image:
                banner.image = image

            banner.save()
            return redirect('list_banners')

        return render(request, 'banner_update.html', {'banner': banner})
    return redirect('login')
def delete_banner(request, banner_id):
    if 'username' in request.session:
        banner = get_object_or_404(Banner, pk=banner_id)
        banner.delete()
        return redirect('list_banners')
    return redirect('login')    
def list_banners(request):
    if 'username' in request.session:
        banners = Banner.objects.all().order_by('-created_at')
        return render(request, 'banner_list.html', {'banners': banners})
    return redirect('login')
def banner_detail(request, banner_id):
    if 'username' in request.session:
        banner = get_object_or_404(Banner, pk=banner_id)
        return render(request, 'banner_detail.html', {'banner': banner})
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


def campus_life_gallery_list(request, slug):
    if 'username' in request.session:
        page = get_object_or_404(CampusLifePage, slug=slug)
        if page.slug != 'nss':
            return redirect('campus_life_member_list', slug=page.slug)
        items = CampusLifeGalleryItem.objects.filter(page=page).order_by('-created_at', '-id')
        return render(request, 'campus_life_gallery_list.html', {'page': page, 'items': items, 'active_slug': page.slug})
    return redirect('login')


def campus_life_gallery_create(request, slug):
    if 'username' in request.session:
        page = get_object_or_404(CampusLifePage, slug=slug)
        if page.slug != 'nss':
            return redirect('campus_life_member_list', slug=page.slug)

        if request.method == 'POST':
            media_type = request.POST.get('media_type') or CampusLifeGalleryItem.TYPE_IMAGE
            caption = (request.POST.get('caption') or '').strip()
            images = request.FILES.getlist('image')
            video_files = request.FILES.getlist('video_file')
            is_active = True if request.POST.get('is_active') == 'on' else False
            batch_id = uuid.uuid4()

            if media_type == CampusLifeGalleryItem.TYPE_IMAGE and not images:
                return render(
                    request,
                    'campus_life_gallery_create.html',
                    {'page': page, 'error': 'Please upload an image.', 'active_slug': page.slug, 'selected_type': media_type},
                )

            if media_type == CampusLifeGalleryItem.TYPE_VIDEO and not video_files:
                return render(
                    request,
                    'campus_life_gallery_create.html',
                    {'page': page, 'error': 'Please upload a video file.', 'active_slug': page.slug, 'selected_type': media_type},
                )

            if media_type == CampusLifeGalleryItem.TYPE_IMAGE:
                for img in images:
                    CampusLifeGalleryItem.objects.create(
                        page=page,
                        upload_batch=batch_id,
                        media_type=media_type,
                        caption=caption,
                        image=img,
                        video_file=None,
                        video_url='',
                        is_active=is_active,
                    )
            else:
                for vf in video_files:
                    CampusLifeGalleryItem.objects.create(
                        page=page,
                        upload_batch=batch_id,
                        media_type=media_type,
                        caption=caption,
                        image=None,
                        video_file=vf,
                        video_url='',
                        is_active=is_active,
                    )
            return redirect('campus_life_gallery_list', slug=page.slug)

        return render(request, 'campus_life_gallery_create.html', {'page': page, 'active_slug': page.slug})
    return redirect('login')


def campus_life_gallery_update(request, item_id):
    if 'username' in request.session:
        item = get_object_or_404(CampusLifeGalleryItem, pk=item_id)
        if item.page.slug != 'nss':
            return redirect('campus_life_member_list', slug=item.page.slug)

        if request.method == 'POST':
            item.caption = (request.POST.get('caption') or '').strip()
            item.is_active = True if request.POST.get('is_active') == 'on' else False
            item.media_type = request.POST.get('media_type') or item.media_type

            image = request.FILES.get('image')
            video_file = request.FILES.get('video_file')

            if item.media_type == CampusLifeGalleryItem.TYPE_IMAGE:
                if image:
                    item.image = image
                item.video_file = None
                item.video_url = ''
                if not item.image:
                    return render(request, 'campus_life_gallery_update.html', {'item': item, 'error': 'Image is required.', 'active_slug': item.page.slug})
            else:
                if video_file:
                    item.video_file = video_file
                item.video_url = ''
                item.image = None
                if not item.video_file:
                    return render(request, 'campus_life_gallery_update.html', {'item': item, 'error': 'Video file is required.', 'active_slug': item.page.slug})

            item.save()
            return redirect('campus_life_gallery_list', slug=item.page.slug)

        return render(request, 'campus_life_gallery_update.html', {'item': item, 'active_slug': item.page.slug})
    return redirect('login')


def campus_life_gallery_delete(request, item_id):
    if 'username' in request.session:
        item = get_object_or_404(CampusLifeGalleryItem, pk=item_id)
        if item.page.slug != 'nss':
            return redirect('campus_life_member_list', slug=item.page.slug)
        slug = item.page.slug
        item.delete()
        return redirect('campus_life_gallery_list', slug=slug)
    return redirect('login')