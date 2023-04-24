from flask import Flask, render_template,request,redirect,url_for,session,abort

from .session_interface import MySessionInterface

app = Flask(__name__)
app.secret_key = b'v8Iagb'
app.session_interface = MySessionInterface()
def get_current_username():
   username = ""
   login_auth = False
   if 'username' in session:
      username = session['username'] #her sayfaya aynı kodların yazılmaması için bir fonksiyona tanımlanır ve sayfalarda bu fonksiyon çağırılır.
      login_auth = True  # İşlemin doğru veya yanlış bir şekilde gerçekleştiğini ifade eder. Ve bu işlemi tüm sayfalara ekleyebileceğimiz fonksiyon
   return username,login_auth

@app.route("/")
def Index():
   username, login_auth = get_current_username()
   return render_template("index.html",username=username,login_auth=login_auth)

@app.route("/about.html")
def About():
   username, login_auth = get_current_username() #bütün sayfalara girişin doğru bir şekilde yapıldığını sağlayan fonksiyon eklenir.
   return render_template("about.html",username=username,login_auth=login_auth)

@app.route("/contact.html")
def Contact():
   username, login_auth = get_current_username()
   return render_template("contact.html",username=username,login_auth=login_auth)

@app.route("/index.html")

def Home():
   username, login_auth = get_current_username()
   return render_template("index.html", username=username, login_auth=login_auth)

@app.route("/news.html")
def ContactList():
   username, login_auth = get_current_username()
   return render_template("news.html",username=username,login_auth=login_auth)

@app.route("/menu.html",methods=['GET','POST'])

def Login():
   if request.method == 'POST':
      # istek yapılacağı için post metodu fonksiyona eklenir
      if request.form:
         if 'username' in request.form and 'password' in request.form:
            username = request.form['username']
            password = request.form['password'] #password ve email fonksiyon olarak getirilir
            if username == 'admin@admin.com' and password == 'admin':
               session['username'] = username
               return redirect(url_for('Index')) #girilen parametreler birbirine eşit ise index.html sayfasına yönlendirilir
            else:
               return redirect(url_for('Login'))#şifre veya kullanıcı adı hatalıysa tekrar login sayfasına yönlendirilir.
      abort(400)#hata rapor mesajı
   username, login_auth = get_current_username()
   return render_template("menu.html",username = username,login_auth=login_auth)