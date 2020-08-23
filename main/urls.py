from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls import url
from main import views

urlpatterns = [
    url(r'^$', views.home, name="home"),
    url(r'^login/$', views.login, name="login"),
    url(r'^signup1/$', views.signup1, name="signup1"),
    url(r'^signup2/(?P<user_id>.*)$', views.signup2, name="signup2"),
    url(r'^signup3/(?P<user_id>.*)$', views.signup3, name="signup3"),
    url(r'^resetPass/$', views.resetPass, name="resetPass"),
    url(r'^resetPass1/$', views.resetPass1, name="resetPass1"),
    url(r'^resetPass2/(?P<token>.*)$', views.resetPass2, name="resetPass2"),
    url(r'^admin_page/$', views.admin_page, name="admin_page"),
    url(r'^instructor_page/(?P<ins_id>.*)', views.instructor_page, name="instructor_page"),
    url(r'^student_page/(?P<stu_id>.*)', views.student_page, name="student_page"),
    url(r'^lesson_page/$', views.lesson_page, name="lesson_page"),
    url(r'^small_lesson_page/$', views.small_lesson_page, name="small_lesson_page"),
    url(r'^block_instructor/(?P<user_id>.*)', views.block_instructor, name="block_instructor"),
    url(r'^block_student/(?P<user_id>.*)', views.block_student, name="block_student"),
    url(r'^advisors_page/$', views.advisors_page, name="advisors_page"),
    url(r'^lesson_details/(?P<lesson_id>.*)', views.lesson_details, name="lesson_details"),
    url(r'^lesson_details/$', views.lesson_details, name="lesson_details"),
    url(r'^lesson_reservation/$', views.lesson_reservation, name="lesson_reservation"),
    url(r'^edit_lesson_reservation/$', views.edit_lesson_reservation, name="edit_lesson_reservation"),
    url(r'^reserved_lessons/$', views.reserved_lessons, name="reserved_lessons"),
    url(r'^history_lessons/$', views.history_lessons, name="history_lessons"),
    url(r'^zoom/$', views.zoom, name="zoom"),
]


urlpatterns += staticfiles_urlpatterns()
