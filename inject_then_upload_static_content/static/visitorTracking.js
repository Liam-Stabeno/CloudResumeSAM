const apiUrl = "${ApiUrl}";
    
async function sendUserAgent() {
  const BrowserData = navigator.userAgent; // Collect User-Agent
  try {
    await fetch(apiUrl, {
      method: "POST",
      headers: {
        "content-type": "application/json",
      },
      body: JSON.stringify({
        userAgent: BrowserData,
      }),
    });
  } catch (error) {
    console.error("Error sending User-Agent: ", error);
    document.getElementById("error-message").textContent =
      "Error sending User-Agent.";
  }
}

async function loadPageViews() {
  try {
    const response = await fetch(apiUrl, {
      method: "GET",
      headers: {
        "content-type": "application/json",
      },
    });

    const data = await response.json();
    document.getElementById("pageViews").textContent = "Page Views: " +
      data.TotalVisits || 0;
  } catch (error) {
    console.error("Error fetching page views:", error);
    document.getElementById("pageViews").textContent =
      "Error loading data";
    document.getElementById("error-message").textContent =
      "Error fetching page views.";
  }
}

function delay(ms) {
  return new Promise((resolve) => setTimeout(resolve, ms));
}

window.onload = async () => {
  await loadPageViews();
  await delay(1500); // Wait for 1.5 seconds
  await sendUserAgent(); // Then send User-Agent
};
