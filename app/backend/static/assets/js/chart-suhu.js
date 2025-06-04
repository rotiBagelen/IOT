document.addEventListener('DOMContentLoaded', function () {
  const ctx = document.getElementById('suhuChart');
  if (!ctx) return;

  const suhuChart = new Chart(ctx, {
    type: 'line',
    data: {
      labels: [],
      datasets: [{
        label: 'Suhu (°C)',
        data: [],
        fill: false,
        borderColor: '#4a7ae2',
        backgroundColor: '#4a7ae2',
        tension: 0
      }]
    },
    options: {
      responsive: true,
      plugins: {
        legend: {
          display: false
        }
      },
      scales: {
        y: {
          beginAtZero: false,
          title: {
            display: true,
            text: 'Suhu (°C)'
          }
        },
        x: {
          title: {
            display: true,
            text: 'Waktu'
          }
        }
      }
    }
  });

  function updateData(chart) {
    fetch('/api/temp') 
      .then(response => response.json())
      .then(data => {
        const waktu = data.timestamps.map(ts => new Date(ts).toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' }));
        const suhu = data.temperatures;
        chart.data.labels = waktu;
        chart.data.datasets[0].data =suhu;
        
        // if (suhuChart.data.labels.length > 10) {
        //   chart.data.labels.shift();
        //   chart.data.datasets[0].data.shift();
        // }

        chart.update();
        const tempElement = document.getElementById('suhu-sekarang');
        const statusKipas = document.getElementById('status-kipas');
        if (tempElement) {
          tempElement.textContent = suhu[suhu.length - 1] + '°C';
          statusKipas.textContent = suhu[suhu.length - 1] > 31 ? 'ON': 'OFF';
          statusKipas.style.color = suhu[suhu.length - 1] > 31 ? '#28a745' : '#dc3545';
        }
      })
      .catch(err => console.error('Gagal ambil data:', err));
  };

  updateData(suhuChart);
  setInterval(() => updateData(suhuChart), 60000);
});
