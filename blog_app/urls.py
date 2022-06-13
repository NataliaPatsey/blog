from blog_app.views import index, contact,get_item_category,get_item_all,\
    get_my_items, get_item_one,add_item,RegisterFormView, LoginFormView,LogoutView, update_item,\
    delete_item, search,like,dislike,unlike, add_to_list,get_my_lists,delete_from_list,drop_from_list,do_list,\
    get_past_list, adm_get_group,adm_compound_group,adm_add_to_group,adm_del_from_group,adm_edit_category,\
    adm_get_category, adm_del_category,adm_add_category

from django.urls import path

urlpatterns = [
    path('', index, name='index'),
    path('contact/', contact, name='contact'),
    path('all/', get_item_all, name='get_item_all'),
    path('category/<int:id>/', get_item_category, name='get_item_category'),
    path('article/<int:id>/', get_item_one, name='get_item_one'),
    path('editarticle/<int:id>/', update_item, name='update_item'),
    path('delarticles/<int:id>/', delete_item, name='delete_item'),
    path('addarticle/', add_item, name='add_item'),
    path('myarticles/', get_my_items, name='get_my_items'),
    path('search/', search, name='search'),
    path('like/<int:id>', like, name='like'),
    path('unlike/<int:id>', unlike, name='unlike'),
    path('dislike/<int:id>', dislike, name='dislike'),
    path('addtolist/<int:id>', add_to_list, name='add_to_list'),
    path('deletefromlist/<int:id>', delete_from_list, name='delete_from_list'),
    path('dropfromlist/<int:id>', drop_from_list, name='drop_from_list'),

    path('dolist/', do_list, name='do_list'),
    path('getpastlist/<int:id>', get_past_list, name='get_past_list'),
    path('getmylists/', get_my_lists, name='get_my_lists'),

    path('admingroup', adm_get_group,name='adm_get_group'),
    path('admincompoundgroup/<int:id>', adm_compound_group,name='adm_compound_group'),
    path('admaddtogroup/<int:group_id>/<int:user_id>', adm_add_to_group,name='adm_add_to_group'),
    path('admdelfromgroup/<int:group_id>/<int:user_id>', adm_del_from_group,name='adm_del_from_group'),

    path('getcategory/', adm_get_category, name='adm_get_category'),
    path('editcategory/<int:id>', adm_edit_category, name='adm_edit_category'),
    path('delcategory/<int:id>', adm_del_category, name='adm_del_category'),
    path('addcategory/', adm_add_category, name='adm_add_category'),

    path('registration/', RegisterFormView.as_view(), name='registration'),
    path('login/', LoginFormView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),

]







