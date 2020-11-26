var myChart = new frappe.Chart("#myChart", {
    type: 'line',
    title: "Hits per Day",
    colors: ['purple'],
    height:400,
    data: {
        labels: {{ hitarr.keys()|list| safe}},
datasets: [
    {
        values: {{ hitarr.values()|list| safe}} 
    },
]},
axisOptions: {
    yAxisMode: "tick",
    
},
lineOptions: {
    hideDots: 1,
        
            regionFill: 1, // default: 0
},
});
var hourPie = new frappe.Chart("#hourpie", {
    type: 'pie',
    title:"Hourly Hits",
    height:300,
    data: {
        labels: {{ hours| safe}},
datasets: [
    {
    values: {{ hhits| tojson}},
    },
]},
});
var osPie = new frappe.Chart("#ospie", {
    type: 'donut',
    height:300,
    title:"Operating Systems",
    data: {
        labels: {{ os.keys() | list }},
datasets: [{
    values: {{ os.values() | list }},
    }],
},
});