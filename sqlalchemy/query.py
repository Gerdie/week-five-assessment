"""

This file is the place to write solutions for the
skills assignment called skills-sqlalchemy. Remember to
consult the exercise directions for more complete
explanations of the assignment.

All classes from model.py are being imported for you
here, so feel free to refer to classes without the
[model.]User prefix.

"""

from model import *

init_app()

# -------------------------------------------------------------------
# Part 2: Write queries


# Get the brand with the **id** of 8.

Brand.query.get(8)

# Get all models with the **name** Corvette and the **brand_name** Chevrolet.

Model.query.filter(Model.name == 'Corvette', Model.brand_name == 'Chevrolet').all()

# Get all models that are older than 1960.

Model.query.filter(Model.year < 1960).all()

# Get all brands that were founded after 1920.

Brand.query.filter(Brand.founded > 1920).all()

# Get all models with names that begin with "Cor".

Model.query.filter(Model.name.like('Cor%')).all()

# Get all brands that were founded in 1903 and that are not yet discontinued.

db.session.query(Brand).filter(Brand.founded == 1903, Brand.discontinued == None).all()

# Get all brands that are either 1) discontinued (at any time) or 2) founded
# before 1950.

db.session.query(Brand).filter((Brand.discontinued != None) | (Brand.founded < 1950)).all()

# Get all models whose brand_name is not Chevrolet.

db.session.query(Model).filter(Model.brand_name != 'Chevrolet').all()

# Fill in the following functions. (See directions for more info.)


def get_model_info(year):
    '''Takes in a year, and prints out each model, brand_name, and brand
    headquarters for that year using only ONE database query.'''

    cars = db.session.query(Model.name, Model.brand_name, Brand.headquarters).join(Brand, Model.brand_name==Brand.name).filter(Model.year == 1949).all()

    for car in cars:
        print car[0], car[1], car[2]


def get_brands_summary():
    '''Prints out each brand name, and each model name for that brand
     using only ONE database query.'''

    cars = db.session.query(Model.brand_name, Model.name).distinct().all()

    for car in cars:
        print car[0], car[1]

# -------------------------------------------------------------------
# Part 2.5: Discussion Questions (Include your answers as comments.)

# 1. What is the returned value and datatype of
# ``Brand.query.filter_by(name='Ford')``?

"""That is a SQLAlchemy query object. It contains the content of the query
SELECT * FROM brands WHERE name='Ford' ... The results of that query can be
accessed by calling the .all(), .first() or .one() methods on the query object."""

# 2. In your own words, what is an association table, and what *type* of
# relationship does an association table manage?

"""An association table is built to manage a many-to-many relationship. It is
used exclusively to relate 2 other tables to each other. If I have a database of
pets and their owners, but humans Sonya and John have joint ownership of their 2
dogs Barky and BarkyLouder, then we might have a 'dogs' table and an 'owners' table, but we would need
an association table to relate Sonya to Barky, and Sonya to BarkyLouder, and John to Barky,
and John to BarkyLouder. Aside from the pet id and the owner id and the association table's
primary key id, the associate table would have no other fields."""

# -------------------------------------------------------------------
# Part 3


def search_brands_by_name(mystr):
    """takes in any string as parameter, and returns a list of objects 
    that are brands whose name contains or is equal to the input string. """

    return db.session.query(Brand).filter(Brand.name.like('%{}%'.format(mystr))).all()


def get_models_between(start_year, end_year):
    """takes in a start year and end year (two integers), and returns a list of 
    objects that are models with years that fall between the start year (inclusive) 
    and end year (exclusive)"""

    return db.session.query(Model).filter(Model.year in range(start_year, end_year)).all()
