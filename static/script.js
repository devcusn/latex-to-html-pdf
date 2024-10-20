const loadReport = async () => {
  try {
    const response = await fetch("http://localhost:4003/api/v1/get-report");
    if (response.ok) {
      let htmlContent = await response.text();
      document.getElementById("report_frame").srcdoc = htmlContent;
    } else {
      console.error("Failed to load report:", response.statusText);
    }
  } catch (error) {
    console.error("Error:", error);
  }
};

window.onload = loadReport;
