fetch('/averageBPM')
    .then(response => response.json())
    .then(data => {
        // Prepare data for both charts
        const hours = data.map(item => item.Hour);
        const bpmValues = data.map(item => item.averageBPM);

        // Chart 1: Regular Bar Chart
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

        // Setup listener for Tab 2 to render the floating bars chart
        $('#bs-tab2').on("shown.bs.tab", function(){
            // Calculate floating bar values: simulate a range (average-5, average+5)
            const floatingData = data.map(item => {
                const lower = item.averageBPM - 5;
                const upper = item.averageBPM + 5;
                return { x: item.Hour, y: [lower, upper] };
            });

            // Chart 2: Floating Bars Chart
            const ctx2 = document.getElementById('chart2').getContext('2d');
            new Chart(ctx2, {
                type: 'bar',
                data: {
                    labels: hours,
                    datasets: [{
                        label: 'Floating Average BPM',
                        data: floatingData,
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
                                text: 'Average Heartrate (BPM)'
                            },
                            beginAtZero: true
                        }
                    }
                }
            });
            // Remove this event handler so Chart 2 is rendered only once
            $('#bs-tab2').off("shown.bs.tab");
        });
    })
    .catch(error => console.error('Error:', error));