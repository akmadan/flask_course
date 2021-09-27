from models import db, Puppy, Toy, Owner 

## Creating 2 Puppies

rufus = Puppy('Rufus') 
lido = Puppy('Lido') 

## Adding to DB

db.session.add_all([rufus, lido])
db.session.commit()

## Querying

print(Puppy.query.all())
rufus = Puppy.query.filter_by(name= "Rufus").first()
print(rufus)

## Creating an owner object
jade = Owner("Jade", rufus.id)

## Giving Rufus some toys 
toy1  = Toy('Chew Toy', rufus.id) 
toy2 = Toy('Cat', rufus.id)

db.session.add_all([jade, toy1, toy2]) 
db.session.commit()

## Printing Rufus now
rufus = Puppy.query.filter_by(name= "Rufus").first()
print(rufus)
print(rufus.report_toys())