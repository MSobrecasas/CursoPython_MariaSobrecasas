# CursoPython_MariaSobrecasas
Trabajo Final API REST DJANGO


API REST para el manejo basico de una Libreria

Entidades:
  Category
  Author
  Book  
  Partner
  BookLoan
  
  
 URL's
 
    'categories/' GET/POST/PUT/DELETE
    'categories/<int:category_id>' GET
    'categories_name/<str:category_name>' GET/POST/PUT/DELETE
    'authors/' GET/POST/PUT/DELETE
    'authors/<int:author_id>' GET
    'authors_last_name/' GET
    'partners/' GET/POST/PUT/DELETE
    'partners/<int:partner_id>' GET
    'partners_dni/<str:partner_dni>' GET
    'books/' GET/POST/PUT/DELETE
    'books/<int:book_id>' GET
    'books_author/<int:author_id>' GET
    'bookloans/' GET/POST/PUT
    'bookloans/<int:bookloan_id>' GET
    'bookloans_status/<str:status>' GET
    'bookloans_partner/<str:partner_dni>' GET
 
