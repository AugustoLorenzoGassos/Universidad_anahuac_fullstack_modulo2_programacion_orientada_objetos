#import numpy

class blogpost:
    sitio_web="www.miblog.com"

blogpost1 = blogpost()
blogpost1.titulo="tútulo del blogpost 1"
blogpost1.autor="Augusto Lorenzo Gassós"
blogpost1.contenido="Comentarios sobre python"
blogpost1.publicado=True
blogpost1.vistas=150

blogpost2 = blogpost()
blogpost2.titulo="tútulo del blogpost 2"
blogpost2.autor="Augusto Lorenzo Gassós"
blogpost2.contenido="Programación orientada a objetos"
blogpost2.publicado=False
blogpost2.vistas=0

blogpost3 = blogpost()
blogpost3.titulo="tútulo del blogpost 3"
blogpost3.autor="Augusto Lorenzo Gassós"
blogpost3.contenido="Uso del framework Django"
blogpost3.publicado=True
blogpost3.vistas=300

blogpost4 = blogpost()
blogpost4.titulo="tútulo del blogpost 4"
blogpost4.autor="Augusto Lorenzo Gassós"
blogpost4.contenido="SQL Server"
blogpost4.publicado=False
blogpost4.vistas=0

lista_blog = [blogpost1, blogpost2, blogpost3, blogpost4]

blog_publicados = 0
blog_publicados_visitas = 0

for blogs in lista_blog:
    if blogs.publicado == True:
        blog_publicados +=1
        blog_publicados_visitas += blogs.vistas

print(f"Total de blogs publicados: {blog_publicados}")
print(f"Tptal de visitas en blogs publicados: {blog_publicados_visitas}")
print(f"Promedio de visitas: {blog_publicados_visitas/blog_publicados}")
