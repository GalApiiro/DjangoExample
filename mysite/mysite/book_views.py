from rest_framework.decorators import api_view


@api_view(['DELETE'])
def delete_book(book):
    return f"{book} is deleted"


class Library:
    @api_view()
    def get_books(self, ):
        return f"Harry Potter 1&2"
