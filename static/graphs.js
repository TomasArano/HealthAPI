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

// Chart 3: Load time per activity data from /timeActivity endpoint when Tab 3 is shown
$('#bs-tab3').on("shown.bs.tab", function(){
    fetch('/timeActivity')
        .then(response => response.json())
        .then(data => {
            const activities = data.map(item => item.Activity);
            const totalTimes = data.map(item => item.totalTime);
            // Updated saturated and dark colours palette with additional colours
            const palette = [
                "rgba(200, 0, 0, 0.8)",    // dark red
                "rgba(204, 153, 0, 0.8)",  // mustard yellow
                "rgba(0, 128, 0, 0.8)",    // dark green
                "rgba(0, 0, 139, 0.8)",    // dark blue
                "rgba(128, 0, 128, 0.8)",  // dark purple
                "rgba(192, 112, 208, 0.8)",// lilac
                "rgba(64, 224, 208, 0.8)"  // turquoise blue
            ];
            // Assign colours using modulo to loop through the palette
            const colors = activities.map((_, i) => palette[i % palette.length]);
            const ctx3 = document.getElementById('chart3').getContext('2d');
            new Chart(ctx3, {
                type: 'doughnut',
                data: {
                    labels: activities,
                    datasets: [{
                        label: 'Time per Activity (minutes)',
                        data: totalTimes,
                        backgroundColor: colors
                    }]
                },
                options: {
                    plugins: {
                        tooltip: {
                            callbacks: {
                                label: function(context) {
                                    const label = context.label || '';
                                    const value = context.raw;
                                    return `${label}: ${value.toFixed(2)} minutes`;
                                }
                            }
                        }
                    }
                }
            });
        })
        .catch(error => console.error('Error (Chart 3):', error));
    
    // Remove the event listener so that Chart 3 is rendered only once
    $('#bs-tab3').off("shown.bs.tab");
});