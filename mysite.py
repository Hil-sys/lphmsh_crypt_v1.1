# за костыльный код отвечает он
# url='https://github.com/Hil-sys'
# author этой гениальной идеи:
# https://github.com/AI1OGUS

from flask import *

base, chisla = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя', '1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33'
basem, chislam = list(base), chisla.split()
u = 0
j = 0

dic = []
for i in range(len(chislam)):
    chislam[i] = int(chislam[i])
    dic.append((basem[i], chislam[i]))


def graphs1(text, base):
    s = []
    for i in range(1, 34):
        s.append((base[i - 1], text.count(base[i - 1])))
    return s

def ras1(text, a, b):
    b = b.upper()
    for i in text:
        if i == a:
            text = text.replace(i, b)
    return text

def ras2(text, c, a, b):
    global dic, base
    ac = 0
    text_str = ''

    if a != '':
        ac = dic[base.find(a)][1]
    
    b -= 1
    KR = list(text.replace(' ', ''))
    
    for i in range(len(KR)):
        l = base.find(KR[i])
        KR[i] = dic[l][1]
    
    for i in range(len(KR)):
        if i % c == b:
            KR[i] = (ac + KR[i]) % 33
    
    for i in range(len(KR)):
        KR[i] = dic[KR[i] - 1][0]
    
    for i in range(len(KR)):
        text_str += KR[i]

    return text_str

def ras3(text):
    a  = text.split()
    c = int(a[0])
    d = int(a[1])
    n = int(a[2])
    m = 1
    for i in range(d):
        m *= c
        if m > n:
            m = m % n
    return m


def bubble_sort(nums):
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(nums) - 1):
            if nums[i][1] < nums[i + 1][1]:
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
                swapped = True

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route('/not', methods=['GET', 'POST'])
def my_form_post():
    global text, base_1
    base_old = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
    base_1 = base_old
    text = request.form['text']
    max_l = len(text)
    select = request.form.get('checked')

    if select != 3:
        s1 = graphs1(text, base_old)
        bubble_sort(s1)
    else:
        s1 = ''

    if select == '0':
        return render_template('index_ras1_1.html', text=text, dictc=s1, gg=text)
    elif select == '1':
        return render_template('index_ras2_1.html', text=text, dictc=s1, max_l=max_l, gg=text)
    else:
        text = str(ras3(text))
        if len(text) > 15:
            return render_template('index_endlong.html', text=text)
        else:
            return render_template('index_endshort.html', text=text)

# RAS1
@app.route('/ras1', methods=['GET', 'POST'])
def perevod_b1():
    global base_1
    
    if request.method == 'POST':
        if request.form.get('action1') == 'Отменить действие':
            comeback = str(request.form['cb'])
            b = comeback[-1]
            a = comeback[-2]
            comeback = comeback[:-2]

            text_old = request.form['text_old']
            text = request.form['text_new']

            text = text.replace(b.upper(), a)

            base_1 = base_1.replace(b.upper(), a)
            s1 = graphs1(text, base_1)
            bubble_sort(s1)

            return render_template('index_ras1_2.html', text=text_old, dictc=s1, gg=text, cb=comeback)
        else:
            comeback = ''
            comeback += str(request.form['cb'])
            a = request.form['now']
            b = request.form['after']
            text_old = request.form['text_old']
            text = request.form['text_new']

            comeback += str(a)
            comeback += str(b)
            text = ras1(text, a, b)

            base_1 = base_1.replace(a, b.upper())
            s1 = graphs1(text, base_1)
            bubble_sort(s1)

            return render_template('index_ras1_2.html', text=text_old, dictc=s1, gg=text, a=a, b=b, cb=comeback)

# RAS2
@app.route('/ras2_1', methods=['POST'])
def perevod_b2():
    c = request.form['len']
    text_old = request.form['text_old']
    iz = 'Пустенько :('
    
    return render_template('index_ras2_2_empty.html', text=text_old, gg=iz, gg1=text_old, c=c)

@app.route('/ras2_2', methods=['POST'])
def perevod_b3():
    text_old = request.form['text_old']
    text = request.form['text_new']
    c = request.form['c']
    u = request.form['letter']
    j = request.form['pos']

    text = ras2(text, int(c), u, int(j))

    return render_template('index_ras2_2.html', gg1=text, text=text_old, c=c)
    
#endfile
@app.route('/end', methods=['POST'])
def end():
    text = request.form['text_new']

    if len(text) > 15:
        return render_template('index_endlong.html', text=text)
    else:
        return render_template('index_endshort.html', text=text)







    # Для закодирования текста шифром виженера
    # k = ''
    # base = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
    # shifr = 'бвгдеёжзийклмнопрстуфхцчшщъыьэюяа'
    # shfg =
    # for i in range(len(text)):
    #     c = base.find(text[i])
    #     k += shifr[c]
    #
    # for i in k:
    #     if base.count(i) == 0:
    #         k = k.replace(i, '')

