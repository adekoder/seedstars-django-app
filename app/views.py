from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.core.paginator import Paginator
from django.views.decorators.http import require_http_methods
from .forms import AddUserForm
from .models import User

# Create your views here.

from django.http import HttpResponse

@require_http_methods(['GET'])
def index(request):
    return render(request, 'app/index.html')

@require_http_methods(['GET'])
def list_users(request):
    users = User.objects.order_by('-created_at')
    paginator = Paginator(users, 5) 
    page = request.GET.get('page')
    users = paginator.get_page(page)
    return render(request, 'app/list.html', {'users': users})
    
@require_http_methods(['GET', 'POST'])
def add_user(request):
    
    if request.method == 'POST':
        form = AddUserForm(request.POST)
        
        if form.is_valid():
            data = form.cleaned_data
            user = User(name=data['name'], email=data['email'])
            user.save()
            form = AddUserForm()
            messages.add_message(request, messages.SUCCESS, 'Hooray!, new user added')
            return HttpResponseRedirect('/add')
        
    else:
        form = AddUserForm()
    return render(request, 'app/add.html', {'form': form})