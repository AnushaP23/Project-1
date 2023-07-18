import random
from django.shortcuts import render
from markdown2 import Markdown
from encyclopedia import util

def convert_to_html(title):
    content = util.get_entry(title)
    markdowner = Markdown()
    if content == None:
        return None
    else:
        return markdowner.convert(content)

def index_page(request):
    entries = util.list_entries()
    css_file = util.get_entry("CSS")
    coffee = util.get_entry("coffee")
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def entry_page(request, title):
    html_content = convert_to_html(title)
    if html_content == None:
        return render(request,"encyclopedia/error_page.html",{
            "message": "This entry does not exist"
        })
    else:
        return render(request,"encyclopedia/entry_page.html",{
            "title": title,
            "content": html_content
        })

def search_page(request):
    if request.method == "POST":
        search_entry= request.POST['q']
        content = convert_to_html(search_entry)
        if content is not None:
            return render(request,"encyclopedia/entry_page.html",{
                "title": search_entry,
                "content": content
            })
        else :
            allEntries = util.list_entries()
            recommendations = []
            for entry in allEntries:
                if search_entry.lower() in entry.lower():
                    recommendations.append(entry)
            return render(request,"encyclopedia/search_page.html",{
                "recommendations": recommendations
            })        
        
def create_new_page(request):
    if request.method == "GET":
        return render(request,"encyclopedia/create_new_page.html")
    else:
        title = request.POST["title"]
        content = request.POST["content"]
        title_Exists = util.get_entry(title)
        if title_Exists is not None:
            return render(request,"encyclopedia/error_page.html",{
                "message": "Entry page already exists"
            })
        else:
            util.save_entry(title,content)
            html_content = convert_to_html(title)
            return render(request,"encyclopedia/entry_page.html",{
                "title": title,
                "content": html_content
            })

def edit_bar(request):
    if request.method == "POST":
        title = request.POST['entry_title']
        content = util.get_entry(title)
        return render(request,"encyclopedia/edit_page.html",{
            "title": title,
            "content": content
        })

def save_the_edit(request):
    if request.method == "POST":
        title = request.POST["title"] 
        content = request.POST["content"] 
        util.save_entry(title,content)
        html_content = convert_to_html(title)
        return render(request,"encyclopedia/entry_page.html",{
            "title": title,
            "content": html_content
        })

def rand_page(request):
        allEntries = util.list_entries()
        rand_entry = random.choice(allEntries)
        html_content = convert_to_html(rand_entry)
        return render(request,"encyclopedia/rand_page.html",{
            "title": rand_entry,
            "content": html_content
        })

    
      





