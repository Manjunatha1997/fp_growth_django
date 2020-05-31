from django.contrib import messages
from django.shortcuts import render, redirect
from app.models import *
from app.forms import *
import pyfpgrowth
# Create your views here.

def data_set():
    fr = open('transactions.csv')
    dataset = []
    for i in fr:
        i = i.strip()
        dataset.append(i.split(','))

    return dataset
    fr.close()


def index(request):
    return render(request,'index.html')

def addTransactions(request):
    if request.method == 'GET':
        row = ""
        fw = open('transactions.csv', 'a')
        for item in request.GET:
            row = row +item+","
        row = row[:-1]
        if row:
            fw.write(row+"\n")
            messages.info(request,"transaction successfull")
            return redirect('/addTransactions')
        fw.close()
    return render(request,'addTransactions.html')

def viewTransactions(request):
    data = data_set()

    # data = [['chicken', 'eggs', 'oil'],
    #         ['eggs', 'masala'],
    #         ['eggs', 'ginger'],
    #         ['chicken', 'eggs', 'masala'],
    #         ['chicken', 'ginger'],
    #         ['eggs', 'ginger'],
    #         ['chicken', 'ginger'],
    #         ['chicken','eggs', 'ginger', 'oil'],
    #         ['chicken', 'eggs', 'ginger']]
    #

    return render(request,'viewTransactions.html',{'data':data})

def frequentItems(request):
    data = data_set()
    # data = [['chicken', 'eggs', 'oil'],
    #         ['eggs', 'masala'],
    #         ['eggs', 'ginger'],
    #         ['chicken', 'eggs', 'masala'],
    #         ['chicken', 'ginger'],
    #         ['eggs', 'ginger'],
    #         ['chicken', 'ginger'],
    #         ['chicken', 'eggs', 'ginger', 'oil'],
    #         ['chicken', 'eggs', 'ginger']]


    patterns = pyfpgrowth.find_frequent_patterns(data,2)

    return render(request,'frequentItems.html',{'data':data,'patterns':patterns})

def rules(request):
    data = data_set()
    # data = [['chicken', 'eggs', 'oil'],
    #         ['eggs', 'masala'],
    #         ['eggs', 'ginger'],
    #         ['chicken', 'eggs', 'masala'],
    #         ['chicken', 'ginger'],
    #         ['eggs', 'ginger'],
    #         ['chicken', 'ginger'],
    #         ['chicken', 'eggs', 'ginger', 'oil'],
    #         ['chicken', 'eggs', 'ginger']]

    patterns = pyfpgrowth.find_frequent_patterns(data, 2)
    rules = pyfpgrowth.generate_association_rules(patterns, 1)
    print(rules)
    return render(request,'rules.html',{'rules':rules})

def document(request):
    return render(request,'document.html')