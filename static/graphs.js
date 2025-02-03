fetch('/averageBPM')
    .then(response => response.json())
    .then(data => {
        const hours = data.map(item => item.Hour);
        const bpmValues = data.map(item => item.averageBPM);
        const ctx = document.getElementById('chart').getContext('2d');
        new Chart(ctx, {
            type: 'bar',
            data: {
                labels: hours,
                datasets: [{
                    label: 'Average BPM',
                    data: bpmValues,
                    backgroundColor: 'rgba(75, 192, 192, 0.6)'
                }]
            },
            options: {
                scales: {
                    x: {
                        title: {
                            display: true,
                            text: 'Time (Hours)'
                        }
                    },
                    y: {
                        title: {
                            display: true,
                            text: 'Average Heartrate (BPM)'
                        },
                        beginAtZero: true
                    }
                }
            }
        });
    })
    .catch(error => console.error('Error:', error));