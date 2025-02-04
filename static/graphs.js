// Chart 1: Load average BPM data
fetch('/averageBPM')
    .then(response => response.json())
    .then(data => {
        const hours = data.map(item => item.Hour);
        const bpmValues = data.map(item => item.averageBPM);
        const ctx1 = document.getElementById('chart1').getContext('2d');
        new Chart(ctx1, {
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
    .catch(error => console.error('Error (Chart 1):', error));

// Chart 2: Load BPM range data from /rangeBPM endpoint when Tab 2 is shown
$('#bs-tab2').on("shown.bs.tab", function(){
    fetch('/rangeBPM')
      .then(response => response.json())
      .then(data => {
         // Prepare data: Each data point is an object with x (Hour) and y array [minBPM, maxBPM]
         const hours = data.map(item => item.Hour);
         const rangeData = data.map(item => ({
             x: item.Hour,
             y: [item.minBPM, item.maxBPM]
         }));
         
         const ctx2 = document.getElementById('chart2').getContext('2d');
         new Chart(ctx2, {
           type: 'bar',
           data: {
              labels: hours,
              datasets: [{
                label: 'BPM Range',
                data: rangeData,
                backgroundColor: 'rgba(192, 75, 192, 0.6)'
              }]
           },
           options: {
              plugins: {
                  tooltip: {
                    callbacks: {
                      label: function(context) {
                          const range = context.raw.y;
                          return `Range: ${range[0]} - ${range[1]}`;
                      }
                    }
                  }
              },
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
                        text: 'BPM Range'
                    },
                    beginAtZero: true
                }
              }
           }
         });
    })
    .catch(error => console.error('Error (Chart 2):', error));

    // Remove the event listener so that Chart 2 is rendered only once
    $('#bs-tab2').off("shown.bs.tab");
});