from django.shortcuts import render, reverse, redirect
from main.models import Instructor, Student, Lesson, User
from django.contrib.auth import authenticate
from django.http import JsonResponse
from django.core.mail import send_mail
import string, random
from django.core.files.storage import FileSystemStorage

# Create your views here.
import datetime

def home(request):
    return render(request, 'index.html')

def login(request):
    if request.POST:
        user = authenticate(username=request.POST['inputemail'], password=request.POST['inputpassword'])
        user = User.objects.filter(username__exact=request.POST['inputemail'])
        if user.exists() :    
            if user.get().password == request.POST['inputpassword'] and not user.get().blocked:
                return redirect('home')
        #   else:
        #       message.success("did you forget your password ?!!")
        return render(request, "Log-In.html")

    else:
        return render(request, "Log-In.html")

def signup1(request):
    if request.POST:
       
        if 'name' in request.POST.keys() and 'email' in request.POST.keys() and 'inputpassword' in request.POST.keys():
            name =  request.POST['name']
            email = request.POST['email']
            passwrd = request.POST['inputpassword']
            code = request.POST['code']
            if code == 'i':
                newUser = Instructor()
            elif code =='s':
                newUser = Student()
            else:
                return redirect('signup1')
            newUser.name = name
            newUser.password = passwrd
            newUser.email = email
            newUser.username = email
            newUser.blocked = True
            newUser.save()
            
            return redirect('signup2', user_id = newUser.Id)
    return render(request, 'sign-up-first-step.html')

def signup2(request, user_id):
    if request.POST:
        user = Instructor.objects.get(pk= user_id)
        if request.FILES['imgFile']:
            fs = FileSystemStorage()
            myfile = request.FILES['imgFile']
            filename = fs.save(user_id + '_img', myfile)
            user.img = user_id + '_img'
        if 'profession' in request.POST.keys() and 'catchphrase' in request.POST.keys():
            user.field = request.POST['profession']
            user.catch_phrase = request.POST['catchphrase']
            user.intro_msg = request.POST['self-introduction']
            user.what_you_can_ask_for = request.POST['askfor']
            user.save()
            return redirect('signup3', user_id = user_id)
    return render(request, 'sign-up-second-step.html', context={'user_id':user_id})

def signup3(request, user_id):
    if request.POST:
        user = Instructor.objects.get(pk= user_id)
        user.blocked = False
        user.save()
        return redirect('home')
    return render(request, 'sign-up-third-step.html', context={'user_id':user_id})

def resetPass(request):
    if request.POST:
        email = request.POST['email']
        token = ''
        for i in range( len(str(email))):
            token += email[i] + random.choice(string.ascii_letters)
        print(token)
        send_mail(
            'Reset Password',
            'Dear User,\nPlease press on the link below to reset your password  <a href="http://127.0.0.1:8000/resetPass2/?token=' + token + '">this is the link</a> ',
            'guidemeemail@gmail.com',
            [email],
            fail_silently=False
        )
        return redirect('resetPass1')
    return render(request, 'reset-password.html')

def resetPass1(request):
    return render(request, 'reset-password1.html')

def resetPass2(request, token):
    if request.POST:
        print('t',request.POST.keys())
        username = 's'
        for i in range(len(token)):
            if i % 2 != 0:
                username += token[i]
        print(username)
    return render(request, 'reset-password2.html')

def admin_page(request):
    instructors = Instructor.objects.all()
    students = Student.objects.all()

    completed_lessons = Lesson.objects.filter(Date__lt = datetime.datetime.now())
    tobe_started_lessons = Lesson.objects.filter(Date__gt=datetime.datetime.now())
    inprogress_lessons = Lesson.objects.filter(Date=datetime.datetime.today())
   
    return render(request, 'admin.html', 
    
                            context={   'completed_lessons':completed_lessons, 'tobe_started_lessons':tobe_started_lessons, 
                                        'inprogress_lessons':inprogress_lessons, 'instructors':instructors, 
                                        'students':students, 'len_completed_lessons':str(len(completed_lessons)),
                                        'len_inprogress_lessons':str(len(inprogress_lessons)), 'len_tobe_started_lessons':str(len(tobe_started_lessons))
                                    }
                )

def instructor_page(request, ins_id):
    ins = Instructor.objects.get(pk=ins_id)
    return render(request, 'Instructor_Page.html', {'ins':ins})

def student_page(request, stu_id):
    stu = Student.objects.get(pk=stu_id)
    return render(request, 'student_page.html', {'stu':stu})

def small_lesson_page(request):
    return render(request, 'smallLesson_page.html')

def lesson_page(request):
    return render(request, 'lesson_page.html')

def block_instructor(request, user_id):

    user_x = Instructor.objects.get(pk= user_id)
    user_x.blocked = not user_x.blocked
    user_x.save()
    return redirect('admin_page')

def block_student(request, user_id):

    user_x = Student.objects.get(pk= user_id)
    user_x.blocked = not user_x.blocked
    user_x.save()
    return redirect('admin_page')

def advisors_page(request):
    instructors = Instructor.objects.all()
    return render (request, 'advisors.html', context={'instructors':instructors})

def zoom(request):
    return render(request, 'zoom.html')

def edit_lesson_reservation(request):
    return render(request, 'edit_lesson_reservation.html')

def history_lessons(request):
    return render(request, 'history_lessons.html')

def lesson_details(request, lesson_id =4):
    return render(request, 'lesson_details.html')

def lesson_reservation(request):
    if request.POST:
        lesson = Lesson(title=request.POST['lesson-title'], 
        starting= request.POST['start-hour']+ ':'+request.POST['start-min'], 
        ending=request.POST['end-hour'] +' : '+ request.POST['end-min'] )
        lesson.save()
    lessons = Lesson.objects.all()
    return render(request, 'lesson_reservation.html', {'lessons':lessons})

def reserved_lessons(request):
    return render(request, 'reserved_lessons.html')