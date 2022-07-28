from enum import auto
from django.http import HttpResponse
from django.shortcuts import render,HttpResponse,redirect
from django.views.decorators.csrf import csrf_exempt
from myapp.models import Board
from myapp.models import Comment
from myapp.forms.boardform import BoardForm



boards = Board.objects.values()


    
# Create your views here.
def index(request):
    
    context = {"articletag" : "index","boards" : boards}
   
    return render(request,'myapp/index.html',context)

# =======board======
# 글 쓰기
@csrf_exempt
def create(request):
    global boards
    if request.method == 'GET':
        context = {"articletag" : "create","boards" : boards}
        return render(request,'myapp/index.html',context)
    elif request.method == 'POST':
        boardForm = BoardForm(request.POST)
        if(boardForm.is_valid()):
            board =  boardForm.save()#엔티티 생성 및 저장 
            url = '/read/'+str(board.id)
            boards = Board.objects.values()
            return redirect(url)
        else :
            context = {"articletag" : "create","boards" : boards,"boardForm": boardForm}
            return render(request,'myapp/index.html',context)
            
# 글 읽기
def read(request,id):
    article = ''
    board = Board.objects.get(id = int(id))
    comments = Comment.objects.filter(board=board)
    context = {"articletag" : "read","boards" : boards,"readBoard":board,"comments":comments}
    return render(request,'myapp/index.html',context)
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
        context = {"articletag" : "update","boards" : boards,"selectBoard":board}
        return render(request,'myapp/index.html',context)
    elif request.method == 'POST':
        board = Board.objects.get(id = int(id)) 
        boardForm = BoardForm(request.POST,instance = board)
        if(boardForm.is_valid()):
            updateBoard =  boardForm.save()#업데이트 내용 저장
            url = '/read/'+str(updateBoard.id)
            boards = Board.objects.values()
            return redirect(url)
        else :
            context = {"articletag" : "create","boards" : boards,"boardForm": boardForm}
            return render(request,'myapp/index.html',context)
    
    
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