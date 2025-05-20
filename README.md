# Enhanced Rock Weathering (ERW) Dashboard & Analysis Toolkit

This project provides a modular, interactive dashboard and analysis toolkit for Enhanced Rock Weathering (ERW) and global carbon removal, inspired by [CDR.fyi's Carbon Removal Map](https://www.cdr.fyi/carbon-removal-map). It includes mapping, regional analysis, economic assessment, case studies, machine learning, and future scenario modeling.

## Features
- Interactive global map showing ERW potential regions
- Regional analysis with detailed metrics
- Economic assessment under different carbon pricing scenarios
- ROI calculations for different regions
- Time horizon projections
- Case studies (Madeira, Azores)
- Machine learning prediction for basalt properties
- Future scenario modeling (Brightway2 + premise)

## Folder Structure
```
dashboard/      # Main Streamlit dashboard
data/           # Project and region data (CSV, GeoJSON)
case_studies/   # Scripts for regional case studies
ml_prediction/  # ML model training and prediction
scenarios/      # Future scenario analysis notebooks
research/       # Literature and data sources
```

## Quick Start
```bash
git clone https://github.com/Ash-Impactco/ERW.git
cd ERW
pip install -r requirements.txt
streamlit run dashboard/app.py
```

## Usage
- **Global Map:** Visualize ERW projects and regions on an interactive map.
- **Regional Analysis:** Explore CO₂ sequestration and economic metrics by region.
- **Economic Assessment:** Adjust carbon price and see impact on viability and ROI.
- **Case Studies:** Analyze basalt mass and ERW potential for Madeira and Azores.
- **ML Prediction:** Upload geochemical data for machine learning-based predictions.
- **Future Scenarios:** Open `scenarios/future_scenarios.ipynb` in Jupyter for scenario modeling.

## Data Sources & References
- [CDR.fyi Carbon Removal Map](https://www.cdr.fyi/carbon-removal-map)
- [PEESEgroup/Enhanced-Rock-Weathering](https://github.com/PEESEgroup/Enhanced-Rock-Weathering)
- [Madeiran basalt characterization (Alves et al., 2017)](https://research.unl.pt/ws/portalfiles/portal/3160539/RI_Alves_Faria_Simao_Madeiran_basalt_characterizarion_JBE2017_manuscript.pdf)
- [USGS MRData](https://mrdata.usgs.gov/)

## Contributing
Contributions are welcome! Please open issues or submit pull requests.

## License
This project is licensed under the MIT License.
