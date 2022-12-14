var waiting_time ;
var plus_forEach ;
var current_pass ;

function googleDriveUploade_download_and_send_to_s3(file_name,file_id) {
	
		 
	  var settings = {
		"url": upload_media_app_host_Url+"/media/googledrive/download_and_send_to_s3/"+file_name+"/"+file_id,
		"method": "PUT",
		"timeout": 0,
	  };
	  
	  $.ajax(settings).done(function (response) {
		
			current_pass = current_pass + plus_forEach
			$('#googleDriveUploade_progress').attr('style',`width: ${current_pass}%`)
	  });


}

function loob_forEach_googleDriveUploade_files(resposne) {
	
	for (let item of resposne) { 
		 
		googleDriveUploade_download_and_send_to_s3(item.file_name,item.file_id)
	}

}

function googleDriveUploade() {

	var kt_daterangepicker_4_range = $("#kt_daterangepicker_4").val().split('~')
	date_from = kt_daterangepicker_4_range[0].trim();
	date_to = kt_daterangepicker_4_range[1].trim();


	var settings = {
		"url": upload_media_app_host_Url+"/media/googledrive/fithcgoogledrive",
		"method": "PUT",
		"timeout": 0,
		"headers": {
			"accept": "application/json",
			"Content-Type": "application/json"
		},
		"data": JSON.stringify({
			"trashed": false,
			"createdTime_from": date_from,
			"createdTime_to": date_to
		}),
	};

	$.ajax(settings).done(function (response) {
		 
		waiting_time = response.length;
		plus_forEach = 100 / waiting_time;
		current_pass = 0;
		 
		if(waiting_time == 0){
			Swal.fire({
				title: `تم العثور على ${waiting_time} من الملفات  `,
				text: "  يرجى التحقق من التواريخ  ",
				icon: 'warning',
				showCancelButton: false,
				confirmButtonColor: '#3085d6',
				cancelButtonColor: '#d33',
				confirmButtonText: ' حسناً '
			}).then(() => {
				$("#kt_daterangepicker_4").click()
			})
		}
		else
		{

			Swal.fire({
				title: `تم العثور على ${waiting_time} من الملفات  `,
				text: " هل تريد المتابعه والرفع ؟ ",
				icon: 'warning',
				showCancelButton: true,
				confirmButtonColor: '#3085d6',
				cancelButtonColor: '#d33',
				confirmButtonText: ' نعم ',
				cancelButtonText: ' لا '
			}).then((result) => {
				if (result.isConfirmed) {
	
					// $("#googleDriveUploade_btn").attr("data-kt-indicator", "on");
					loob_forEach_googleDriveUploade_files(response);
	
				} else {
					// do nothing !! 
				}
			})

		}
		

		// console.log(response);
	});




}

function media_get_pafy_url() {

	video_url_txt = $("#video_url_txt").val()


	var settings = {
		"url": upload_media_app_host_Url+"/media/livecam/get_pafy_url",
		"method": "PUT",
		"timeout": 0,
		"headers": {
			"accept": "application/json",
			"Content-Type": "application/json"
		},
		"data": JSON.stringify({
			"video_url": video_url_txt
		}),
	};


	$.ajax(settings).done(function (response) {
		alert('done')
		$("#pafy_url_txt").val(response)
		console.log(response);
	});


}

function media_capturelivevideo() {

	media_capturelivevideo_url = $("#pafy_url_txt").val()


	var settings = {
		"url": upload_media_app_host_Url+"/media/livecam/capturelivevideo",
		"method": "PUT",
		"timeout": 0,
		"headers": {
			"accept": "application/json",
			"Content-Type": "application/json"
		},
		"data": JSON.stringify({
			"pafy_url": media_capturelivevideo_url,
			"capterMainFolder":"LONDON_BUS_RIDES",
			"captureSubFolder":"V00D4K9OshI",
		}),
	};


	$.ajax(settings).done(function (response) {
		alert('done')
		console.log(response);
	});


}












const fileInput = document.querySelector("#fileInput");

const uploadFile = file => {
	console.log("Uploading file...");
	const API_ENDPOINT = upload_media_app_host_Url+"/media/s3/sendToS3/manual_upload";
	const request = new XMLHttpRequest();
	const formData = new FormData();

	request.open("POST", API_ENDPOINT, true);
	request.onreadystatechange = () => {
		if (request.readyState === 4 && request.status === 200) {
 
			alert('DONE ');
		}
	};
	formData.append("file", file);
	request.send(formData)
}

fileInput.addEventListener("change", event => {
	const files = event.target.files;
	uploadFile(files[0]);

});