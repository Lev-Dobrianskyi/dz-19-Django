from django.shortcuts import render, redirect
from datetime import datetime


def profile_view(request):
    current_time = datetime.now().strftime("%d.%m.%Y %H:%M:%S")

    last_visit = request.session.get('last_visit')

    request.session['last_visit'] = current_time

    if not last_visit:
        last_visit = "Це ваш перший візит!"

    if request.method == "POST":
        action = request.POST.get("action")
        if action == "save_name":
            name = request.POST.get("name", "").strip()
            if name:
                request.session['user_name'] = name
            return redirect('profile')

    user_name = request.session.get('user_name')

    context = {
        'user_name': user_name,
        'last_visit': last_visit,
        'current_theme': request.session.get('theme', 'light')  # За замовчуванням світла
    }
    return render(request, 'mycabinet/profile.html', context)


def tasks_view(request):
    tasks = request.session.get('tasks', [])

    if request.method == "POST":
        action = request.POST.get("action")
        if action == "add":
            task_text = request.POST.get("task", "").strip()
            if task_text:
                tasks.append(task_text)
                request.session['tasks'] = tasks
            return redirect('tasks')
        elif action == "remove":
            index = int(request.POST.get("index", "-1"))
            if 0 <= index < len(tasks):
                tasks.pop(index)
                request.session['tasks'] = tasks
            return redirect('tasks')

    context = {
        'tasks': tasks,
        'user_name': request.session.get('user_name'),
        'current_theme': request.session.get('theme', 'light')
    }
    return render(request, 'mycabinet/tasks.html', context)


def settings_view(request):
    if request.method == "POST":
        action = request.POST.get("action")

        if action == "change_theme":
            theme = request.POST.get("theme")
            if theme in ['light', 'dark']:
                request.session['theme'] = theme
            return redirect('settings')

        elif action == "remove_name":
            if 'user_name' in request.session:
                del request.session['user_name']
            return redirect('settings')

        elif action == "clear_tasks":
            request.session['tasks'] = []
            return redirect('settings')

        elif action == "clear_theme":
            if 'theme' in request.session:
                del request.session['theme']
            return redirect('settings')

    context = {
        'user_name': request.session.get('user_name'),
        'current_theme': request.session.get('theme', 'light')
    }
    return render(request, 'mycabinet/settings.html', context)

def testing_view(request): # typed by hand, manually😱 for practice🤯
    if request.method == "POST":
        action = request.POST.get("action")

        if action == "Test_stuff":
            test_stuff = request.POST.get("test_stuff", "").strip()
            if test_stuff:
                request.session['test_stuff'] = test_stuff
            return redirect('test')

        elif action == "deleteTest":
            if "test_stuff" in request.session:
                del request.session["test_stuff"]
            return redirect('test')

    test_stuff = request.session.get('test_stuff')
    return render(request, "mycabinet/testing.html", {"test_stuff": test_stuff})