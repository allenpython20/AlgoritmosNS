$(document).ready(function() {

	$('.numero-cluster').click(function(){

		const cluster = $(this).find('.valor-cluster').val()

		$('#carga-info-cluster').load("/carga_info/"+cluster,function(){
			$('html, body').animate({
	        	scrollTop: parseInt($("#divResultados").offset().top-76)
	    	}, 1000);
		})

		

		
	})



});