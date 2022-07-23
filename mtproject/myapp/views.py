from enum import auto
from django.http import HttpResponse
from django.shortcuts import render,HttpResponse,redirect
from django.views.decorators.csrf import csrf_exempt
from myapp.models import Board
from myapp.models import Comment


boards = Board.objects.values()

# 템플릿
def HTMLTemplate(articleTag, id=None):
    global boards
    contextUI = ''
    commentUI = ''
    if id != None:
        contextUI = f'''
            <li>
                <form action="/delete/" method="post">
                    <input type="hidden" name="id" value={id}>
                    <input type="submit" value="delete">
                </form>
            </li>
            <li><a href="/update/{id}">update</a></li>
        '''
        
        commentUI = f'''
            -----댓글쓰기-----
         
                <form action="/comment/create/" method="post">
                <p><textarea name="comment" placeholder="comment"></textarea></p>
                    <input type="hidden" name="id" value={id}>
                    <input type="submit" value="create">
                </form>
            
           
        '''
        
    ol = ''
    for board in boards:
        ol += f'<li><a href="/read/{board["id"]}">{board["board_title"]}</a></li>'
    return f'''
    <html>
    <body>
        <h1><a href="/">Django</a></h1>
        <ul>
            {ol}
        </ul>
        {articleTag}
        {commentUI}
        <ul>
            <li><a href="/create/">create</a></li>
            {contextUI}
        </ul>
        
        
    </body>
    </html>
    '''
    
# Create your views here.
def index(request):
    article = '''
    <h2>Welcome</h2> 
    Hello, Django
    '''
   
    return HttpResponse(HTMLTemplate(article)) 

# =======board======
# 글 쓰기
@csrf_exempt
def create(request):
    global boards
    if request.method == 'GET':
        article = '''
            <form action="/create/" method="post">
                <p><input type="text" name="title" placeholder="title"></p>
                <p><textarea name="body" placeholder="body"></textarea></p>
                <p><input type="submit"></p>
            </form>
        '''
        return HttpResponse(HTMLTemplate(article))
    elif request.method == 'POST':
        board =  Board(board_title = request.POST['title'],board_text = request.POST['body'])#엔티티 생성
        board.save()#저장 
        url = '/read/'+str(board.id)
        boards = Board.objects.values()
        return redirect(url)
# 글 읽기
def read(request,id):
    article = ''
    board = Board.objects.get(id = int(id))
    comments = Comment.objects.filter(board=board)
    ol = "<ul>"
    for comment in comments:
        ol += f'댓글 : {comment.comment_text} <br> '
    ol+="</ul>"
    article = f'<h2>{board.board_title}</h2>{board.board_text}'+ol;
    return HttpResponse(HTMLTemplate(article, id))
# 글 삭제 
@csrf_exempt
def delete(request):
    global boards
    if request.method == 'POST':
        id = int(request.POST['id'])
        Board.objects.filter(id = int(id)).delete()
        boards = Board.objects.values()
        return redirect('/')
# 글 갱신
@csrf_exempt
def update(request,id):
    global boards
    if request.method == 'GET':
        board = Board.objects.get(id = int(id)) 
        article = f'''
            <form action="/update/{id}/" method="post">
                <p><input type="text" name="title" placeholder="title" value={board.board_title}></p>
                <p><textarea name="body" placeholder="body">{board.board_text}</textarea></p>
                <p><input type="submit"></p>
            </form>
        '''
        return HttpResponse(HTMLTemplate(article, id))
    elif request.method == 'POST':
        board = Board.objects.get(id = int(id)) 
        board.board_title = request.POST['title']
        board.board_text = request.POST['body']
        board.save()
        boards = Board.objects.values()
        return redirect(f'/read/{id}')
    
    
#=====Comment=====
@csrf_exempt
def commentCreate(request):
    global boards
    
    if request.method == 'POST':
        board = Board.objects.get(id = request.POST['id']) 
        comment =  Comment(comment_text = request.POST['comment'],board = board)#엔티티 생성
        comment.save()#저장 
        url = '/read/'+str(board.id)
        boards = Board.objects.values()
        return redirect(url)