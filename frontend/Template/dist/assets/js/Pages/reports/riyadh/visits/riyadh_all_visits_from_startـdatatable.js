
 
 
 
 var table ; 
 var comment_table ;

function GetURLSearchParams()
{  
    return new Promise(function(resolve,reject){ 
		
		var urlParams = new URLSearchParams(window.location.search);
		// if(urlParams.has('check_FACILITY_EMAIL')){$('#check_FACILITY_EMAIL').prop( "checked", true );} 

        resolve() 
    }) 
     
};

function GetSelectSelectedValues(select_Id) {
	tempList = [] ;
	for (const element of $(select_Id).find(':selected')){tempList.push(element.value)}
	 return tempList;
} 



function Get_datatableQuery(datatable_current_data) {   
	
	
	return { 
		"offset":datatable_current_data['start'] , 
		"limit":datatable_current_data['length'], 
		RAQEB_ENTITY_ID: GetSelectSelectedValues("#RAQEB_ENTITY_ID"),
		ENTITY_VISIT_ID: GetSelectSelectedValues("#ENTITY_VISIT_ID"),
		TASK_TYPE_NAME: GetSelectSelectedValues("#TASK_TYPE_NAME"),
		VISIT_STATUS_NAME: GetSelectSelectedValues("#VISIT_STATUS_NAME"),
		SECTION_NAME: GetSelectSelectedValues("#SECTION_NAME"),
		BILL_STATUS: GetSelectSelectedValues("#BILL_STATUS"),
		BILL_STATUS_NAME: GetSelectSelectedValues("#BILL_STATUS_NAME"),
		BILL_STATUS_1: GetSelectSelectedValues("#BILL_STATUS_1"),
		OWNER_ID_TYPE: GetSelectSelectedValues("#OWNER_ID_TYPE"),
		USER_ID: GetSelectSelectedValues("#USER_ID"),
		OWNER_ID: GetSelectSelectedValues("#OWNER_ID"),
		 
		}



}
 
function Genrate_data(){
   
	 
	return new Promise(function (resolve, reject) {
		table = $('#riyadh_all_visits_from_start_datatable').DataTable({
			 
				
			lengthMenu: [[10, 25, 50, 99999999], [10, 25, 50, "All"]],
			
			responsive: true,
			// searchDelay: 500,
			processing: true,
			serverSide: true,
			autoWidth: false,
			
			buttons: [
				'print',
				'copyHtml5',
				{
					extend: 'excelHtml5',
					exportOptions: {
						columns: [ 7,0,1, ':visible'   ]
					}
				},
				// 'excelHtml5',
				'csvHtml5',
				'pdfHtml5',
			],
			ajax: { 
				url:  Tables_host_Url+`/riyadh/raqeb/visits`,
				type: 'PUT',
				xhrFields: {
					withCredentials: true
				},
				contentType: "application/json", 
				crossDomain: true, 
				data: function name(d) { 
					// delete d.columns
					// delete d.search
					// delete d.order
					// delete d.draw  
					return JSON.stringify( $.extend({}, d, Get_datatableQuery(d)) );  
				},
				dataSrc: function ( json ) {   
					//Make your callback here.  
					return json.data; 
				}, 
				
			}, 
			"createdRow": function( row, data, dataIndex ) { 
			},  
			columns: [ 
				{ 
					data : null,
					visible:true,
					"defaultContent": '' ,
					"targets": 0
				} ,
				 
				{data: 'USER_ID' ,    visible:true   },  
				{data: 'RAQEB_ENTITY_ID' ,    visible:true   },  
				{data: 'ENTITY_VISIT_ID' ,    visible:true   },  
				{data: 'TASK_TYPE_NAME' ,    visible:true   },  
				{data: 'INSPECTION_START' ,    visible:true   },  
				{data: 'INSPECTION_END' ,    visible:false   },  
				{data: 'VISIT_STATUS_ID' ,    visible:false   },  
				{data: 'VISIT_STATUS_NAME' ,    visible:true   },  
				{data: 'COMMENTS' ,    visible:true   },  
				{data: 'SECTION_ID' ,    visible:false   },  
				{data: 'SECTION_NAME' ,    visible:true   },  
				{data: 'BILL_STATUS' ,    visible:false   },  
				{data: 'BILL_STATUS_NAME' ,    visible:true   },  
				{data: 'BILL_STATUS_1' ,    visible:true   },  
				{data: 'OWNER_ID' ,    visible:true   },  
				{data: 'OWNER_ID_TYPE' ,    visible:true   },  
				{data: 'ENTITY_MOBILE' ,    visible:true   },  
				{data: 'OWNER_NAME' ,    visible:true   },  
				{data: 'OWNER_MOBILE' ,    visible:true   },  
				{data: 'TELEPHONE_NUMBER' ,    visible:true   }, 
				{ 
					data : null,
					visible:false,
					"defaultContent": '' ,
					"targets": -1
				} ,


			], 
			columnDefs: [
				
				// { "width": "550px", "targets": "_all" },
				// BUTTON GO TO  FACILITY_ID
				{
					targets: 0,
					title: ' ',
					orderable: false, 
					render: function(data, type, full, meta) {  
						return '\
						<div class="d-flex justify-content-start">\
								<a href="/" class="btn btn-sm btn-clean btn-icon" title="تفاصيل ">\
									<i class="fas fa-external-link-alt fa-1x"></i>\
								</a>\
						</div>\
						';
					},
				}, 
				 

				
				 
				{
					targets: 1, 
					orderable: false,
					title : ' <strong>USER_ID</strong> ',
					render: function(data, type, full, meta) {
					return data;
					},
				},         
			 
				{
					targets: 2, 
					orderable: false,
					title : ' <strong>RAQEB_ENTITY_ID</strong> ',
					render: function(data, type, full, meta) {
					return data;
					},
				},         
			 
				{
					targets: 3, 
					orderable: false,
					title : ' <strong>ENTITY_VISIT_ID</strong> ',
					render: function(data, type, full, meta) {
					return data;
					},
				},         
			 
				{
					targets: 4, 
					orderable: false,
					title : ' <strong>TASK_TYPE_NAME</strong> ',
					render: function(data, type, full, meta) {
					return data;
					},
				},         
			 
				{
					targets: 5, 
					orderable: false,
					title : ' <strong>INSPECTION_START</strong> ',
					render: function(data, type, full, meta) {
					return data;
					},
				},         
			 
				{
					targets: 6, 
					orderable: false,
					title : ' <strong>INSPECTION_END</strong> ',
					render: function(data, type, full, meta) {
					return data;
					},
				},         
			 
				{
					targets: 7, 
					orderable: false,
					title : ' <strong>VISIT_STATUS_ID</strong> ',
					render: function(data, type, full, meta) {
					return data;
					},
				},         
			 
				{
					targets: 8, 
					orderable: false,
					title : ' <strong>VISIT_STATUS_NAME</strong> ',
					render: function(data, type, full, meta) {
					return data;
					},
				},         
			 
				{
					targets: 9, 
					orderable: false,
					title : ' <strong>COMMENTS</strong> ',
					render: function(data, type, full, meta) {
					return data;
					},
				},         
			 
				{
					targets: 10, 
					orderable: false,
					title : ' <strong>SECTION_ID</strong> ',
					render: function(data, type, full, meta) {
					return data;
					},
				},         
			 
				{
					targets: 11, 
					orderable: false,
					title : ' <strong>SECTION_NAME</strong> ',
					render: function(data, type, full, meta) {
					return data;
					},
				},         
			 
				{
					targets: 12, 
					orderable: false,
					title : ' <strong>BILL_STATUS</strong> ',
					render: function(data, type, full, meta) {
					return data;
					},
				},         
			 
				{
					targets: 13, 
					orderable: false,
					title : ' <strong>BILL_STATUS_NAME</strong> ',
					render: function(data, type, full, meta) {
					return data;
					},
				},         
			 
				{
					targets: 14, 
					orderable: false,
					title : ' <strong>BILL_STATUS_1</strong> ',
					render: function(data, type, full, meta) {
					return data;
					},
				},         
			 
				{
					targets: 15, 
					orderable: false,
					title : ' <strong>OWNER_ID</strong> ',
					render: function(data, type, full, meta) {
					return data;
					},
				},         
			 
				{
					targets: 16, 
					orderable: false,
					title : ' <strong>OWNER_ID_TYPE</strong> ',
					render: function(data, type, full, meta) {
					return data;
					},
				},         
			 
				{
					targets: 17, 
					orderable: false,
					title : ' <strong>ENTITY_MOBILE</strong> ',
					render: function(data, type, full, meta) {
					return data;
					},
				},         
			 
				{
					targets: 18, 
					orderable: false,
					title : ' <strong>OWNER_NAME</strong> ',
					render: function(data, type, full, meta) {
					return data;
					},
				},         
			 
				{
					targets: 19, 
					orderable: false,
					title : ' <strong>OWNER_MOBILE</strong> ',
					render: function(data, type, full, meta) {
					return data;
					},
				},         
			 
				{
					targets: 20, 
					orderable: false,
					title : ' <strong>TELEPHONE_NUMBER</strong> ',
					render: function(data, type, full, meta) {
					return data;
					},
				},         
			


				
				{
					targets: -1,
					title: ' ',
					orderable: false, 
					render: function(data, type, full, meta) {  
						return `\
						<div class="d-flex justify-content-start">\
								<a data-bs-toggle="modal" data-bs-target="#kt_modal_Entity_POP_Details" onClick=GetRecord('${data["FACILITY_ID"]}') target="_blank" class="btn btn-sm btn-clean btn-icon" title="تفاصيل المبنى ">\
									<i class="las la-eye fs-2x"></i>\
								</a>\
						</div>\
						`;
					},
				},

			],
			initComplete: function() {  
				$(".form-select").select2({
							tags: true,
							tokenSeparators: [',']
					});
				resolve()
			},
		});
		
	})
		
  
}

$(".checkbox_filter").change(function() {
    $('#kt_search').click()
});

$('#kt_search').on('click', function(e) {
	e.preventDefault();
	  
	table.destroy(); 
	Genrate_data(); 
	return false;
});

	
$('#kt_reset').on('click', function(e) {
	location.reload();
}); 

$('#export_copy').on('click', function(e) {
	e.preventDefault();
	table.button(1).trigger();
});

$('#export_excel').on('click', function(e) {
	e.preventDefault();
	table.button(2).trigger();
});

$('#export_csv').on('click', function(e) {
	e.preventDefault();
	table.button(3).trigger();
});
 
promises = []
promises.push( 
				// Get_INSPECTION_LICENSING_NUMBER_FOR_INVESTOR_Values(),
				GetURLSearchParams().then(() => {   
					   
											Genrate_data();
                                        }
                                )
								
             ) 
Promise.all(promises).then(() => {  
	 
	
 });

 