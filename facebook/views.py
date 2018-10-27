from django.shortcuts import render, redirect
from facebook.models import Article, Comment

# Create your views here.
def play(request):
    return render(request, 'play.html')

count = 0
def play2(request):
    # 무언가 작업
    donghun = '양동훈'

    global count
    count = count + 1

    age = 15
    if age > 19:
        status = '성인'
    else:
        status = '미성년자'

    diary = ['날씨 맑았다 - 10월5일', '춥다 - 10월1일','덥다 - 9월3일']

    return render(request, 'play2.html', { 'name': donghun, 'count': count, 'status': status, 'diary':diary })

def profile(request):
    return render(request, 'profile.html')

count = 0
def event(request):

    name = '양동훈'

    global count
    count = count + 1
    if count == 7:
        asd = '당첨!'
    else:
        asd = '꽝..'

    age = 26
    if age > 20:
        status = '성인'
    else:
        status = '미성년자'


    return render(request, 'event.html', { 'name': name, 'count': count,'status':status, 'asd':asd})

def newsfeed(requeust):
    # db에서 글을 불러와소 newsfeed.html로 보내주자
    articles = Article.objects.all()

    return render(requeust, 'newsfeed.html', {'articles': articles})

def detail_feed(request, pk):
    # pk번 글을 불러오기
    article = Article.objects.get(pk=pk)
    if request.method == 'POST':
        Comment.objects.create(
            article = article,
            name = request.POST ['nickname'],
            text = request.POST['reply'],
            password = request.POST['password']
        )
    return render(request, 'detail_feed.html', { 'feed': article })

def new_feed(request):
    # 데이터베이스 저장하는 작업을하는 함수
    # 사용자가 게시버튼을 눌렀는가?
    if request.method == 'POST':
        # 글 저장
        new_article = Article.objects.create(
            author = request.POST['nickname'],
            title = request.POST['title'],
            text = request.POST['reply'] + ' - 추신 : 감사합니다.',
            password = request.POST['password']
        )
    return render(request, 'new_feed.html')

def edit_feed(request, pk):
    article = Article.objects.get(pk=pk)

    # 실제로 수정한 내용을 저장
    if request.method == 'POST': #수정버튼을 눌렀다
        if request.POST['password'] == article.password:
            article.title = request.POST['title']
            article.author = request.POST['author']
            article.text = request.POST['content']
            article.save()
        return redirect(f'/feed/{ pk }')
    else: #틀렸을 상황
        return  redirect('fail/')

    return render(request, 'edit_feed.html', { 'feed' : article })

def remove_feed(request, pk):
    article = Article.objects.get(pk=pk)
    # 삭제 로직
    if request.method == 'POST':
        # request.POST['password'] <--- 사용자가 입력한 비번
        # 진짜 비밀번호 --> article.password
        if request.POST['password'] == article.password:
            # 비밀번호가 일치하므로 삭제하기
            article.delete()

    return render(request, 'remove_feed.html', { 'feed' : article })
