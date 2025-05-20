# Enhanced Rock Weathering (ERW) Analysis Dashboard

This interactive dashboard provides a comprehensive analysis of Enhanced Rock Weathering (ERW) potential across different regions, evaluating decarbonization performance and economic viability under various carbon pricing scenarios.

## Features

- Interactive global map showing ERW potential regions
- Regional analysis with detailed metrics
- Economic assessment under different carbon pricing scenarios
- ROI calculations for different regions
- Time horizon projections

## Installation

1. Clone this repository:
```bash
git clone <repository-url>
cd <repository-name>
```

2. Install the required dependencies:
```bash
pip install -r requirements.txt
```

## Running the Application

To run the dashboard, execute:
```bash
streamlit run app.py
```

The dashboard will open in your default web browser at `http://localhost:8501`.

## Usage

1. **Global Map Tab**
   - View regions with high ERW potential
   - Click on markers to see detailed information
   - Green markers indicate high potential regions
   - Orange markers indicate medium potential regions

2. **Regional Analysis Tab**
   - View CO2 sequestration potential by region
   - Compare economic viability scores
   - Analyze agricultural land availability
   - Sort and filter data using interactive tables

3. **Economic Assessment Tab**
   - Adjust carbon price using the sidebar slider
   - View economic viability under different scenarios
   - Analyze ROI calculations
   - Compare payback periods across regions

## Data Sources

The analysis is based on:
- Publicly available datasets
- Research from the PEESE group
- Regional agricultural statistics
- Carbon pricing scenarios

## References

- Alves, Faria, Simão. "Madeiran basalt characterization." Journal of Building Engineering, 2017. [PDF](https://research.unl.pt/ws/portalfiles/portal/3160539/RI_Alves_Faria_Simao_Madeiran_basalt_characterizarion_JBE2017_manuscript.pdf)
- [basalts_flexible_calculation GitHub Repository](https://github.com/iozer/basalts_flexible_calculation)
- PEESEgroup/Enhanced-Rock-Weathering: [GitHub Repository](https://github.com/PEESEgroup/Enhanced-Rock-Weathering)
- Publicly available datasets and geological literature

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
