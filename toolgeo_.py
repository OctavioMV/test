import folium
import overpy
import streamlit as st
from geopy.geocoders import Nominatim
from streamlit_folium import folium_static

# Function to get coordinates and shop types
def get_coordinates_and_shops(addresses, radius, show_supermarkets, show_restaurants):
    geolocator = Nominatim(user_agent="food_map")
    map_centers = []

    for address in addresses:
        location = geolocator.geocode(address)
        if location:
            map_centers.append({
                'coordinates': [location.latitude, location.longitude],
                'address': address,
            })

    if not map_centers:
        return None

    m = folium.Map(location=map_centers[0]['coordinates'], zoom_start=14)
    api = overpy.Overpass()

    for center in map_centers:
        coordinates = center['coordinates']
        address = center['address']

        folium.Marker(
            location=coordinates,
            popup=address,
        ).add_to(m)

        folium.Circle(
            location=coordinates,
            radius=radius,
            color='blue',
            fill=True,
            fill_opacity=0.2,
        ).add_to(m)

        query = f"""
        [out:json];
        (
          {"node['amenity'='restaurant'](around:%d,%f,%f);" % (radius, coordinates[0], coordinates[1]) if show_restaurants else ''}
          {"node['shop'='supermarket'](around:%d,%f,%f);" % (radius, coordinates[0], coordinates[1]) if show_supermarkets else ''}
        );
        out center;
        """

        result = api.query(query)
        for node in result.nodes:
            amenity_type = node.tags.get('amenity')
            shop_type = node.tags.get('shop')
            icon_html = ""

            if show_restaurants and amenity_type and amenity_type != 'Unknown':
                icon_html = '<i class="fa fa-cutlery"></i> ' + amenity_type
            elif show_supermarkets and shop_type and shop_type != 'Unknown':
                icon_html = '<i class="fa fa-shopping-cart"></i> ' + shop_type

            if icon_html:
                folium.Marker(
                    location=[node.lat, node.lon],
                    icon=folium.DivIcon(html=icon_html),
                ).add_to(m)

        for way in result.ways:
            amenity_type = way.tags.get('amenity')
            shop_type = way.tags.get('shop')
            icon_html = ""

            if show_restaurants and amenity_type and amenity_type != 'Unknown':
                icon_html = '<i class="fa fa-cutlery"></i> ' + amenity_type
            elif show_supermarkets and shop_type and shop_type != 'Unknown':
                icon_html = '<i class="fa fa-shopping-cart"></i> ' + shop_type

            if icon_html:
                folium.Marker(
                    location=[way.center_lat, way.center_lon],
                    icon=folium.DivIcon(html=icon_html),
                ).add_to(m)

    return m

# Streamlit User Interface
st.title("Open tool to trace food-borne outbreaks, identifying nearby restaurants and supermarkets")
st.sidebar.header("Configuration")

# Configuration for circle radius and addresses
radius = st.sidebar.slider("Circle Radius (meters)", 100, 10000, 1000)
addresses = st.sidebar.text_area("Address/es (one per line)")

# Configuration for what to show on the map
show_supermarkets = st.sidebar.checkbox("Show Supermarkets", True)
show_restaurants = st.sidebar.checkbox("Show Restaurants", True)

if st.sidebar.button("Generate Map"):
    addresses = [line.strip() for line in addresses.split('\n') if line.strip()]
    if addresses:
        map = get_coordinates_and_shops(addresses, radius, show_supermarkets, show_restaurants)
        if map:
            folium_static(map)  # Use folium_static to display the map
        else:
            st.warning("No coordinates found for the provided addresses.")
    else:
        st.warning("Please enter at least one address.")
