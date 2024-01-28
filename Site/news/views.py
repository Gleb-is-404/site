from django.shortcuts import render
from .models import int_info, users, tag
from django.http import JsonResponse
import django.contrib.auth
from urllib.parse import unquote
'''
from .forms import PostForm
from django.views.generic import DetailView, UpdateView, DeleteView'''
from django.http import HttpResponse
# Create your views here.
import mysql.connector
import json
import io
import sys

# Establish a connection to your MySQL database
'''db = mysql.connector.connect(
    host='localhost',
    user='Gleb',
    password='swattheevil',
    database='giraffe'
)
cursor = db.cursor()
# Define your SQL query
query = "SELECT * FROM employee"

# Execute the query
cursor.execute(query)

# Fetch all rows from the result set
rows = cursor.fetchall()'''
'''tag.objects.create(name=inp['name'], surname=inp['surname'], email_address=inp['email'], points=100)''' 
def func_do(inp):
    locals().update(inp['function_exec'])
    original_stdout = sys.stdout
    sys.stdout = open('output.txt', 'w')
    result = exec(inp['function'])
    sys.stdout.close()
    sys.stdout = original_stdout
    with open('output.txt', 'r') as output_file:
        captured_output = output_file.read()
    inp['text']=captured_output
    return inp
def data_saver(inp):
    int_info.objects.create(function_name=inp['function_name'], function_description=inp['function_description'], function_input=inp['function_input'], function_function=inp['function_function'], function_tags=inp['function_tags'])
    '''int_info.objects.create(function_name='ijoj', function_description='jkllk', function_input=['j90', 'jol'], function_function='jkjkj')'''
    return inp
def registrator(inp):
    users.objects.create(name=inp['name'], surname=inp['surname'], email_address=inp['email'], points=100)
    '''int_info.objects.create(function_name='ijoj', function_description='jkllk', function_input=['j90', 'jol'], function_function='jkjkj')'''
    return inp
def data_sender(inp):
    queryset = int_info.objects.filter(function_tags=[inp['main_tag'],inp['side_tag']]).values_list('create_time', 'function_name', 'function_description', 'function_input', 'function_function', 'function_tags')
    result_list = [list(row) for row in queryset]
    # Convert the queryset into a 2D list
    inp['data_read']=result_list
    return inp
def deleter(inp):
    int_info.objects.filter(function_name=inp['delete_name']).delete()
    return inp
def tag_loader(inp):
    main = tag.objects.filter(points='1').values_list('name', flat=True)
    side = tag.objects.filter(points='2').values_list('name', flat=True)
    main=list(main)
    side=list(side)
    # Convert the queryset into a 2D list
    inp['main']=main
    inp['side']=side
    return inp
function_list={'data_sender':data_sender,'data_saver':data_saver, 'func_do':func_do, 'deleter':deleter, 'registrator':registrator, 'tag_loader':tag_loader}
def handle_request(request):
    if request.method == 'POST':
        try:
            # Get data from the POST request
            data = json.loads(request.body.decode('utf-8'))

            # Your processing logic here
            # ...

            # Return a JSON response
            response_data = {'status': 'success', 'message': 'Data received successfully', 'n':data}
            return JsonResponse(function_list[data['func']](data['data']))
        except Exception as e:
            # Log the exception for debugging
            print('Error:', e)
            return JsonResponse({'status': 'error', 'message': 'Internal Server Error'})
    else:
        # Handle other HTTP methods if needed
        return JsonResponse({'status': 'error', 'message': 'Invalid HTTP method'})
data = int_info.objects.all()
diction={'int':data}
def add_data(request):
    if list(users.objects.filter(email_address=request.session['user_data']))!=[]:
        return render(request, 'news/kek.html')
def signup(request):
    return render(request, 'news/cotolog.html')
def main_page(request):
    x = unquote(request.GET.get('x', ''))
    if x!='':
        request.session['user_data'] = x
    return render(request, 'news/main.html', {'email':x})

def login(request):
    if list(users.objects.filter(email_address=request.session['user_data']))!=[]:
        return render(request, 'news/login.html')
def index(request):
    if list(users.objects.filter(email_address=request.session['user_data']))!=[]:
        return render(request, 'news/information.html')
