# Enhanced Rock Weathering (ERW) Dashboard

An interactive dashboard for analyzing and visualizing Enhanced Rock Weathering (ERW) data, including geological features, climate data, and volcanic areas.

## Features

- **Interactive Geological Map**: Visualize geological features with detailed information about age, type, and mineral composition
- **Climate Data Integration**: Overlay climate zones with temperature and rainfall information
- **Volcanic Areas Analysis**: Map and analyze volcanic regions and their characteristics
- **Data Analysis Tools**: Comprehensive analysis of geological features, climate correlations, and mineral compositions
- **Interactive Visualizations**: Dynamic charts and maps for better data understanding
Added 
## Installation

1. Clone the repository:
```bash
git clone [your-repository-url]
cd erw-dashboard
```

2. Create a virtual environment:
```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

1. Run the geological visualization:
```bash
streamlit run arcgis_visualization.py
```

2. Run the volcanic areas visualization:
```bash
streamlit run volcanic_areas.py
```

## Project Structure

```
erw-dashboard/
├── arcgis_visualization.py    # Geological and climate data visualization
├── volcanic_areas.py         # Volcanic regions analysis
├── requirements.txt          # Project dependencies
└── README.md                # Project documentation
```

## Dependencies

- streamlit
- folium
- geopandas
- pandas
- requests
- branca
- numpy

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- ArcGIS REST API for geological and climate data
- Streamlit for the web application framework
- Folium for interactive mapping
