from django.shortcuts import render, redirect
from .models import User_account
from .forms import UserForm

# Create your views here.


def login(request):
    if request.session.get('is_login', None):  # 檢查session確定是否登入，不允許重複登入
        return redirect("/index/")  # 若已登入則導向主頁
    if request.method == 'POST':  # 接收POST訊息，若無則讓返回空表單
        login_form = UserForm(request.POST)  # 導入表單模型
        if login_form.is_valid():  # 驗證表單
            # 從表單的cleaned_data中獲得具體值
            username = login_form.cleaned_data['username']
            password = login_form.cleaned_data['password']
            try:
                user = User_account.objects.get(user_name=username)
                if user.password == password:  # 密文處理
                    # 使用session寫入登入者資料
                    request.session['is_login'] = True
                    request.session['user_id'] = user.user_id
                    request.session['user_name'] = user.user_name
                    message = "登入成功"
                    return redirect('/index/')
                else:
                    message = "帳密錯誤"
            except:
                message = "帳密錯誤"
    login_form = UserForm(request.POST)  # 返回空表單
    return render(request, "login.html", locals())


def logout(request):
    if not request.session.get('is_login', None):  # 如果原本未登入，就不需要登出
        return redirect('/index/')
    request.session.flush()  # 一次性將session內容全部清除
    return redirect('/index/')


def home(request):
    return render(request, "index.html")
