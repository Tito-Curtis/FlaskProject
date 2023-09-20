from market import db,app

class User(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    username=db.Column(db.String(40),nullable=False, unique=True)
    email_address=db.Column(db.String(60), nullable=False, unique=True) 
    password_hash=db.Column(db.String(60))
    budget=db.Column(db.Integer,nullable=False, default=1000)
    items=db.relationship('Item',backref='owned_user',lazy=True)

    def __init__(self,username,email_address,password_hash):
        self.username = username
        self.email_address = email_address
        self.password_hash = password_hash
     

    def __repr__(self):
        return (f'{self.username}')



class Item(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String(30),nullable=False)  
    price=db.Column(db.Integer,nullable=False)
    barcode=db.Column(db.String(12),nullable=False)
    description=db.Column(db.String(100),nullable=False,unique=True)
    owner = db.Column(db.Integer(), db.ForeignKey('user.id'))
  
    def __init__(self,name,price,barcode,description):
        self.name=name
        self.price=price
        self.barcode=barcode
        self.description=description
        
   

    def __repr__(self):
        return f'name: {self.name}'

with app.app_context():
    db.create_all()
    #db.drop_all()

with app.app_context():
    user1=User.query.filter_by(username='Curtis Baidoo').first()
    user2=User.query.filter_by(username='Fredrick Asamoah').first()
    user3=User.query.filter_by(username='Solomon Gyan').first()
    user4=User.query.filter_by(username='Benedict Mensah').first()

    if not user1:
        user1 = User('Curtis Baidoo','jnrCurtis75@gmail.com','tiscuritocurtis10')
        db.session.add(user1)
    if not user2:
        user2 = User('Fredrick Asamoah','fredrick84@gmail.com','divisive2200')
        db.session.add(user2)

    if not user3:
        user3 = User('Solomon Gyan','solly10_@gmail.com','solly10_')
        db.session.add(user3)

    
    if not user4:
        user4 = User('Benedict Mensah','billygoat@gmail.com','billy1212')
        db.session.add(user4)

    db.session.commit()
    db.session.close()



with app.app_context():
    Item1=Item.query.filter_by(name='Itel').first()
    Item2=Item.query.filter_by(name='Samsung A13s').first()
    Item3=Item.query.filter_by(name='Hp Laptop').first()
    Item4=Item.query.filter_by(name='Iphone x').first()
    Item1.owner = User.query.filter_by(username='Curtis Baidoo').first().id
    Item2.owner = User.query.filter_by(username='Fredrick Asamoah').first().id
    Item3.owner = User.query.filter_by(username='Solomon Gyan').first().id
    Item4.owner = User.query.filter_by(username='Benedict Mensah').first().id
    if not Item1:
        Item1=Item('Itel', 2000,'993216299897','2020 model')

        db.session.add(Item1)
    
    if not Item2:

        Item2=Item('Samsung A13s',1400,'123915473165','super strong')
        db.session.add(Item2)

    if not Item3:
        Item3=Item('Hp Laptop',6900,'231905128446','high quality')
        db.session.add(Item3)

    if not Item4:
        Item4=Item('Iphone x', 7100,'111000111000','high picture quality')
        db.session.add(Item4)


    db.session.commit()
    db.session.close()


  
