from django.urls import path
from diary import views

urlpatterns = [
    path('', views.NoteView.as_view(), name='note_view'),
    path('<int:note_id>', views.NoteView.as_view(), name='note_delete'),
    path('page/<int:note_id>', views.PageView.as_view(), name='all_page'),
    path('page/<int:photo_id>', views.DetailPhotoPageView.as_view(), name='detail_photo_page'),
    path('page/<int:plan_id>', views.DetailPlanPageView.as_view(), name='detail_plan_page'),
    path('page/<int:comment_id>', views.CommentView.as_view(), name='comment'),
    path('trash', views.Trash.as_view(), name='trash'),
    path('stamp', views.Stamp.as_view(), name='stamp'),
]