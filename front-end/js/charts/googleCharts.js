
$(function () {
    google.charts.load('current', { 'packages': ['corechart'] });
    google.charts.setOnLoadCallback(function () {
        var options = {
            width: 600,
            height: 400,
            // curveType: 'function',
            vAxis: {
                viewWindow: {
                    min: 0,
                    max: 100,
                },
            }
        };

        var data = new google.visualization.DataTable();
        data.addColumn('string', 'time');
        data.addColumn('number', 'random number');
        data.addRows([]);
        var chart = new google.visualization.LineChart(document.getElementById('chart_div'));
        chart.draw(data, options);

        function datafeed() {

            $.ajaxSetup({
                timeout: 1000 * 10,
                cache: false,
            });

            $.ajax({
                url: "/charts",
                dataType: "json",
                success: function (result, status) {

                    var w = [];

                    w.push(result.x[0], result.y[0])
                    data.addRow(w);

                    if (data.og.length > 20) {
                        data.og.shift();
                        data.hc.shift();
                    }

                    chart.draw(data, options);
                },
                error: function (result, status) {
                    console.log(result);
                }
            });
        };

        setInterval(datafeed, 1000);
    });
});