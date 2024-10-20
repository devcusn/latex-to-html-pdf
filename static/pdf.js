const loadReport = async () => {
  try {
    const response = await fetch("http://localhost:4003/api/v1/get-pdf");
    if (response.ok) {
      const blob = await response.blob();
      const url = URL.createObjectURL(blob);
      document.getElementById("embde_pdf").src = url;
    } else {
      console.error("Failed to load report:", response.statusText);
    }
  } catch (error) {
    console.error("Error:", error);
  }
};

window.onload = loadReport;
