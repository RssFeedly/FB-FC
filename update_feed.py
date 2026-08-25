from datetime import datetime
from feedgen.feed import FeedGenerator

def generate_rss():
    fg = FeedGenerator()
    fg.id('https://www.facebook.com/FCASanMarcosOficial/')
    fg.title('FCASanMarcosOficial - Facebook')
    fg.author({'name': 'FCASanMarcosOficial', 'email': 'no-reply@github.com'})
    fg.link(href='https://www.facebook.com/FCASanMarcosOficial/', rel='alternate')
    fg.subtitle('Feed automatizado para FCASanMarcosOficial')
    fg.language('es')

    # Añadimos una entrada de aviso o estado actual
    fe = fg.add_entry()
    fe.id(f'https://www.facebook.com/FCASanMarcosOficial/ {datetime.now().strftime("%Y-%m-%d %H:%M")}')
    fe.title('Visita la página oficial de FCA San Marcos en Facebook')
    fe.link(href='https://www.facebook.com/FCASanMarcosOficial/')
    fe.published(datetime.now().strftime('%Y-%m-%dT%H:%M:%S+00:00'))
    fe.description('Este es un feed de respaldo automatizado. Debido a las restricciones de seguridad y anti-scraping de Meta, te recomendamos visitar directamente la página oficial para ver las últimas publicaciones.')

    # Generar el archivo feed.xml en la raíz del repositorio
    fg.rss_file('feed.xml', pretty=True)
    print("¡Archivo feed.xml generado con éxito!")

if __name__ == '__main__':
    generate_rss()
