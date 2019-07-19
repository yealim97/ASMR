from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import json
from django.views.generic import View

#from .models import Festival


# save data for web browser


save_data = []
dict1 = {}
dict2 = {}
dict3 = {}
empty_dict = {'title': '', 'start': '', 'finish': '', 'number': '', 'address': '', 'img': ''}


def post_list(request)    :
    return render(request, 'blog/post_list.html', {})


def httpres(request):
    return HttpResponse('OK')


def run(request):
    global dict1, dict2, dict3

    data = request.GET

    # replace data
    outer_data = ''
    for d in data:
        outer_data = d



    tmp_data = outer_data.split(" //// ")

    # split data
    replace_data_to_dict = []
    for tmp in tmp_data:

        replace_data_to_dict.append(tmp.replace("\'", "\""))


    # check list's length(festival number), and
    if len(replace_data_to_dict) == 3:

        d1, d2, d3 = replace_data_to_dict


        dict1 = json.loads(d1)
        dict2 = json.loads(d2)
        dict3 = json.loads(d3)

    elif len(replace_data_to_dict) == 2:

        d1, d2 = replace_data_to_dict
        dict1 = json.loads(d1)
        dict2 = json.loads(d2)

        # empty
        dict3 = empty_dict
    elif len(replace_data_to_dict) == 1:

        d1 = str(replace_data_to_dict)
        d1 = d1.replace('[\'', '').replace('\']', '')
        dict1 = json.loads(d1)

        dict2 = empty_dict
        dict3 = empty_dict
    else:
        dict1 = empty_dict
        dict2 = empty_dict
        dict3 = empty_dict


    return render(request, 'blog/post_list.html')


def Festivalget(request):
    global dict1, dict2, dict3

    data = {
        'title1': dict1['title'],
        'address1': dict1['address'],
        'img1': dict1['img'] + '&thumb',
        'title2': dict2['title'],
        'address2': dict2['address'],
        'img2': dict2['img'] + '&thumb',
        'title3': dict3['title'],
        'address3': dict3['address'],
        'img3': dict3['img'] + '&thumb',
    }

    return JsonResponse(data)

