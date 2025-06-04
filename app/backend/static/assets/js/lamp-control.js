function turnOnLamp() {
  document.getElementById("lamp-status").innerText = "ON";
  document.getElementById("lamp-status").style.color = "#28a745";
  fetch('/api/lamp', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({ state: 'on' })
  })
}

function turnOffLamp() {
  document.getElementById("lamp-status").innerText = "OFF";
  document.getElementById("lamp-status").style.color = "#dc3545";
  fetch('/api/lamp', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({ state: 'off' })
  })
}
