from flask import Blueprint, request

from app.controllers import SearchController

routes = Blueprint("routes", __name__)
search_controller = SearchController()

@routes.get("/")
def get():
  term = request.args.get("search")
  return search_controller.search(term)
