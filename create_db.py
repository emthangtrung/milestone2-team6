from myapp import myapp_obj, db
from myapp.models import *

db.create_all()

print('Database created successfully!')
