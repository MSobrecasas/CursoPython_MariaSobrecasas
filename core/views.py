from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.status import *
from django.core.serializers import serialize
import json
from core.models import *
from datetime import datetime


# Create your views here.
class CategoryView(APIView):
    def get(self, request, category_id=None):
        if category_id:
            if Category.objects.filter(pk=category_id).exists():
                category_response = Category.objects.filter(pk=category_id)
            else:
                return HttpResponse(content_type='application/json',
                                    content=json.dumps({'detail': 'Category not found'}),
                                    status=HTTP_404_NOT_FOUND)
        else:
            category_response = Category.objects.all()
        category_response = serialize('json', category_response)

        return HttpResponse(content_type='application/json',
                            content=category_response,
                            status=HTTP_200_OK)

    def post(self, request):
        body = json.loads(request.body)
        category, created = Category.objects.get_or_create(**body)
        if created:
            category.save()
            return HttpResponse(content_type='application/json',
                                content=json.dumps({'detail': 'Category created successfully',
                                                    'data': body}),
                                status=HTTP_201_CREATED)
        return HttpResponse(content_type='application/json',
                            content=json.dumps({'detail': 'Category already exists'}),
                            status=HTTP_409_CONFLICT)

    def put(self, request, category_id):
        category = Category.objects.filter(pk=category_id)
        if not category.exists():
            return HttpResponse(content_type='application/json',
                                content=json.dumps({'detail': 'Category not found'}),
                                status=HTTP_404_NOT_FOUND)
        body = json.loads(request.body)
        body['last_update'] = datetime.now()
        category.update(**body)
        return HttpResponse(content_type='application/json',
                            content=json.dumps({'detail': 'Category updated successfully'}),
                            status=HTTP_200_OK)

    def delete(self, request, category_id):
        category = Category.objects.filter(pk=category_id)
        if not category.exists():
            return HttpResponse(content_type='application/json',
                                content=json.dumps({'detail': 'Category not found'}),
                                status=HTTP_404_NOT_FOUND)
        category.delete()
        return HttpResponse(content_type='application/json',
                            content=json.dumps({'detail': 'Category deleted successfully'}),
                            status=HTTP_200_OK)


class CategoryNameView(APIView):
    def get(self, request, category_name=None):

        if Category.objects.filter(name__iexact=category_name):
            category_response = list(Category.objects.filter(name__iexact=category_name).only("name",
                                                                                              "recommended_age", ))
        else:
            return HttpResponse(content_type='application/json',
                                content=json.dumps({'detail': 'Category not found'}),
                                status=HTTP_404_NOT_FOUND)
        category_response = serialize('json', category_response)

        return HttpResponse(content_type='application/json',
                            content=category_response,
                            status=HTTP_200_OK)


class AuthorView(APIView):
    def get(self, request, author_id=None):
        if author_id:
            if Author.objects.filter(pk=author_id).exists():
                author_response = Author.objects.filter(pk=author_id)
            else:
                return HttpResponse(content_type='application/json',
                                    content=json.dumps({'detail': 'Author not found'}),
                                    status=HTTP_404_NOT_FOUND)
        else:
            author_response = Author.objects.all()
        author_response = serialize('json', author_response)

        return HttpResponse(content_type='application/json',
                            content=author_response,
                            status=HTTP_200_OK)

    def post(self, request):
        body = json.loads(request.body)
        author, created = Author.objects.get_or_create(**body)
        if created:
            author.save()
            return HttpResponse(content_type='application/json',
                                content=json.dumps({'detail': 'Author created successfully',
                                                    'data': body}),
                                status=HTTP_201_CREATED)
        return HttpResponse(content_type='application/json',
                            content=json.dumps({'detail': 'Author already exists'}),
                            status=HTTP_409_CONFLICT)

    def put(self, request, author_id):
        author = Author.objects.filter(pk=author_id)
        if not author.exists():
            return HttpResponse(content_type='application/json',
                                content=json.dumps({'detail': 'Author not found'}),
                                status=HTTP_404_NOT_FOUND)
        body = json.loads(request.body)
        body['last_update'] = datetime.now()
        author.update(**body)
        return HttpResponse(content_type='application/json',
                            content=json.dumps({'detail': 'Author updated successfully'}),
                            status=HTTP_200_OK)

    def delete(self, request, author_id):
        author = Author.objects.filter(pk=author_id)
        if not author.exists():
            return HttpResponse(content_type='application/json',
                                content=json.dumps({'detail': 'Author not found'}),
                                status=HTTP_404_NOT_FOUND)
        author.delete()
        return HttpResponse(content_type='application/json',
                            content=json.dumps({'detail': 'Author deleted successfully'}),
                            status=HTTP_200_OK)


class AuthorLastnameView(APIView):
    def get(self, request, author_last_name=None):

        if Author.objects.filter(last_name__iexact=author_last_name):
            author_response = list(Author.objects.filter(last_name__iexact=author_last_name).only("first_name",
                                                                                                  "last_name", ))
        else:
            return HttpResponse(content_type='application/json',
                                content=json.dumps({'detail': 'Author not found'}),
                                status=HTTP_404_NOT_FOUND)
        author_response = serialize('json', author_response)

        return HttpResponse(content_type='application/json',
                            content=author_response,
                            status=HTTP_200_OK)


class PartnerView(APIView):
    def get(self, request, partner_id=None):
        if partner_id:
            if Partner.objects.filter(pk=partner_id).exists():
                partner_response = Partner.objects.filter(pk=partner_id)
            else:
                return HttpResponse(content_type='application/json',
                                    content=json.dumps({'detail': 'Partner not found'}),
                                    status=HTTP_404_NOT_FOUND)
        else:
            partner_response = Partner.objects.all()
        partner_response = serialize('json', partner_response)

        return HttpResponse(content_type='application/json',
                            content=partner_response,
                            status=HTTP_200_OK)

    def post(self, request):
        body = json.loads(request.body)
        partner, created = Partner.objects.get_or_create(**body)
        if created:
            partner.save()
            return HttpResponse(content_type='application/json',
                                content=json.dumps({'detail': 'Partner created successfully',
                                                    'data': body}),
                                status=HTTP_201_CREATED)
        return HttpResponse(content_type='application/json',
                            content=json.dumps({'detail': 'Partner already exists'}),
                            status=HTTP_409_CONFLICT)

    def put(self, request, partner_id):
        partner = Partner.objects.filter(pk=partner_id)
        if not partner.exists():
            return HttpResponse(content_type='application/json',
                                content=json.dumps({'detail': 'Partner not found'}),
                                status=HTTP_404_NOT_FOUND)
        body = json.loads(request.body)
        body['last_update'] = datetime.now()
        partner.update(**body)
        return HttpResponse(content_type='application/json',
                            content=json.dumps({'detail': 'Partner updated successfully'}),
                            status=HTTP_200_OK)

    def delete(self, request, partner_id):
        partner = Partner.objects.filter(pk=partner_id)
        if not partner.exists():
            return HttpResponse(content_type='application/json',
                                content=json.dumps({'detail': 'Partner not found'}),
                                status=HTTP_404_NOT_FOUND)
        partner.delete()
        return HttpResponse(content_type='application/json',
                            content=json.dumps({'detail': 'Partner deleted successfully'}),
                            status=HTTP_200_OK)


class PartnerDniView(APIView):
    def get(self, request, partner_dni=None):

        if Partner.objects.filter(dni__iexact=partner_dni):
            partner_response = list(Partner.objects.filter(dni__iexact=partner_dni).only("first_name",
                                                                                         "last_name",
                                                                                         "dni"))
        else:
            return HttpResponse(content_type='application/json',
                                content=json.dumps({'detail': 'Partner not found'}),
                                status=HTTP_404_NOT_FOUND)
        author_response = serialize('json', partner_response)

        return HttpResponse(content_type='application/json',
                            content=author_response,
                            status=HTTP_200_OK)


class BookView(APIView):

    def get(self, request, book_id=None):
        if book_id:
            if Book.objects.filter(pk=book_id).exists():
                book_response = Book.objects.filter(pk=book_id)
            else:
                return HttpResponse(content_type='application/json',
                                    content=json.dumps({'detail': 'Book not found'}),
                                    status=HTTP_404_NOT_FOUND)
        else:
            book_response = Book.objects.all()
        book_response = serialize('json', book_response)

        return HttpResponse(content_type='application/json',
                            content=book_response,
                            status=HTTP_200_OK)

    def post(self, request):
        body = json.loads(request.body)
        body['author'] = Author.objects.get(pk=body['author'])
        body['category'] = Category.objects.get(pk=body['category'])
        book, created = Book.objects.get_or_create(**body)
        if created:
            book.save()
            return HttpResponse(content_type='application/json',
                                content=json.dumps({'detail': 'Book created successfully'}),
                                status=HTTP_201_CREATED)
        return HttpResponse(content_type='application/json',
                            content=json.dumps({'detail': 'Book already exists'}),
                            status=HTTP_409_CONFLICT)

    def put(self, request, book_id):
        book = Book.objects.filter(pk=book_id)
        if not book.exists():
            return HttpResponse(content_type='application/json',
                                content=json.dumps({'detail': 'Book not found'}),
                                status=HTTP_404_NOT_FOUND)
        body = json.loads(request.body)
        body['last_update'] = datetime.now()
        book.update(**body)
        return HttpResponse(content_type='application/json',
                            content=json.dumps({'detail': 'Book updated successfully'}),
                            status=HTTP_200_OK)

    def delete(self, request, book_id):
        book = Book.objects.filter(pk=book_id)
        if not book.exists():
            return HttpResponse(content_type='application/json',
                                content=json.dumps({'detail': 'Book not found'}),
                                status=HTTP_404_NOT_FOUND)
        book.delete()
        return HttpResponse(content_type='application/json',
                            content=json.dumps({'detail': 'Book deleted successfully'}),
                            status=HTTP_200_OK)


class BookAuthorView(APIView):
    def get(self, request, author_id=None):

        if Book.objects.filter(author__exact=author_id):
            partner_response = list(Book.objects.filter(author__exact=author_id).only("name",
                                                                                      "author",
                                                                                      "category"))
        else:
            return HttpResponse(content_type='application/json',
                                content=json.dumps({'detail': 'Book not found'}),
                                status=HTTP_404_NOT_FOUND)
        response = serialize('json', partner_response)

        return HttpResponse(content_type='application/json',
                            content=response,
                            status=HTTP_200_OK)


class BookLoanView(APIView):

    def get(self, request, bookloan_id=None):
        if bookloan_id:
            if BookLoan.objects.filter(pk=bookloan_id).exists():
                bookloan_response = BookLoan.objects.filter(pk=bookloan_id)
            else:
                return HttpResponse(content_type='application/json',
                                    content=json.dumps({'detail': 'BookLoan not found'}),
                                    status=HTTP_404_NOT_FOUND)
        else:
            bookloan_response = BookLoan.objects.all()
        bookloan_response = serialize('json', bookloan_response)

        return HttpResponse(content_type='application/json',
                            content=bookloan_response,
                            status=HTTP_200_OK)

    def post(self, request):
        body = json.loads(request.body)
        body['book'] = Book.objects.get(pk=body['book'])
        body['partner'] = Partner.objects.get(pk=body['partner'])
        bookloan, created = BookLoan.objects.get_or_create(**body)
        if created:
            bookloan.save()
            return HttpResponse(content_type='application/json',
                                content=json.dumps({'detail': 'BookLoan created successfully'}),
                                status=HTTP_201_CREATED)
        return HttpResponse(content_type='application/json',
                            content=json.dumps({'detail': 'BookLoan already exists'}),
                            status=HTTP_409_CONFLICT)

    def put(self, request, bookloan_id):
        bookloan = BookLoan.objects.filter(pk=bookloan_id)
        if not bookloan.exists():
            return HttpResponse(content_type='application/json',
                                content=json.dumps({'detail': 'BookLoan not found'}),
                                status=HTTP_404_NOT_FOUND)
        body = json.loads(request.body)
        body['last_update'] = datetime.now()
        bookloan.update(**body)
        return HttpResponse(content_type='application/json',
                            content=json.dumps({'detail': 'BookLoan updated successfully'}),
                            status=HTTP_200_OK)

    # def delete(self, request, bookloan_id):
    #     bookloan = BookLoan.objects.filter(pk=bookloan_id)
    #     if not bookloan.exists():
    #         return HttpResponse(content_type='application/json',
    #                             content=json.dumps({'detail': 'BookLoan not found'}),
    #                             status=HTTP_404_NOT_FOUND)
    #     bookloan.delete()
    #     return HttpResponse(content_type='application/json',
    #                         content=json.dumps({'detail': 'BookLoan deleted successfully'}),
    #                         status=HTTP_200_OK)


class BookLoanStatusView(APIView):
    def get(self, request, status=None):

        if BookLoan.objects.filter(status__exact=status):
            response = list(BookLoan.objects.filter(status__exact=status).only("status",
                                                                               "book",
                                                                               "partner"))
        else:
            return HttpResponse(content_type='application/json',
                                content=json.dumps({'detail': 'BookLoan not found'}),
                                status=HTTP_404_NOT_FOUND)
        author_response = serialize('json', response)

        return HttpResponse(content_type='application/json',
                            content=author_response,
                            status=HTTP_200_OK)


class BookLoanPartnerView(APIView):
    def get(self, request, partner_dni=None):
        if Partner.objects.filter(dni__iexact=partner_dni):
            partner = list(Partner.objects.filter(dni__iexact=partner_dni))[0]

            if BookLoan.objects.filter(partner__exact=partner.pk):
                response = list(BookLoan.objects.filter(partner__exact=partner.pk).only("status",
                                                                                        "book",
                                                                                        "partner"))
            else:
                return HttpResponse(content_type='application/json',
                                    content=json.dumps({'detail': 'BookLoan not found'}),
                                    status=HTTP_404_NOT_FOUND)
            author_response = serialize('json', response)

            return HttpResponse(content_type='application/json',
                                content=author_response,
                                status=HTTP_200_OK)
        else:
            return HttpResponse(content_type='application/json',
                                content=json.dumps({'detail': 'Partner not found'}),
                                status=HTTP_404_NOT_FOUND)