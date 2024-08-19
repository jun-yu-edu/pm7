from django.http import HttpResponse, JsonResponse
# Create your views here.

def data(request):
    return HttpResponse("안녕하세요!")

def json_data(request):
    data = {"name": "Jun", "age": 17, "city": "Seoul"}
    return JsonResponse(data)

def hello(request):
    return HttpResponse("안녕 덥다")

def random_data(request, num):
    data = {
        'my_num' : num
    }
    return JsonResponse(data)

def hello_name(request, name):
    return HttpResponse(f'안녕 {name}')