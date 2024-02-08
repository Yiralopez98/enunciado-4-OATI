from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from tutoria import Base, Tutorial, Tag, TutorialTag 

# Crear el motor de la base de datos
engine = create_engine('mysql://usuario:contraseña@localhost/tutoria_db')

# Crear todas las tablas en la base de datos
Base.metadata.create_all(engine)

# Crear una sesión
Session = sessionmaker(bind=engine)
session = Session()

# Ejemplo de cómo agregar datos a la base de datos
tutorial1 = Tutorial(title='Tutorial 1', description='Descripción del tutorial 1', published=True, long_description='Descripción larga del tutorial 1')
tutorial2 = Tutorial(title='Tutorial 2', description='Descripción del tutorial 2', published=False, long_description='Descripción larga del tutorial 2')

tag1 = Tag(name='Python')
tag2 = Tag(name='SQL')

tutorial_tag1 = TutorialTag(tutorial=tutorial1, tag=tag1)
tutorial_tag2 = TutorialTag(tutorial=tutorial2, tag=tag1)
tutorial_tag3 = TutorialTag(tutorial=tutorial2, tag=tag2)

session.add_all([tutorial1, tutorial2, tag1, tag2, tutorial_tag1, tutorial_tag2, tutorial_tag3])
session.commit()

# Ejemplo de cómo consultar datos en la base de datos
print("Tutoriales:")
for tutorial in session.query(Tutorial).all():
    print(f"ID: {tutorial.id}, Título: {tutorial.title}, Publicado: {tutorial.published}")

print("\nTags:")
for tag in session.query(Tag).all():
    print(f"ID: {tag.id}, Nombre: {tag.name}")

# Cerrar la sesión
session.close()
