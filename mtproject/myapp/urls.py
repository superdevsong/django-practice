

from django.urls import path, include
from myapp import views # 사용자 정의 모듈 어떻게 Import하는지 알아보기

urlpatterns = [#''url요청시 위임받은 app 
    path('',views.index),#views파일에 정의한 반환값을 보내는것인데 다음과 같은 문법이 성립될려면 함수가 1급객체여야됨 알아보기
    path('create/',views.create),
    path('read/<id>',views.read),
    path('delete/',views.delete),
    path('update/<id>/',views.update),
    path('comment/create/',views.commentCreate)
]
