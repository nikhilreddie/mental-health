    // Function to toggle dark mode
    function toggleDarkMode() {
      var body = document.body;
      body.classList.toggle("dark-mode"); // Toggle dark mode class on the body
      var isDarkMode = body.classList.contains("dark-mode"); // Check if dark mode is active
      localStorage.setItem("darkMode", isDarkMode); // Store the state of dark mode in localStorage
    }

    // Function to set dark mode based on localStorage
    function setDarkModeFromStorage() {
      var darkMode = localStorage.getItem("darkMode");
      if (darkMode === 'true') {
        document.body.classList.add("dark-mode"); // Add dark mode class to the body
      }
    }

    // Call the function to set dark mode from localStorage when the page loads
    setDarkModeFromStorage();

    // Optionally, you can also listen for changes in localStorage to update the dark mode dynamically
    window.addEventListener('storage', function (event) {
      if (event.key === 'darkMode') {
        setDarkModeFromStorage();
      }
    });