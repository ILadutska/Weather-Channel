let timeElement = document.getElementById("currentTime");
let dayElement = document.getElementById("currentDay");
let dateElement = document.getElementById("currentDate");

setInterval(() => {
  let d = new Date();

  //time
  timeElement.innerHTML = d.toLocaleTimeString();

  //day name
  dayElement.innerHTML = d.toLocaleDateString('en-US', { weekday: 'long' });

  // "mm/dd/yyyy" format
  let month = (d.getMonth() + 1).toString().padStart(2, '0');
  let day = d.getDate().toString().padStart(2, '0');
  let year = d.getFullYear();
  dateElement.innerHTML = `${month}/${day}/${year}`;
}, 1000);


