from flask import Blueprint, request

from app.controllers import SearchController

routes = Blueprint("routes", __name__)
search_controller = SearchController()

@routes.get("/")
def search_page():
  return search_controller.search_page(
    request.args.get("search"),
    request.args.get("size"),
  )

@routes.get("/json")
def search_json():
  return search_controller.search_json(
    request.args.get("search"),
    request.args.get("size"),
  )
