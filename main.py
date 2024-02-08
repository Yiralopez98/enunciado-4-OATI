from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from tutoria import Base, Tutorial, Tag, TutorialTag  # Reemplaza "your_module_name" con el nombre de tu archivo .py que contiene las definiciones de las clases

# Crear el motor de la base de datos
engine = create_engine('sqlite:///tutorial_app.db')

# Crear todas las tablas en la base de datos
Base.metadata.create_all(engine)

# Crear una sesión para interactuar con la base de datos
Session = sessionmaker(bind=engine)
session = Session()

# Ejemplo de cómo agregar un tutorial y sus etiquetas a la base de datos
def add_tutorial_with_tags(title, description, published, long_description, tags):
    tutorial = Tutorial(title=title, description=description, published=published, long_description=long_description)
    for tag_name in tags:
        tag = session.query(Tag).filter_by(name=tag_name).first()
        if not tag:
            tag = Tag(name=tag_name)
        tutorial.tags.append(tag)
    session.add(tutorial)
    session.commit()

# Ejemplo de cómo obtener todos los tutoriales
def get_all_tutorials():
    return session.query(Tutorial).all()

# Ejemplo de cómo obtener todos los tutoriales publicados
def get_published_tutorials():
    return session.query(Tutorial).filter_by(published=True).all()

# Ejemplo de cómo obtener todos los tutoriales relacionados con una etiqueta específica
def get_tutorials_by_tag(tag_name):
    return session.query(Tutorial).join(Tutorial.tags).filter(Tag.name == tag_name).all()

# Ejemplo de uso
if __name__ == "__main__":
    # Agregar un tutorial con etiquetas
    add_tutorial_with_tags("Tutorial de SQLAlchemy", "Descripción del tutorial de SQLAlchemy", True, "Descripción larga del tutorial de SQLAlchemy", ["SQLAlchemy", "Base de datos"])

    # Obtener todos los tutoriales
    all_tutorials = get_all_tutorials()
    print("Todos los tutoriales:")
    for tutorial in all_tutorials:
        print(tutorial.title)

    # Obtener todos los tutoriales publicados
    published_tutorials = get_published_tutorials()
    print("\nTutoriales publicados:")
    for tutorial in published_tutorials:
        print(tutorial.title)

    # Obtener todos los tutoriales relacionados con una etiqueta específica
    tag_tutorials = get_tutorials_by_tag("SQLAlchemy")
    print("\nTutoriales relacionados con SQLAlchemy:")
    for tutorial in tag_tutorials:
        print(tutorial.title)

