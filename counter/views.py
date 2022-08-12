from pydoc import apropos
from django.shortcuts import render
import requests
# 
# Create your views here.
def home(request):
  import requests
  import json

  if request.method == 'POST':
    query = request.POST['query']
    api_url = 'https://api.api-ninjas.com/v1/nutrition?query='.format(query)
    api_request = requests.get(api_url + query, headers={'X-Api-Key': 'ltFvOHHfs2GsSCnKe8Pz+g==iOxbZjbwM4aupqnU'})
    try:
      api = json.loads(api_request.content)
      print(api_request.content)
    except Exception as e:
      api = "oops!"
      print(e)
    return render(request, 'home.html',{'api':api})
  else:
    return render(request, 'home.html',{'query': 'Enter a valid query'})
