from django.shortcuts import render

# Create your views here.

lst = [
	{'待办事项':'遛狗', '已完成':False},
	{'待办事项':'遛狗', '已完成':True},
]

key = [
	{'开关值':'off'},
]

def home(request):
	global lst
	if request.method == "POST":
		if request.POST['待办事项'] == '':
			return render(request,"todolist/home.html", {'警告': '请输入内容！'})
		else:
			lst.append({'待办事项': request.POST['待办事项'], '已完成':False})
			content = { '清单': lst}
			return render(request,"todolist/home.html", content)
	elif request.method == "GET":
		content = { '清单': lst}
		return render(request,"todolist/home.html", content)

def about(request):
	return render(request,"todolist/about.html")

def edit(request):
	return render(request,"todolist/edit.html")

def serchdata(request):
	content = { '开关值变动': key}
	return render(request,"todolist/serchdata.html", content)

def getdata(request):
	global key
	if request.method == "POST":
		if request.POST['开关值'] == 'on':
			key[0]['开关值'] = request.POST['开关值']
			content = { '开关值变动': key[0]['开关值']}
			return render(request,"todolist/getdata.html", content)
		else:
			key[0]['开关值'] = request.POST['开关值']
			content = { '开关值变动': key[0]['开关值']}
			return render(request,"todolist/getdata.html", content)
	elif request.method == "GET":
		content = { '开关值变动': key}
		return render(request,"todolist/getdata.html", content)