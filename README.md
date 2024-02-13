Food-Borne Outbreak Tracing Tool

The Food-Borne Outbreak Tracing Tool is a web application that generates a map displaying nearby restaurants and supermarkets based on user-provided addresses. This tool aims to assist in tracing potential sources of food-borne illnesses by identifying food establishments in proximity to specified locations. This code has been uploaded in the streamlit server and can be executed there (https://toolgeo.streamlit.app/).

Features

    Interactive Map: Utilizes Folium to create an interactive map that displays markers for addresses, restaurants, and supermarkets.
    Customizable Configuration: Allows users to adjust the circle radius and choose whether to display supermarkets and/or restaurants on the map.
    Geocoding Support: Utilizes Geopy to convert user-provided addresses into geographic coordinates for mapping.
    OpenStreetMap Integration: Queries OpenStreetMap data using Overpy to identify nearby restaurants and supermarkets.

Dependencies

    Folium: For creating interactive maps.
    Overpy: For querying OpenStreetMap data.
    Streamlit: For creating interactive web applications.
    Geopy: For geocoding addresses.
    Streamlit-Folium: For integrating Folium maps with Streamlit.

Usage

    Input Addresses: Enter one or more addresses in the sidebar.
    Adjust Radius: Use the slider to adjust the radius of the search area.
    Select Features: Choose whether to show supermarkets and/or restaurants on the map.
    Generate Map: Click the "Generate Map" button to display the map with markers.

Functionality

The core functionality of the tool is encapsulated within the get_coordinates_and_shops function. This function retrieves coordinates for provided addresses and places markers for nearby restaurants and/or supermarkets on the map.

Streamlit User Interface

The Streamlit User Interface provides a simple and intuitive way for users to interact with the tool:

    Sidebar Configuration: Contains options to adjust the circle radius, input addresses, and select features to display on the map.
    Generate Map Button: Triggers the generation of the map based on user inputs.

Contributing

Contributions to this project are welcome! If you have suggestions for improvements or bug fixes, feel free to open an issue or submit a pull request.

License

This project is licensed under the Creative Commons 4.0.

Acknowledgments

    This project utilizes open-source libraries and data from Folium, Overpy, Geopy, and OpenStreetMap.
    Special thanks to the Streamlit community for their support and contributions to the Streamlit framework.

