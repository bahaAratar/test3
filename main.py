'''
ORM(Object Relational Mapping - обьектно реляционное отношение) - технология которая связывает БД с концепциями обьектно ориентированных языков прогрммирования. ORM - прослойка между БД и кодом который пишет программист, которая позволяет создавать в программе обьекты, обновлять, удалять и получать их

'''

# python:
    # peewee
    # sqlalchemy
    # DjabgoORM

# Класс - таблица БД
# Атрибут класса - поле БД
# Обьект класса - строка в таблице

import peewee
from peewee import PostgresqlDatabase as PDB
from datetime import datetime


db = PDB(
    'orm_py25',
    user = 'aratar',
    password = '1111',
    host = 'localhost',
    port = 5432
    )

class Category(peewee.Model):
    id = peewee.PrimaryKeyField()
    name = peewee.CharField(max_length=100, unique=True)
    created_at = peewee.DateTimeField(default=datetime.now)
    
    class Meta:
        database = db
        db_table = 'category'

class Product(peewee.Model):
    id = peewee.PrimaryKeyField()
    name = peewee.CharField(max_length=100)
    price = peewee.DecimalField(max_digits=10, decimal_places=2, default=10)
    amount = peewee.IntegerField(null=False)
    category = peewee.ForeignKeyField(Category, related_name='products', to_field='id', on_delete='cascade')
    
    class Meta:
        database = db
        db_table = 'product'


db.connect()
# Category.create_table()
# Product.create_table()

# category = Category(name='game')
# category.save()

def post_category(category_name):
    try:
        category = Category(name=category_name)
        category.save()
        print('Saved!!!')
    except peewee.IntegrityError:
        print('такая катергория уже существует')



def get_category():
    categories = Category.select()
    for cat in categories:
        print(f'{cat.id}) {cat.name} -- {cat.created_at}')

def delete(category_id):
    try:
        category = Category.get(id=category_id)
        category.delete_instance()
        print('категория удалена')
        get_category()
    except peewee.DoesNotExist:
        print('категории с таким id нет')

def update_category(category_id, new_name):
    category = Category.get(id=category_id)
    category.name = new_name
    category.save()
    print('категория обновлена')
    get_category()
    

def detail_category(id_category):
    category = Category.get()

# post_category('game3')
# post_category('game2')
get_category()
update_category(4, 'new_game4.2')
# delete(1)
# ":L>k,`1mjhngbvfcdxznm