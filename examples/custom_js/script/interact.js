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
            draw( "#spirograph", data.x, data.y );
        }, "json" );
    })
});

function draw(elementName, x, y) {
    // set up canvas
    const canvas = document.querySelector( elementName );

    if (!canvas.getContext) {
        console.log("No canvas found!")
        return;
    }
    const ctx = canvas.getContext('2d');

    // Clear the canvas ahead of drawing
    ctx.clearRect(0, 0, canvas.width, canvas.height);

    // set line stroke and line width
    ctx.strokeStyle = 'blue';
    ctx.lineWidth = 1;

    // set starting point at centre of canvas
    let xCentre = 0.5 + 0.5*canvas.width;
    let yCentre = 0.5 + 0.5*canvas.height;
    let scale = 0.05*canvas.width;

    // draw a line
    ctx.beginPath();
    for ( var i=0; i<=x.length; i++ ) {
        if ( i===0 ) {
            // move to the first point
            ctx.moveTo( ( x[i]*scale )+xCentre, ( y[i]*scale )+yCentre );
        } else {
            // now draw lines to all successive points
            ctx.lineTo( ( x[i]*scale )+xCentre, ( y[i]*scale )+yCentre );
        }
    }

    ctx.stroke();
}