function init() {

    var chartData1 = {
        labels: null,
        datasets: [{
            label: '每件產品產生時間區間',
            data: null,
            backgroundColor: 'rgba(0, 255, 0, 0.6)',
            borderColor: 'rgba(0,255,0,1)',
            borderWidth: 1,
        }],
    };
    var chartOptions1 = {
        scales: {
            yAxes: [{
                ticks: {
                    suggestedMin: 0,
                    suggestedMax: 6,
                },
            }],
        },
    };


    var chartData2 = {
        labels: null,
        datasets: [{
            label: '當日累積產量',
            data: null,
            backgroundColor: 'rgba(223, 158, 18, 0.1)',
            borderColor: 'rgba(223, 158, 18, 1)',
            borderWidth: 1,
        }],
    };
    var chartOptions2 = {
        scales: {
            yAxes: [{
                ticks: {
                    suggestedMin: 0,
                    // suggestedMax: 6,
                },
            }],
        },
        // animation: {
        //     duration: 0
        // },
    };


    var ctx1 = document.getElementById('timeSpan').getContext('2d');
    var ctx2 = document.getElementById('productCumulate').getContext('2d');

    var myChart1 = new Chart(ctx1, {
        type: 'bar',
        data: chartData1,
        options: chartOptions1,
    });

    var myChart2 = new Chart(ctx2, {
        type: 'line',
        data: chartData2,
        options: chartOptions2,
    });


    function rand3() {
        var rnd = Math.round(Math.random() * 4) - 2;
        return 3 - rnd;
    }


    var x1 = [];    // 每片產出
    var y1 = [];
    var x2 = [];    // 累積產量
    var y2 = [];
    var q = 0;      // 累積產量Q

    function pp() {
        q++;
        var stopTiming = rand3();
        x1.push(new Date().toTimeString().substring(0, 8));
        y1.push(stopTiming);
        myChart1.data.labels = x1;
        myChart1.data.datasets[0].data = y1;

        if (x1.length > 8) {
            x1.shift();
            y1.shift();
        }


        myChart1.update();


        setTimeout(pp, stopTiming * 1000);
    };

    setInterval(function() {
        x2.push(new Date().toTimeString().substring(0, 8));
        y2.push(q);
        myChart2.data.labels = x2;
        myChart2.data.datasets[0].data = y2;

        // if (x2.length > 10) {
        //     x2.shift();
        //     y2.shift();
        // }

        myChart2.update();

    }, 10 * 1000);

    pp();
}




window.addEventListener('load', init, false);

