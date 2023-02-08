# Create your views here.
# request -> response
# request handler
from django.db import transaction, connection
from django.db.models import Count, ExpressionWrapper, DecimalField, F
from django.shortcuts import render
from django.contrib.contenttypes.models import ContentType

from store.models import Customer, Product, Collection, Order, OrderItem
from tags.models import TaggedItem


@transaction.atomic()
def say_hello(request):
    # OR statement, use ~ for negation
    # query_set = Product.objects.filter(Q(inventory__lt=10) | Q(unit_price__lt=20))
    # query_set = Product.objects.filter(inventory__lt=10, unit_price__lt=20)
    # query_set = Product.objects.filter(inventory__lt=10).filter(unit_price__lt=20)

    # --------------------------
    # inventory = price
    # query_set = Product.objects.filter(inventory=F('unit_price'))
    # --------------------------
    # Sorting
    # query_set = Product.objects.order_by('title')
    # query_set = Product.objects.order_by('title') # Use earliest() to get the 1st item after sorting
    # query_set = Product.objects.order_by('unit_price', 'title') # Multiple sort order
    # query_set = Product.objects.order_by('-title') # DESC order

    # ---------------------------------
    # Get 5 products
    # query_set = Product.objects.all()[:5]

    # -------------------
    # Get some columns only
    # values for dictionary, values_list for a tuple
    # query_set = Product.objects.values_list('id', 'title', 'collection__title')

    # ---------------------
    # query_set = Product.objects.filter(id__in=OrderItem.objects.values('product_id').distinct()).order_by('title')
    # query_set = OrderItem.objects.values('product_id').distinct()

    # ---------
    # only get instance of product instead of dictionary
    # must be careful as many queries may go into database if we are not careful
    # query_set = Product.objects.only('id', 'title')
    #
    # query_set = Product.objects.defer('id', 'title')

    # ------------------
    # create a join with collection table
    # selected_related (1) items
    # prefetch_related (n) items
    # query_set = Product.objects.select_related('collection').all()

    # -------------------
    # get aggregated values
    # query_set = Product.objects.aggregate(count=Count('id'), min_price=Min('unit_price'))

    # ------------------------
    # annotate
    # query_set = Customer.objects.annotate(is_new=Value(True))
    # query_set = Customer.objects.annotate(new_id=F('id') + 1)

    # query_set = Customer.objects.annotate(
    #     orders_count=Count('order')
    # )

    # Expression Wrapper
    # discounted_price = ExpressionWrapper(F('unit_price') * 0.8, output_field=DecimalField())
    # query_set = Product.objects.annotate(
    #     discounted_price=discounted_price
    # )

    # ----------------------
    # Django database functions
    # query_set = Customer.objects.annotate(
    #     full_name=Func(F('first_name'), Value(' '), F('last_name'), function='CONCAT')
    # )
    #
    # query_set = Customer.objects.annotate(
    #     full_name=Concat('first_name', Value(' ') , 'last_name')
    # )

    # ---------------------------
    # content type id for dynamic loading of models
    # content_type = ContentType.objects.get_for_model(Product)
    #
    # query_set = TaggedItem.objects.select_related('tag').filter(
    #     content_type=content_type,
    #     object_id=1
    # )

    # query_set = TaggedItem.objects.get_tags_for(Product, 1)

    # Insert record into tables
    # collection = Collection.objects.get(pk=11)
    # collection = Collection(title='Video Games') another way of creating an object
    # collection = Collection.objects.create(name='a', featured_product_id=1)
    # collection.title = 'Games'
    # collection.featured_product = None  # 1 way of adding
    # collection.featured_product_id = 1  # 2nd way of adding
    # collection.save()

    # Collection.objects.filter(pk=11).update(featured_product=None)

    # Deleting objects
    # collection = Collection(pk=11)
    # collection.delete()
    # collection.objects.filter(id__gt=5).delete()

    # ----------------------
    # Transaction to prevent inconsistency within tables in a database
    # with transaction.atomic():
    #     order = Order()
    #     order.customer_id = 1
    #     order.save()
    #
    #     item = OrderItem()
    #     item.order = order
    #     item.product_id = 1
    #     item.quantity = 1
    #     item.unit_price = 10
    #     item.save()

    # -----------------------
    # Executing raw SQL queries
    # queryset = Product.objects.raw('SELECT * FROM store_product')
    # with connection.cursor() as cursor:
    #     cursor.execute()
    #     cursor.callproc('get_customers', [1, 2, 'a'])

    return render(request, 'hello.html', {'name': 'Jonathan'})
