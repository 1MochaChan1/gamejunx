from app import application, request, db, make_response
from app.colored_print import Colors, DebugPrint
from app.helpers import went_wrong, create_wishlist
from app.models import User, Wishlist


