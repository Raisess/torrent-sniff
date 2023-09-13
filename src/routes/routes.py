from flask import Blueprint, request

from app.controllers import SearchController

routes = Blueprint("routes", __name__)
search_controller = SearchController()

@routes.get("/")
def search():
  return search_controller.search(request.args.get("search"))
