from basic import db, Puppy 

#####CREATE#####

tom = Puppy('Tom', 5) 
db.session.add(tom) 
db.session.commit()

#####READ#####

all_puppies = Puppy.query.all() 
print(all_puppies)


####SELECT By ID#####
puppy1 = Puppy.query.get(1) 
print(puppy1.name)


#####FILTERS#####
puppy_tom = Puppy.query.filter_by(name = 'Tom') 
print(puppy_tom.all())


#####UPDATE######
puppy1 = Puppy.query.get(1) 
puppy1.age = 10 
db.session.add(puppy1) 
db.session.commit()



#####DELETE#####
puppy2 = Puppy.query.get(2) 
db.session.delete(puppy2) 
db.session.commit()


#####PRINT####
all_puppies = Puppy.query.all() 
print(all_puppies)
