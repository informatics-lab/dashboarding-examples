$( document ).ready( function() {
    $( "#trigger" ).click( function ( event ) {
        let n = $( '#nValue' ).val().toString();
        let m = $( '#mValue' ).val().toString();
        let rn = $( '#rnValue' ).val().toString();
        let rm = $( '#rmValue' ).val().toString();
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