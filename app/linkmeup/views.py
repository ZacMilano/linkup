from django.http import HttpResponse

def hello_world(request):
  print(type(request))
  return HttpResponse("Hello, world. You're at the index.")
