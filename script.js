$(document).ready(function() {
    $('#calculatorForm').submit(function(e) {
        e.preventDefault();
        var realPart = parseFloat($('#realPart').val());
        var imaginaryPart = parseFloat($('#imaginaryPart').val());

        var magnitude = Math.sqrt(Math.pow(realPart, 2) + Math.pow(imaginaryPart, 2));
        var angle = Math.atan2(imaginaryPart, realPart) * (180 / Math.PI);

        $('#result').html('Magnitude: ' + magnitude.toFixed(2) + ', Angle: ' + angle.toFixed(2) + ' degrees');
        $('#result').show();
    });
});
