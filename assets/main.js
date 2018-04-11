$(function() {
	$('#demoLink').click(function() {
		$('#demo').show();
        $('#home').hide();
        return false;
    });
	$('#homeLink').click(function() {
        $('#demo').hide();
        $('#home').show();
        return false;
    });
});