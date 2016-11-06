	$.widget.bridge('uibutton', $.ui.button);

    $(document).ready(function() {
        $('#rootwizard').bootstrapWizard({
            onTabShow: function(tab, navigation, index) {
                var $total = navigation.find('li').length;
                var $current = index + 1;
                var $percent = ($current / $total) * 100;
                $('#rootwizard').find('.bar').css({
                    width: $percent + '%'
                });
            }
        });
    });


	initializeRatings();

    function initializeRatings() {
      $('#rate').shieldRating({
          max: 10,
          step: 0.1,
          value: 5,
          markPreset: true
      });
    }


$(document).ready(function() {
    $('#summarise').DataTable({
    	stateSave: true,
        data: [],
        columns: [
	        { data: 'Damage Parts' },
	        { data: 'Damage Rating' }
    	]
    });
});

function SendData() {
	console.log("Data is Send to Server");
}