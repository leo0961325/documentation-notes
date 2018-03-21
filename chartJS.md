# Chart.js



畫圖語法備註
```js
$(document).ready(function() {
    var chartdata = {
        labels: null,
        datasets: [{
            label: "My First dataset",
            //backgroundColor: 'rgb(255, 99, 132)',
            borderColor: 'rgb(255, 99, 132)',
            data: null,
        }]
    };
    var chartoptions = {
        scales:{
            yAxes: [{
                ticks: {
                    beginAtZero:true,
                    min: 120,
                    max: 180,
                    stepSize: 20
            }
        }]

        }
    };
    var ctx = document.getElementById('myChart').getContext('2d');
    var myChart = new Chart(ctx, {
    // The type of chart we want to create
        type: 'line',
        data: chartdata,
        options: chartoptions
    });
    
    var d_list = [];
    var v_list = []; 
    var getData = function() {
        $.get("{% url 'ajax' %}") 
        .done(function(alldata,status) {
            //放一個計數器隨時看到當前的value
            $("#ajaxtest").html(alldata.value)
            //for(var i in alldata){
            d_list.push(alldata.da);
            v_list.push(alldata.value);
            //}
            //alert(v_list)
            if(d_list.length>10){
                d_list.shift();
            }
            if(v_list.length>10){
                v_list.shift();
            }
            myChart.data.labels = d_list;
            myChart.data.datasets[0].data = v_list;
            myChart.update();
        })
    };
    var time1 = setInterval(getData,2000); 
});
```