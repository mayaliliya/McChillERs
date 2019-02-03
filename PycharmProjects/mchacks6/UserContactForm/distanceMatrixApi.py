import googlemaps
import bond
from datetime import datetime

gmaps = googlemaps.Client(key="AIzaSyAo11H5Xap778cLtl-vWOJgMA_vNq4ys3A")

origins = js.call("GetAddress")

destination = "San Francisco, California"

duration = gmaps.DistanceMatrixService().duration