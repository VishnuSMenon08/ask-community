from django.shortcuts import render,HttpResponse,redirect,reverse
from ask.models import Profile,Question,Poll,Answer,Comment
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import authenticate,login
from ask.forms import RegistrationForm

def register(request):
    registration_form = RegistrationForm(request.POST)
    context = {'form' : registration_form}
    if request.method == "POST":
        registration_form = RegistrationForm(request.POST)
        if registration_form.is_valid():
            registration_form.save(commit=True)
            messages.success(request,"Thank you for registering with us !")
            return redirect('askCommunity:login')
        else:
            context['message'] = registration_form.errors
            context['form'] = registration_form
    return render(request,'register.html',context =  context)

def home(request):
    context_dict = {}
    discussions = {}
    all_queries = Question.objects.all().order_by("-date_updated")
    for query in all_queries:
        discussions[query.question_id] = {}
        discussions[query.question_id]['query'] = query
        try:
            latest_answer =  Answer.objects.filter(question_id=query.question_id).order_by('-date_answered')[0]
            discussions[query.question_id]['latestAnswer'] = latest_answer
            discussions[query.question_id]['comments'] = Comment.objects.filter(answer_id = latest_answer.answer_id)
        except:
            discussions[query.question_id]['latestAnswer'] = "No Answers yet"
            discussions[query.question_id]['comments'] = "No Comments yet"     
    if request.user.is_authenticated:
        user = request.user
        profile = Profile.objects.get(user = user)
        context_dict['user'] = user
        context_dict['profile'] = profile
    context_dict['discussions'] = discussions
    return render(request,'home.html',context = context_dict)

def detail(request,question_id):
    if request.method == "POST":
        if not request.user.is_authenticated:
            return redirect('askCommunity:login')
        question = Question.objects.get(question_id = question_id)
        answer = Answer()
        answer.question_id = question
        answer.answer = request.POST.get('answer')
        answer.answered_by = Profile.objects.get(user = request.user)
        answer.save()
    else:
        question = Question.objects.get(question_id = question_id)
    all_answers = Answer.objects.filter(question_id = question_id)
    context = {'question' : question,
    'answers' : all_answers}
    return render(request,'detail.html',context = context)

def login_user(request):
    if request.method == "POST":
        username = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(username=username,password=password)
        if user:
            login(request,user)
            return redirect("askCommunity:home")
    return render(request,'login.html')

@login_required(login_url = '/forum/login')
def comment(request,answer_id):
    if request.method == "POST":
        comment = Comment()
        comment.comment = request.POST.get('comment-box')
        comment.commented_by = Profile.objects.get(user = request.user)
        comment.answer_id = Answer.objects.get(answer_id = answer_id)
        comment.save()
        messages.success(request,"Comment posted!")
    return redirect("askCommunity:home")

@login_required(login_url = '/forum/login')
def post_query(request):
    if request.method == "POST":
        query = Question()
        query.question = request.POST.get('question-area')
        query.asked_by = Profile.objects.get(user = request.user)
        query.save()
        messages.success(request,"Your Question was posted!")
    return redirect("askCommunity:home")



