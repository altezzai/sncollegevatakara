from django.urls import path
from . import views

urlpatterns = [
    # ... other URL patterns
    path('', views.index, name='index'),
    path('news/<int:nw_id>/', views.news, name='news'),
    path('allnews', views.allnews, name='allnews'),
    path('events/<int:ev_id>/', views.events, name='events'),
    path('allevents', views.allevents, name='allevents'),
    path('faculty/<str:dept>/', views.faculty, name='faculty'),
    path('notification', views.notification, name='notification'),
    path('notification2/<int:noti_id>/', views.notification2, name='notification2'),
    path('notificationfilter/<str:upg>/', views.notificationfilter, name='notificationfilter'),

    # Campus Life (admin)
    path('campus-life/admin/scholarships/', views.scholarship_item_list, name='scholarship_item_list'),
    path('campus-life/admin/scholarships/create/', views.scholarship_item_create, name='scholarship_item_create'),
    path('campus-life/admin/scholarships/<int:item_id>/update/', views.scholarship_item_update, name='scholarship_item_update'),
    path('campus-life/admin/scholarships/<int:item_id>/delete/', views.scholarship_item_delete, name='scholarship_item_delete'),
    path('campus-life/admin/other-clubs-committees/', views.club_committee_item_list, name='club_committee_item_list'),
    path('campus-life/admin/other-clubs-committees/create/', views.club_committee_item_create, name='club_committee_item_create'),
    path('campus-life/admin/other-clubs-committees/<int:item_id>/update/', views.club_committee_item_update, name='club_committee_item_update'),
    path('campus-life/admin/other-clubs-committees/<int:item_id>/delete/', views.club_committee_item_delete, name='club_committee_item_delete'),
    path('campus-life/admin/<slug:slug>/', views.campus_life_member_list, name='campus_life_member_list'),
    path('campus-life/admin/<slug:slug>/create/', views.campus_life_member_create, name='campus_life_member_create'),
    path('campus-life/admin/member/<int:member_id>/update/', views.campus_life_member_update, name='campus_life_member_update'),
    path('campus-life/admin/member/<int:member_id>/delete/', views.campus_life_member_delete, name='campus_life_member_delete'),
    path('campus-life/admin/<slug:slug>/gallery/', views.campus_life_gallery_list, name='campus_life_gallery_list'),
    path('campus-life/admin/<slug:slug>/gallery/create/', views.campus_life_gallery_create, name='campus_life_gallery_create'),
    path('campus-life/admin/gallery/<int:item_id>/update/', views.campus_life_gallery_update, name='campus_life_gallery_update'),
    path('campus-life/admin/gallery/<int:item_id>/delete/', views.campus_life_gallery_delete, name='campus_life_gallery_delete'),

    # Campus Life (dynamic)
    path('campus-life/', views.campus_life, name='campus_life'),
    path('campus-life/<slug:slug>/', views.campus_life_page, name='campus_life_page'),

    # Legacy endpoints removed (migrated to Campus Life)
    path('about', views.about, name='about'),
    path('about/history', views.history, name='history'),
    path('about/vision-mission', views.vision_mission, name='vision_mission'),
    path('about/funding-agencies', views.funding_agencies, name='funding_agencies'),
    path('about/icc', views.icc, name='icc'),

    path('administration/statutory-bodies', views.statutory_bodies, name='statutory_bodies'),
    path('administration/administrative-office', views.administrative_office, name='administrative_office'),
    path('administration/organogram', views.organogram, name='organogram'),
    path('administration/rti', views.rti, name='rti'),
    path('alumni', views.alumni, name='alumni'),
    path('contact-us', views.contact_us, name='contact_us'),
    path('gallery', views.gallery, name='gallery'),
    path('gallery/admin/', views.gallery_item_list, name='gallery_item_list'),
    path('gallery/admin/create/', views.gallery_item_create, name='gallery_item_create'),
    path('gallery/admin/<int:item_id>/update/', views.gallery_item_update, name='gallery_item_update'),
    path('gallery/admin/<int:item_id>/delete/', views.gallery_item_delete, name='gallery_item_delete'),
    path('gallery/admin/<int:item_id>/images/<int:image_id>/delete/', views.gallery_image_delete, name='gallery_image_delete'),

    path('annual-reports/', views.annual_reports, name='annual_reports'),
    path('annual-reports/admin/', views.annual_report_list, name='annual_report_list'),
    path('annual-reports/admin/create/', views.annual_report_create, name='annual_report_create'),
    path('annual-reports/admin/<int:report_id>/update/', views.annual_report_update, name='annual_report_update'),
    path('annual-reports/admin/<int:report_id>/delete/', views.annual_report_delete, name='annual_report_delete'),
    path('courses', views.courses, name='courses'),
    path('FYUGP', views.FYUGP, name='FYUGP'),
    path('applicatonforms', views.applicatonforms, name='applicatonforms'),
    path('courses', views.courses, name='courses'),
    path('universityinfo', views.universityinfo, name='universityinfo'),
    path('iqac', views.iqac, name='iqac'),
    path('iqac/admin/', views.iqac_member_list, name='iqac_member_list'),
    path('iqac/admin/create/', views.iqac_member_create, name='iqac_member_create'),
    path('iqac/admin/<int:member_id>/update/', views.iqac_member_update, name='iqac_member_update'),
    path('iqac/admin/<int:member_id>/delete/', views.iqac_member_delete, name='iqac_member_delete'),
    path('manager', views.manager, name='manager'),
    path('principal', views.principal, name="principal"),

    path('create_employee', views.create_employee, name='create_employee'),
    path('employee_list', views.employee_list, name='employee_list'),
    path('delete_employee/<int:employee_id>/', views.delete_employee, name='delete_employee'),
    path('update_employee/<int:employee_id>/', views.update_employee, name='update_employee'),

    path('event/create/', views.event_create, name='event_create'),
    path('event/<int:event_id>/update/', views.event_update, name='event_update'),
    path('event/<int:event_id>/delete/', views.event_delete, name='event_delete'),
    path('events/', views.event_list, name='event_list'),  # Create a view for listing events

    path('news/', views.news_list, name='news_list'),
    path('news/create/', views.create_news, name='create_news'),
    path('news/update/<int:pk>/', views.update_news, name='update_news'),
    path('news/delete/<int:pk>/', views.delete_news, name='delete_news'),

    path('create_notification/', views.create_notification, name='create_notification'),
    path('update_notification/<int:notification_id>/', views.update_notification, name='update_notification'),
    path('delete_notification/<int:notification_id>/', views.delete_notification, name='delete_notification'),
    path('list_notifications/', views.list_notifications, name='list_notifications'),
    
    path('create_banner/', views.create_banner, name='create_banner'),
    path('update_banner/<int:banner_id>/', views.update_banner, name='update_banner'),
    path('delete_banner/<int:banner_id>/', views.delete_banner, name='delete_banner'),
    path('list_banners/', views.list_banners, name='list_banners'),
    path('banner/<int:banner_id>/', views.banner_detail, name='banner_detail'),

    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),


]
