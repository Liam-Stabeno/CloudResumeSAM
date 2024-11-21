const apiUrl = "${ApiUrl}";
    
async function loadPageViews() {
  try {
    const response = await fetch(apiUrl, {
      method: "GET",
      headers: {
        "content-type": "application/json",
      },
    });

    const data = await response.json();
    document.getElementById("pageViews").textContent = "Page Views: " + (data.TotalVisits || 0);
  } catch (error) {
    console.error("Error fetching page views:", error);
    document.getElementById("pageViews").textContent = "Error loading data";
    document.getElementById("error-message").textContent = "Error fetching page views.";
  }
}

window.onload = async () => {
  await loadPageViews()
};
