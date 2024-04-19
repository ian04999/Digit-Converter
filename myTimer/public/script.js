document.addEventListener('DOMContentLoaded', function () {
  // Function to update the displayed time
  function updateClock() {
    const currentTimeElement = document.getElementById('currentTime');
    const currentTimeInMilliseconds = new Date().getTime();
	
	const options = { hour12: false };  // Display time in 24-hour format
    const formattedTime = new Date(currentTimeInMilliseconds).toLocaleTimeString(undefined, options);
    
	const milliseconds = currentTimeInMilliseconds % 1000;

    currentTimeElement.textContent = `Current Time: ${formattedTime}:${milliseconds}`;
  }

  // Update the time every second (1000 milliseconds)
  setInterval(updateClock, 1);

  // Initial update
  updateClock();
});
