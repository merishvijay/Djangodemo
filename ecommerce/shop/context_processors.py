from shop.models import Category

def menu_links(requet):
    c=Category.objects.all()
    return{"links":c}