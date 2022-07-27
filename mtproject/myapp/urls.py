

from django.urls import path, include
from myapp import views # 사용자 정의 모듈 어떻게 Import하는지 알아보기

urlpatterns = [#''url요청시 위임받은 app 
    path('',views.index),#iews파일에 정의한 반환값
    path('read/<id>',views.read),
    path('delete/',views.delete),
    path('update/<id>/',views.update),
    path('create/',views.create),
    path('comment/create/',views.commentCreate)
]
