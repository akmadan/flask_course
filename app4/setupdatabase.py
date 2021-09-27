from basic import db, Puppy

db.create_all() 

tuffy = Puppy('Tuffy', 3) 
sam = Puppy('Sam', 4)

print(sam.id) 
print(tuffy.id)

db.session.add_all([tuffy, sam])

db.session.commit()

print(sam.id) 
print(tuffy.id)
