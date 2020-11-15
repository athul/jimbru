var ctx = document.getElementById('myChart').getContext('2d');
var ptx = document.getElementById('hourpie').getContext('2d');
var ostx = document.getElementById('ospie').getContext('2d')
var myChart = new Chart(ctx, {
    type: 'line',
    data: {
        labels: {{ days| safe}},
datasets: [{
    label: '# of Hits',
    data: {{ hitarr| tojson}},
    backgroundColor: [
    'rgba(255, 99, 132, 0.2)',
],
    pointBackgroundColor: 'tomato',
    borderColor: [
    'crimson',
],
    borderWidth: 1
            }]
        },
options: {
    responsive: false,
        title: {
        display: true,
            text: 'Hits in Last 7 days'
    },
    scales: {
        yAxes: [{
            ticks: {
                fontColor: "rgba(0,0,0,0.5)",
                fontStyle: "bold",
                beginAtZero: true,
                maxTicksLimit: 5,
                padding: 10
            },
            gridLines: {
                drawTicks: false,
                display: false
            }

        }],
            xAxes: [{
                gridLines: {
                    zeroLineColor: "transparent"
                },
                ticks: {
                    fontColor: "rgba(0,0,0,0.5)",
                    fontStyle: "bold"
                }
            }]
    }
}
    });
var hourPie = new Chart(ptx, {
    type: 'pie',
    data: {
        labels: {{ hours| safe}},
datasets: [{
    data: {{ hhits| tojson}},
    backgroundColor: [
    "tomato", "crimson", "blue", "green", "pink", "rebeccapurple", "black", "yellow", "orange", "magenta", "lime", "royalblue",
],
            }]
        },
options: {
    responsive: false,
        title: {
        display: true,
            text: 'Hourly Hits'
    }
}
    });
var osPie = new Chart(ostx, {
    type: 'polarArea',
    data: {
        labels: {{ os.keys() | list }},
datasets: [{
    data: {{ os.values() | list }},
    backgroundColor: [
    "tomato",
    "crimson",
    "blue",
    "green",
    "pink",
    "rebeccapurple",
],
            }]
        },
options: {
    responsive: false,
        title: {
        display: true,
            text: 'Operating Systems'
    }
}
    });