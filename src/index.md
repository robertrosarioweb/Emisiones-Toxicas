---
theme: cotton
toc: false
---



<h1 style="text-align: center; margin-top: 20px; display: inline;">Panel de Control de Emisiones Toxicas en Puerto Rico 1987-2023</h1>

<p style="text-align: left; margin-top: 20px; white-space: nowrap;">
  <span style="font-weight: bold;">Fuente:</span> 
  <a href="https://www.epa.gov/toxics-release-inventory-tri-program/tri-basic-data-files-calendar-years-1987-present" style="text-decoration: none;">https://www.epa.gov/toxics-release-inventory-tri-program/tri-basic-data-files-calender-years-1987-present</a>
</p>



```js
import * as L from "npm:leaflet";
import * as aq from "npm:arquero";
import * as Inputs from "https://cdn.jsdelivr.net/npm/@observablehq/inputs@0.12/+esm";


// Slider Setup
const sliderContainer = document.createElement("div");
document.body.appendChild(sliderContainer);
const slider = Inputs.range([1987, 2023], { step: 1, value: 2023, label: "Año" });
sliderContainer.appendChild(slider);

display(slider);

// Zoom Slider Setup
const zoomsliderContainer = document.createElement("div");
document.body.appendChild(zoomsliderContainer);
const zoomSlider = Inputs.range([5, 10], { step: 1, value: 7,label:"Zoom" });
zoomsliderContainer.appendChild(zoomSlider);

display(zoomSlider);

// Map Container Setup
const container = document.createElement("div");
container.style.display = "flex";
container.style.flexDirection = "row";
container.style.position = "absolute";
container.style.top = "400px";
container.style.width = "100%";
document.body.appendChild(container);

// Map Container Setup (on the left)
const mapContainer = document.createElement("div");
mapContainer.style.flex = "1.5"; // Make the map take more space
mapContainer.style.marginRight = "100px"; // Margin to create some space between the containers
mapContainer.style.height = "650px"; // Ensure the map container has a fixed height
container.appendChild(mapContainer);

// Histograms Container Setup (on the right)
const histogramsContainer = document.createElement("div");
histogramsContainer.style.flex = "1"; // Make histograms take less space
histogramsContainer.style.marginLeft = "10px"; // Optional space on the left side of the histogram container
histogramsContainer.style.height = "600px"; 
histogramsContainer.style.paddingTop = "0px"; // Adds padding on top of the histograms
histogramsContainer.style.paddingBottom = "20px"; // Adds padding on the bottom of the histograms
container.appendChild(histogramsContainer);


const yearDisplayContainer = document.createElement("div");
yearDisplayContainer.style.position = "absolute";
yearDisplayContainer.style.top = "270px"; // Adjust this value as needed
yearDisplayContainer.style.left = "50%"; // Center it horizontally
yearDisplayContainer.style.transform = "translateX(-50%)"; // Ensure proper centering
yearDisplayContainer.style.backgroundColor = "white";
yearDisplayContainer.style.padding = "10px";
yearDisplayContainer.style.borderRadius = "5px";
yearDisplayContainer.style.fontSize = "16px";
yearDisplayContainer.style.fontWeight = "bold";
yearDisplayContainer.style.boxShadow = "0 2px 6px rgba(0, 0, 0, 0.3)";
yearDisplayContainer.style.zIndex = "1000"; // Ensure it's above the map and other elements

// Set up as a flex container with 3 columns
yearDisplayContainer.style.display = "grid";
yearDisplayContainer.style.gridTemplateColumns = "repeat(3, 1fr)";
yearDisplayContainer.style.gap = "30px"; // Increase the gap between columns
yearDisplayContainer.style.textAlign = "center"; // Align the text in the center of each column

// Append the year display container to the body (above the map)
document.body.appendChild(yearDisplayContainer);

// Create and append content blocks (placeholders for now)
const block1 = document.createElement("div");
block1.textContent = "Año: 2023";  // Placeholder text, will be updated later
yearDisplayContainer.appendChild(block1);

const block2 = document.createElement("div");
block2.textContent = "Block 2";  // Another info block
yearDisplayContainer.appendChild(block2);

const block3 = document.createElement("div");
block3.textContent = "Block 3";  // Another info block
yearDisplayContainer.appendChild(block3);

function updateYearDisplay(year) {
  // Update only the first block's content with the new year
  const yearText = `Año: ${year}`;
  
  // Ensure we update the year portion only
  block1.textContent = yearText; // Update the text content
  const yearElement = document.createElement("span");
  yearElement.textContent = year;
  yearElement.style.color = "red"; // Set the color to red

  // Replace the original year text with the span containing the red year
  block1.innerHTML = "Año: ";
  block1.appendChild(yearElement);
}
updateYearDisplay(2023);



const prButton = document.createElement("button");
prButton.textContent = "Puerto Rico";

// Adding more styles
prButton.style.marginTop = "20px"; // Optional margin
prButton.style.marginLeft = "-20px"; // Optional margin
prButton.style.padding = "10px 20px"; // Adds padding inside the button
prButton.style.fontSize = "16px"; // Font size for the text
prButton.style.backgroundColor = "gray"; // Button background color
prButton.style.color = "white"; // Text color
prButton.style.border = "none"; // Removes the default border
prButton.style.borderRadius = "5px"; // Rounded corners
prButton.style.cursor = "pointer"; // Changes cursor on hover
prButton.style.transition = "background-color 0.3s ease"; // Smooth background color transition

// Adding hover effect
prButton.addEventListener("mouseover", () => {
  prButton.style.backgroundColor = "gray"; // Change color on hover
});

prButton.addEventListener("mouseout", () => {
  prButton.style.backgroundColor = "gray"; // Revert color when not hovering
});

// Optionally append the button to the body or a specific container
document.body.appendChild(prButton);


const usaButton = document.createElement("button");
usaButton.textContent = "United States";

// Adding more styles
usaButton.style.marginTop = "20px"; // Optional margin
usaButton.style.marginLeft = "200px"; // Optional margin
usaButton.style.padding = "10px 20px"; // Adds padding inside the button
usaButton.style.fontSize = "16px"; // Font size for the text
usaButton.style.backgroundColor = "gray"; // Button background color
usaButton.style.color = "white"; // Text color
usaButton.style.border = "none"; // Removes the default border
usaButton.style.borderRadius = "5px"; // Rounded corners
usaButton.style.cursor = "pointer"; // Changes cursor on hover
usaButton.style.transition = "background-color 0.3s ease"; // Smooth background color transition

// Adding hover effect
usaButton.addEventListener("mouseover", () => {
  usaButton.style.backgroundColor = "gray"; // Change color on hover
});

usaButton.addEventListener("mouseout", () => {
  usaButton.style.backgroundColor = "gray"; // Revert color when not hovering
});

// Optionally append the button to the body or a specific container
document.body.appendChild(usaButton);


// Position the buttons at the top right of the page
prButton.style.position = "absolute";
prButton.style.top = "200px"; // Position from the top
prButton.style.right = "800px"; // Position from the right

usaButton.style.position = "absolute";
usaButton.style.top = "200px"; // Position from the top
usaButton.style.right = "600px"; // Adjust to create space between the buttons




let selectedButton = 'pr';  // Default to Puerto Rico

// Function to fetch and render data
function fetchAndRenderData(year, region) {
  let fetchData, mapView;

  // Conditional logic for data fetching and map view based on region
  if (region === 'pr') {
    fetchData = readData_PR(year); // Puerto Rico data fetching
    mapView = [18.220883, -66.410149]; // Puerto Rico's map view
  } else if (region === 'usa') {
    fetchData = readData_USA(year); // USA data fetching
    mapView = [37.0902, -95.7129]; // USA's map view
  }

  // Fetch the data and render the map and histograms
  fetchData.then((data) => {
    if (data) {
      console.log("DATAAAAAAAAAAA");
      console.log(data);
      histogramsContainer.innerHTML = ''; // Clear the existing histograms
      renderMap(data.objects()); // Render map with new data
      renderHistograms(data); // Render histograms with new data
      map.setView(mapView, region === 'pr' ? 7 : 7); // Adjust map zoom based on region
    }
  });
}

// Event listener for Puerto Rico button
prButton.addEventListener("click", () => {
  selectedButton = 'pr'; // Set the selected button to Puerto Rico
  updateYearDisplay(slider.value); // Ensure the year display updates when the button is clicked
  fetchAndRenderData(slider.value, 'pr'); // Fetch and render data for Puerto Rico
});

// Event listener for USA button
usaButton.addEventListener("click", () => {
  selectedButton = 'usa'; // Set the selected button to USA
  updateYearDisplay(slider.value); // Ensure the year display updates when the button is clicked
  fetchAndRenderData(slider.value, 'usa'); // Fetch and render data for USA
});

// Event listener for slider input
slider.addEventListener("input", (event) => {
  const year = event.target.value;
  updateYearDisplay(year); // Update year display

  // Fetch data based on the selected button (PR or USA)
  fetchAndRenderData(year, selectedButton);
});
// Map Initialization
let map;
let markers = []; // Store references to markers so we can remove them later
let legendControl;

function initializeMap() {
  if (!map) {
    const div = document.createElement("div");
    div.style.width = "105%";
    div.style.height = "90%"; // Ensure the map takes the full height of the container
    mapContainer.appendChild(div);

    // Initialize the map if not already initialized
    map = L.map(div).setView([18.220883, -66.410149], zoomSlider.value); // Centered on Puerto Rico with zoom level 7

    const linkMapa = 'https://api.mapbox.com/styles/v1/mapbox/satellite-streets-v12/tiles/512/{z}/{x}/{y}@2x?access_token=';
    const token = 'pk.eyJ1IjoibWVjb2JpIiwiYSI6IjU4YzVlOGQ2YjEzYjE3NTcxOTExZTI2OWY3Y2Y1ZGYxIn0.LUg7xQhGH2uf3zA57szCyw';

    L.tileLayer(linkMapa + token, {
      attribution: '© Mapbox © OpenStreetMap',
    }).addTo(map);
  }
}

zoomSlider.addEventListener("input", (event) => {
  const zoomLevel = event.target.value; // Get the value from the zoom slider
  map.setZoom(zoomLevel); // Set the map zoom to the slider value
});

// Create the legend control function
function createLegend() {
  legendControl = L.control({ position: "topright" });

  legendControl.onAdd = function (map) {
    const div = L.DomUtil.create("div", "info legend");
    const categories = [
  "Químicos",
  "Terminales de Petróleo a Granel",
  "Servicios Eléctricos",
  "Equipo Eléctrico",
  "Alimentos",
  "Fabricación Variada",
  "Metales Fabricados",
  "Petróleo",
  "Distribuidores de Productos Químicos",
  "Bebidas",
  "Maquinaria",
  "Productos de Madera",
  "Metales Básicos",
  "Equipos de Transporte",
  "Papel",
  "Otros",
  "Residuos Peligrosos",
  "Tabaco",
  "Plásticos y Caucho",
  "Computadoras y Productos Electrónicos"
];
    const colors = [
      "red", "blue", "green", "yellow", "purple", "orange", "pink", "brown", "gray",
      "cyan", "magenta", "lime", "indigo", "teal", "violet", "turquoise", "maroon",
      "olive", "silver", "gold"
    ];

    let legendHTML = "<h5 style='margin: 0;'>Industry Sector</h5>";
    categories.forEach((category, index) => {
      legendHTML += `
        <div style="display: flex; align-items: center; margin: 2px 0;">
          <i style="background:${colors[index]}; width: 10px; height: 10px; margin-right: 5px;"></i> 
          <span style="font-size: 8px;">${category}</span>
        </div>
      `;
    });

    div.innerHTML = legendHTML;

    
    div.style.backgroundColor = "white"; 
    div.style.padding = "5px"; 
    div.style.borderRadius = "5px"; 
    div.style.opacity = "0.9"; 
    div.style.zIndex = "9999";

    return div;
  };

  // Add the legend control to the map
  legendControl.addTo(map);
}
// Clear existing markers
function clearMarkers() {
  markers.forEach(marker => marker.remove());
  markers = []; // Reset the markers array
}


async function readData_USA(year) {
  let csvURL = `https://cdat.uprh.edu/~eramos/data/datos_EPA/${year}_us_clean.csv`;
  const response = await fetch(csvURL);
  
  // Log raw CSV data
  const csvText = await response.text();
  console.log("Fetched CSV data:", csvText);
  
  // Process the CSV and select only relevant columns
  const data = aq.fromCSV(csvText);
  return data; // Only the selected columns will be returned
}

async function readCSV(url) {
    const response = await fetch(url);
    const csvText = await response.text();
    const rows = csvText.split('\n').map(row => row.split(','));
    const headers = rows[0];
    return rows.slice(1).map(row => {
        return headers.reduce((obj, header, index) => {
            obj[header] = row[index];
            return obj;
        }, {});
    });
}

function convertToCSV(data) {
    const headers = Object.keys(data[0]);
    const csvRows = [headers.join(',')];

    data.forEach(row => {
        const values = headers.map(header => row[header]);
        csvRows.push(values.join(','));
    });

    return csvRows.join('\n');
}

async function select_PRData(data) {
    // Define the latitude and longitude boundaries for Puerto Rico
    const latMin = 17.8;
    const latMax = 19.5;
    const lonMin = -68.5;
    const lonMax = -65.0;

    // Filter the data directly using array methods
    const filteredData = data.filter(row =>
        row.LATITUDE >= latMin &&
        row.LATITUDE <= latMax &&
        row.LONGITUDE >= lonMin &&
        row.LONGITUDE <= lonMax
    );

    return filteredData;
}

async function readData_PR(year) {
    let csvURL = `https://cdat.uprh.edu/~eramos/data/datos_EPA/${year}_us_clean.csv`;
    const data = await readCSV(csvURL);
    const filteredData = await select_PRData(data);

    const datatext = convertToCSV(filteredData);
    const dataf = aq.fromCSV(datatext);
    return dataf
}

function renderMap(data) {
  initializeMap(); 

  clearMarkers(); 

  const categoryColors = {
    "Chemicals": "red",
    "Petroleum Bulk Terminals": "blue",
    "Electric Utilities": "green",
    "Electrical Equipment": "yellow",
    "Food": "purple",
    "Miscellaneous Manufacturing": "orange",
    "Fabricated Metals": "pink",
    "Petroleum": "brown",
    "Chemical Wholesalers": "gray",
    "Beverages": "cyan",
    "Machinery": "magenta",
    "Wood Products": "lime",
    "Primary Metals": "indigo",
    "Transportation Equipment": "teal",
    "Paper": "violet",
    "Other": "turquoise",
    "Hazardous Waste": "maroon",
    "Tobacco": "olive",
    "Plastics and Rubber": "silver",
    "Computers and Electronic Products": "gold"
  };

  function getColorByCategory(category) {
    const color = categoryColors[category];
    return color || "gray"; 
  }

  if (Array.isArray(data) && data.length > 0) {
    data.forEach(d => {
      const lat = d["LATITUDE"];
      const lng = d["LONGITUDE"];

      if (lat && lng && d["INDUSTRY SECTOR"]) {
        let markerColor = getColorByCategory(d["INDUSTRY SECTOR"]);
        let marker = L.circleMarker([lat, lng], { 
          color: markerColor,
          radius: 5,
          weight: 2,
          opacity: 1,
          fillOpacity: 1,
        }).addTo(map);

        const popupContent = `
          <strong>Año:</strong>${d["YEAR"]}<br>
          <strong>Municipio:</strong>${d["CITY"]}<br>
          <strong>Nombre de la Facilidad:</strong>${d["FACILITY"]}<br>
          <strong>Sector Industrial:</strong> ${d["INDUSTRY SECTOR"]}<br>
          <strong>Químico:</strong> ${d["CHEMICAL"]}<br>
        `;
        marker.bindPopup(popupContent);

    
        markers.push(marker);
      }
    });
  }
}

function renderHistograms(data) {
  const histogram1 = plotHistogram1(data, "CITY", 20);
  const histogram2 = plotHistogram2(data, "INDUSTRY SECTOR", 20);

  // Apply margin between histograms
  histogram1.style.marginBottom = "20px";  // Adds space between histograms
  histogram2.style.marginTop = "20px";  // Adds space before the second histogram
  
  histogramsContainer.appendChild(histogram1);
  histogramsContainer.appendChild(histogram2);
}



function plotHistogram1(data, variable, cantidad) {
  let dataAgrupada = data
    .groupby(variable)
    .count()
    .orderby(aq.desc('count'))
    .reify()
    .slice(0, cantidad);

  const colorScale = d3.scaleOrdinal(d3.schemeCategory10);


  const topCityData = dataAgrupada.objects()[0]; 
  const topCity = topCityData[variable]; 
  const topCityCount = topCityData.count; 
  

  const totalCases = dataAgrupada.objects().reduce((sum, city) => sum + city.count, 0);

  
  const percentage = ((topCityCount / totalCases) * 100).toFixed(2); 


  updateBlock2(topCity, topCityCount, totalCases, percentage);

  return Plot.plot({
    width: 480,
    height: 250,
    marks: [
      Plot.barX(dataAgrupada.objects(), {
        x: "count",
        y: variable,
        sort: { y: "x", reverse: true },
        fill: (d) => colorScale(d[variable]),
      }),
      Plot.ruleY([0])
    ],
    marginLeft: 140,
    marginTop: 20,
    y: { label: "MUNICIPIO" },
    x: { label: "FRECUENCIA" },
    style: {
      border: "2px solid black",
      padding: "10px",
      background: "white"
    },
    grid: true,
  });
}

function updateBlock2(topCity, topCityCount, totalCases, percentage) {
 
  const cityElement = document.createElement("span");
  cityElement.textContent = `${topCity.toUpperCase()} `; 
  cityElement.style.color = "red";  

 
  const percentageElement = document.createElement("span");
  percentageElement.textContent = ` ${percentage}%`;
  percentageElement.style.color = "red"; 

  
  const textElement = document.createElement("span");
  textElement.textContent = `La mayor cantidad de casos ocurrieron en `; 
  
  const countText = document.createElement("span");
  countText.textContent = `${topCityCount} de un total de ${totalCases} para un`; 


  block2.textContent = "";  
  block2.appendChild(textElement);  
  block2.appendChild(cityElement);  
  block2.appendChild(countText);  
  block2.appendChild(percentageElement);  
}



const categoryTranslationMap = {
  "Chemicals": "Químicos",
  "Petroleum Bulk Terminals": "Terminales de Petróleo a Granel",
  "Electric Utilities": "Servicios Eléctricos",
  "Electrical Equipment": "Equipo Eléctrico",
  "Food": "Alimentos",
  "Miscellaneous Manufacturing": "Fabricación Variada",
  "Fabricated Metals": "Metales Fabricados",
  "Petroleum": "Petróleo",
  "Chemical Wholesalers": "Distribuidores de Productos Químicos",
  "Beverages": "Bebidas",
  "Machinery": "Maquinaria",
  "Wood Products": "Productos de Madera",
  "Primary Metals": "Metales Básicos",
  "Transportation Equipment": "Equipos de Transporte",
  "Paper": "Papel",
  "Other": "Otros",
  "Hazardous Waste": "Residuos Peligrosos",
  "Tobacco": "Tabaco",
  "Plastics and Rubber": "Plásticos y Caucho",
  "Computers and Electronic Products": "Computadoras y Productos Electrónicos"
};

function plotHistogram2(data, variable, cantidad) {
  let dataAgrupada = data
    .groupby(variable)
    .count()
    .orderby(aq.desc('count'))
    .reify()
    .slice(0, cantidad);

  const translatedData = dataAgrupada.objects().map(d => {
    const translatedCategory = categoryTranslationMap[d[variable]] || d[variable]; 
    return { ...d, [variable]: translatedCategory };
  });

  // Function to truncate text and add ellipsis
  function truncateWithEllipsis(text, maxLength = 6) {
    if (text.length > maxLength) {
      return text.substring(0, maxLength) + '...';
    }
    return text;
  }

  const topIndustrySector = translatedData.length > 0 ? translatedData[0][variable] : "N/A"; 

  updateBlock3(topIndustrySector);

  const colorScale = d3.scaleOrdinal(d3.schemeCategory10);

  return Plot.plot({
    width: 480,
    height: 250,
    marks: [
      Plot.barX(translatedData, {  
        x: "count",
        y: variable,
        sort: { y: "x", reverse: true },
        fill: (d) => colorScale(d[variable]),
      }),
      Plot.ruleY([0])
    ],
    marginLeft: 140,
    marginTop: 20,
    y: {
      label: "SECTOR INDUSTRIAL",  
      tickFormat: (label) => truncateWithEllipsis(label, 20), // Apply truncation with ellipsis
    },
    x: { label: "FRECUENCIA" },
    style: {
      border: "2px solid black",
      padding: "10px",
      background: "white"
    },
    grid: true,
  });
}

function updateBlock3(topIndustrySector) {
  
  const sectorElement = document.createElement("span");
  sectorElement.textContent = topIndustrySector;
  sectorElement.style.color = "red";  

  block3.textContent = "Sector Industrial: "; 
  block3.appendChild(sectorElement);  
}

// Initialize map and add legend
initializeMap();
createLegend();

// Trigger data fetching and rendering with default year (2000) on page load
readData_PR(2023).then((data) => {
  if (data) {
    console.log("DATAAAAAAAAAAA");
    console.log(data);
    renderMap(data.objects());
    renderHistograms(data);
  } else {
    console.error("Failed to load or process data.");
  }
});

// Checkbox to hide/show legend
const legendCheckbox = document.createElement('input');
legendCheckbox.type = 'checkbox';
legendCheckbox.checked = true;
legendCheckbox.style.marginTop = '10px'; // Adds margin to the checkbox to separate it from the zoom slider
const checkboxLabel = document.createElement('label');
checkboxLabel.textContent = 'Show Legend';
checkboxLabel.style.marginLeft = '10px';

// Position the checkbox on top of the map
const checkboxContainer = document.createElement('div');
checkboxContainer.style.position = 'absolute'; // Position relative to the map container
checkboxContainer.style.top = '-140px'; // Position it near the top of the map container
checkboxContainer.style.left = '28px'; // Align it with the left side of the map container
checkboxContainer.style.zIndex = '9999'; // Ensure it's above the map and other elements
checkboxContainer.appendChild(legendCheckbox);
checkboxContainer.appendChild(checkboxLabel);

mapContainer.appendChild(checkboxContainer);

legendCheckbox.addEventListener('change', (event) => {
  if (event.target.checked) {
    map.addControl(legendControl); // Show legend
  } else {
    map.removeControl(legendControl); // Hide legend
  }
});