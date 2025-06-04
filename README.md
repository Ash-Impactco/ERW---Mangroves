# Enhanced Rock Weathering (ERW) Dashboard

An interactive dashboard for analyzing and visualizing Enhanced Rock Weathering (ERW) data, including geological features, climate data, and volcanic areas.

## Features

- **Interactive Geological Map**: Visualize geological features with detailed information about age, type, and mineral composition
- **Climate Data Integration**: Overlay climate zones with temperature and rainfall information
- **Volcanic Areas Analysis**: Map and analyze volcanic regions and their characteristics
- **Mangrove Areas Visualization**: Interactive mapping of mangrove forests and their characteristics
- **Web-based Interactive Map**: Accessible online visualization with layer switching capabilities
- **Data Analysis Tools**: Comprehensive analysis of geological features, climate correlations, and mineral compositions
- **Interactive Visualizations**: Dynamic charts and maps for better data understanding

## Online Visualization

Access the interactive map visualization at: [https://ash-impactco.github.io/ERW/visualization/map_visualization.html](https://ash-impactco.github.io/ERW/visualization/map_visualization.html)

Features of the interactive map:
- Toggle between geological features, volcanic areas, and mangrove areas
- Click on features to view detailed information
- Responsive design that works on all devices
- Interactive popups with feature details
- Modern UI with easy layer switching

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

- ## References

- Alves, Faria, Simão. "Madeiran basalt characterization." Journal of Building Engineering, 2017. [PDF](https://research.unl.pt/ws/portalfiles/portal/3160539/RI_Alves_Faria_Simao_Madeiran_basalt_characterizarion_JBE2017_manuscript.pdf)
- [basalts_flexible_calculation GitHub Repository](https://github.com/iozer/basalts_flexible_calculation)
- PEESEgroup/Enhanced-Rock-Weathering: [GitHub Repository](https://github.com/PEESEgroup/Enhanced-Rock-Weathering)
- Publicly available datasets and geological literature

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
