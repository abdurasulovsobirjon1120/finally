from django.shortcuts import redirect


"""
decoratirlar vazifasi : misol uchun turli xil rolli insonlarni boshqa boshqa page ga o'tqazish kerak bo'ladi .
accountni account page ga , boshliqni boshliqga , menejerni menejerga . Aynan shu vazifalar uchun kerak bo'ladi.
Bundan tashqari bu decoratorni xoxlagan maqsadda ishlatish mumkin . xoxlagan redirect qilish operatsiyalarida
"""
def authenticated(my_view):
    def wrapper (request ,*args, **kwargs):
        if request.user.is_authenticated:
            return redirect('maqola')
        else: return my_view (request, *args, **kwargs)

    return wrapper
