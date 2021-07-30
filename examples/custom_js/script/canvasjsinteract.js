$( document ).ready( function() {
    // Display initial values for sliders.
    let inputs = [ "n", "m", "rn", "rm" ]
    for ( var i=0;i<=inputs.length;i++ ) {
        nameRange = '#' + inputs[i] + 'Range';
        nameValue = '#' + inputs[i] + 'Value';
        $( nameValue ).html( $( nameRange ).val() );
    }

    // Update displayed values for sliders on slider changes.
    $( '#nRange' ).change(function () { $( '#nValue' ).html( $( '#nRange' ).val() ) });
    $( '#mRange' ).change(function () { $( '#mValue' ).html( $( '#mRange' ).val() ) });
    $( '#rnRange' ).change(function () { $( '#rnValue' ).html( $( '#rnRange' ).val() ) });
    $( '#rmRange' ).change(function () { $( '#rmValue' ).html( $( '#rmRange' ).val() ) });

    // Submit values of sliders to plot point calculator on button click.
    $( "#trigger" ).click( function ( event ) {
        let n = $( '#nRange' ).val().toString();
        let m = $( '#mRange' ).val().toString();
        let rn = $( '#rnRange' ).val().toString();
        let rm = $( '#rmRange' ).val().toString();
        console.log("n: " + n + ", m: " + m + ", rn: " + rn + ", rm: " + rm);

        let url = "http://localhost:8000/plot";
        let data = '{ "n": ' + n + ', "m": ' + m + ', "rn": ' + rn + ', "rm": ' + rm + ' }';
        $.post( url, data, function ( data ) {
            drawChart( data.x, data.y );
        }, "json" );
    })
});

// function drawChart( xVals, yVals ) {
//     data: [
// 		{
// 		type: "line", //change it to column, spline, line, pie, etc
// 		dataPoints: [
// 			{ x: 10, y: 10 },
// 			{ x: 20, y: 14 },
// 			{ x: 30, y: 18 },
// 			{ x: 40, y: 22 },
// 			{ x: 50, y: 18 },
// 			{ x: 60, y: 28 }
// 		]
// 	}
// 	]
// }


function drawChart(xVals, yVals) {
    let data = [];
    for ( var i=0;i<=xVals.length;i++ ) {
        data.push({
            x: xVals[i],
            y: yVals[i]
        });
    }
    console.log(data)
    let options = {
        animationEnabled: false,
        axisX: {
            minimum: -10,
            maximum: 10,
            gridThickness: 0,
            valueFormatString: " ",
            tickLength: 0
        },
        axisY: {
            minimum: -10,
            maximum: 10,
            gridThickness: 0,
            valueFormatString: " ",
            tickLength: 0
        },
        data: [{
            type: "line",
            markerSize: 0,
            dataPoints: data,
        }]
    };
    $( "#spirograph" ).CanvasJSChart(options);
}